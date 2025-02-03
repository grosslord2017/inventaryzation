import json
from importlib.resources import contents

from .forms import InventaryzationAddForm
from operator import attrgetter
from .models import Inventaryzation, ArchiveUtil, Jurnal, Act, InventarNumberTemp
from time import strftime as st
from iris.settings import BASE_DIR
from django.contrib import messages
from django.db.models import Q
from django.http import FileResponse
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from .services import (inventar_number, ParsExcel, relations, CreateExcel, formating_for_ajax_response,
                       get_all_group, get_all_locations, get_all_workers, CreateActFiles)


# Create your views here.

# module inventaryzation
def inventaryzation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    all_items = Inventaryzation.objects.all().order_by('id')

    context = {
        'all_items': all_items,
        'locations': get_all_locations(),
        'groups': get_all_group()
    }

    return render(request, "inventaryzation/inventaryzation.html", context=context)

# страница создания нового объекта
def inv_add_new_item(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    if request.FILES:
        file = request.FILES['upload']
        # заменить метод parse_temp на parse(если затягивание без инвентарных номеров)
        # ParsExcel(file).parse()
        pars = ParsExcel(file, request.user)
        pars.parse_temp()
        count_items = pars.count_items
        messages.success(request, f"Об'єкти додано: {count_items}")
        return HttpResponseRedirect('/inventaryzation')

    if request.method == 'POST':
        new_item_form = InventaryzationAddForm(request.POST)
        if new_item_form.is_valid():
            new_item = new_item_form.cleaned_data
            try:
                Inventaryzation.objects.get(serial=new_item['serial'])
                messages.error(request, 'Такий серійний номер вже зареєстровано')
            except:
                try:
                    Inventaryzation.objects.get(inv_numb=new_item['inv_numb'])
                    messages.error(request, 'Такий інвентарний номер вже зареєстровано')
                except:
                    act = CreateActFiles(request.user)
                    #invent_numb = inventar_number()
                    Inventaryzation.objects.create(
                        group=new_item['group'],
                        name=new_item['name'],
                        model=new_item['model'],
                        serial=new_item['serial'] if new_item['serial'] != '-' else new_item['inv_numb'],
                        inv_numb=new_item['inv_numb'],
                        location=new_item['location'],
                        responsible=new_item['responsible'],
                        description=new_item['description'],
                        price=new_item['price'],
                        date_of_purchase=new_item['date_of_purchase'],
                        market_price=new_item['market_price'],
                        date_of_registration=new_item['date_of_registration']
                    )

                    item = [atr for atr in new_item.values()]
                    act.add_new([item])
            return HttpResponseRedirect('/inventaryzation')

    inventaryzation_add_form = InventaryzationAddForm()
    context = {
        'invent_add_form': inventaryzation_add_form
    }

    return render(request, "inventaryzation/inv_add_new_item.html", context=context)

# модальное окно с выбором категорий для выгрузки в файл
def download(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    if request.POST:
        excel = CreateExcel()

        if request.POST.get('all_items'):
            all_items = Inventaryzation.objects.all().order_by('id')
            for item in all_items:
                item_atr_list = list(vars(item).values())[1:]
                excel.push_objects(item_atr_list)

        else:
            for value in request.POST:
                if value == 'csrfmiddlewaretoken':
                    continue
                # items = Inventaryzation.objects.filter(group=relations[value]).order_by('id')
                items = Inventaryzation.objects.filter(location=relations[value]).order_by('id')
                for item in items:
                    item_atr_list = list(vars(item).values())[1:]
                    excel.push_objects(item_atr_list)

        filename = excel.table_path
        excel.save_excel()

        return FileResponse(open(f'{filename}', 'rb'))

    context = {}
    return render(request, 'inventaryzation/download.html', context)

# страница создания инвентарных штрих-кодов
def generate_inventar_number(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    return render(request, 'inventaryzation/generate_inventar_number.html', {})

# смена материально ответственного
def change_responsible(request):
    if not request.user.is_superuser:
        return Http404

    workers = get_all_workers()

    if request.method == "POST":
        # 'select_first_user': ['Волошко Максим'], 'select_second_user': [''], 'serial': ['24XSI02', '66762085562']
        responsible_now = request.POST.get('select_first_user')
        responsible_then = request.POST.get('select_second_user')
        items_serial = request.POST.getlist('serial')

        if responsible_then != '':
            items = []
            for serial in items_serial:
                item = Inventaryzation.objects.get(serial=serial)
                items.append(item)

            create_file = CreateActFiles(request.user)
            # act_id = create_file.transfer(items, responsible_then)
            create_file.transfer(items, responsible_then)

            for item in items:
                item.responsible = responsible_then
                item.save()

        return HttpResponseRedirect('/inventaryzation')

    context = {
        "all_workers": workers
    }
    return render(request, 'inventaryzation/change_responsible.html', context=context)

# списание
def utilization(request):
    if not request.user.is_superuser:
        return Http404

    if request.method == "POST":
        invent_numb = request.POST.getlist('invent_numb')
        description_temp = request.POST.getlist('description') # может прийти пустая строка если какой-то элемент пропустить
        items = [] # все обьекты которые утилизируем
        description = [] # список причин списания

        create_file = CreateActFiles(request.user)

        for temp in description_temp: # отсеиваем пустые причины списания
            if temp:
                description.append(temp)

        for temp in invent_numb:
            items.append(Inventaryzation.objects.get(inv_numb=temp))
    # -------------------Розбивка на пользователей для формирования акта------------------------
        zip_item_description_list = [list(tup) for tup in zip(items, description)] # связываем попарно итем и причину списания

        items_sort = list(sorted(items, key=attrgetter('responsible'))) # сортируем по МВО
        check_responsible = items_sort[0].responsible
        items_for_act = []
        for item in items_sort:
            if item.responsible != check_responsible:
                check_responsible = item.responsible
                # print(items_for_act) # отправляем на формирование акта сгрупированых пользователей
                create_file.utilization(items_for_act)
                items_for_act.clear()
                for item_description in zip_item_description_list:
                    if item in item_description:
                        items_for_act.append(item_description)
            else:
                for item_description in zip_item_description_list:
                    if item in item_description:
                        items_for_act.append(item_description)
        if items_for_act:
            # print(items_for_act) # если спиоок ен пуст - отправляем последний на формирование акта
            create_file.utilization(items_for_act)

        messages.success(request, f"Об'єкти списано успішно.")
        return HttpResponseRedirect('/inventaryzation')

    context = {}
    return render(request, 'inventaryzation/utilization.html', context=context)

# страница актов
def all_acts(request):
    all_files = Act.objects.all().order_by('id').reverse()
    context = {'all_files': all_files}
    return render(request, 'inventaryzation/all_acts.html', context=context)

# страница истории действий в базе
def jurnal(request):
    info = Jurnal.objects.order_by('date_operation').reverse()
    context = {
        'info': info,
    }
    return render(request, 'inventaryzation/jurnal.html', context=context)



# ---------- AJAX -----------------------------------------------------------------------------------------------------
# живой поиск по инвентарному номеру и Фамилии
def search(request):
    item = json.loads(request.body).get("item")
    items = (Inventaryzation.objects.filter(Q(inv_numb__startswith=item)) or
             Inventaryzation.objects.filter(Q(responsible__startswith=item)) or
             Inventaryzation.objects.filter(Q(serial__startswith=item)))
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list})

# фильры по нажатии на кнопку локации
def filter_location(request):
    location = json.loads(request.body).get("item")
    items = Inventaryzation.objects.filter(location=location)
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list})

