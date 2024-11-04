from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404

from .forms import InventaryzationAddForm
from .models import Inventaryzation
from django.contrib import messages
from .services import inventar_number, ParsExcel, relations, CreateExcel
from django.http import FileResponse

# Create your views here.

# module inventaryzation
def inventaryzation(request):
    all_items = Inventaryzation.objects.all().order_by('id')
    all_cars = Inventaryzation.objects.filter(group="Автомобілі")
    all_furnitures = Inventaryzation.objects.filter(group="Меблі")
    all_bulddings = Inventaryzation.objects.filter(group="Будівлі")
    all_office_equipments = Inventaryzation.objects.filter(group="Орг.техніка")
    all_peripheres = Inventaryzation.objects.filter(group="Периферія")
    all_PC_and_laptops = Inventaryzation.objects.filter(group="Ноутбуки та ПК")
    all_smartphone_and_tablet = Inventaryzation.objects.filter(group="Смартфони та планшети")
    all_warehouse_equipment = Inventaryzation.objects.filter(group="Складське обладнання")
    all_interior_items = Inventaryzation.objects.filter(group="Предмети інтерєру")

    context = {
        'all_items': all_items,
        'all_cars': all_cars,
        'all_furnitures': all_furnitures,
        'all_bulddings': all_bulddings,
        'all_office_equipments': all_office_equipments,
        'all_peripheres': all_peripheres,
        'all_PC_and_laptops': all_PC_and_laptops,
        'all_smartphone_and_tablet': all_smartphone_and_tablet,
        'all_warehouse_equipment': all_warehouse_equipment,
        'all_interior_items': all_interior_items
    }

    return render(request, "inventaryzation/inventaryzation.html", context=context)


def inv_add_new_item(request):
    if request.FILES:
        file = request.FILES['upload']
        ParsExcel(file).parse()
        messages.success(request, "Об'єкти додано")
        return HttpResponseRedirect('/inventaryzation')

    if request.method == 'POST':
        new_item_form = InventaryzationAddForm(request.POST)
        if new_item_form.is_valid():
            new_item = new_item_form.cleaned_data
            try:
                test = Inventaryzation.objects.get(serial=new_item['serial'])
                messages.error(request, 'Такий серійний номер вже зареєстровано')
            except:
                item = Inventaryzation.objects.create(
                    group=new_item['group'],
                    name=new_item['name'],
                    model=new_item['model'],
                    serial=new_item['serial'],
                    inv_numb=inventar_number(),
                    location=new_item['location'],
                    responsible=new_item['responsible'],
                    description=new_item['description'],
                    price=new_item['price'],
                    date_of_purchase=new_item['date_of_purchase'],
                    market_price=new_item['market_price'],
                    date_of_registration=new_item['date_of_registration']
                )
            return HttpResponseRedirect('/inventaryzation')

    inventaryzation_add_form = InventaryzationAddForm()
    context = {
        'invent_add_form': inventaryzation_add_form
    }

    return render(request, "inventaryzation/inv_add_new_item.html", context=context)


def download(request):

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
                items = Inventaryzation.objects.filter(group=relations[value]).order_by('id')
                for item in items:
                    item_atr_list = list(vars(item).values())[1:]
                    excel.push_objects(item_atr_list)

        filename = excel.table_path
        excel.save_excel()

        return FileResponse(open(f'{filename}', 'rb'))

    context = {}
    return render(request, 'inventaryzation/download.html', context)


def upload(request):
    pass