# фильтры по нажатии на кнопку групы
def filter_group(request):
    group = json.loads(request.body).get("item")
    items = Inventaryzation.objects.filter(group=group)
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list})

# фильтр по нажатии на кнопку даты
def filter_date(request):
    dates = json.loads(request.body).get("item")
    items_purch = Inventaryzation.objects.filter(date_of_purchase__range=[dates[0], dates[1]])
    items_registr = Inventaryzation.objects.filter(date_of_registration__range=[dates[0], dates[1]])
    items = []
    for list_of_items in [items_purch, items_registr]:
        for item in list_of_items:
            items.append(item)
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list})

# фильтр по нажатии на кнопку цены
def filter_price(request):
    price = json.loads(request.body).get("item")
    items = []
    items_price = Inventaryzation.objects.filter(price__range=[int(price[0]), int(price[1])])
    items_market_price = Inventaryzation.objects.filter(market_price__range=[int(price[0]), int(price[1])])
    for list_of_items in [items_price, items_market_price]:
        for item in list_of_items:
            items.append(item)
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list})

# фильтр объектов по материально ответственому лицу
def items_in_responsible(request):
    worker = json.loads(request.body).get("item")
    items = Inventaryzation.objects.filter(responsible=worker)
    items_list = formating_for_ajax_response(items)
    return JsonResponse({'items_list': items_list })

# создание уникальных инвентарных номеров по переданому количеству
def quantity_barcode(request):
    quantity = json.loads(request.body).get("item")
    items_list = []
    count = 0
    while count < int(quantity):
        number = inventar_number()
        items_list.append(number)
        count += 1

    return JsonResponse({"items_list": items_list})
