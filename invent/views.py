import datetime
import json

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User, Group, Permission
from django.http.response import JsonResponse

from .forms import AddNewItem
from .models import Item, Worker, Location, History
from django.contrib import messages
from .services import add_to_history
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required

# Create your views here.


def home(request):

    items = Item.objects.all()
    workers = Worker.objects.all().order_by('surname')
    locations = Location.objects.all()
    user = request.user

    items_name = set([item.name for item in items])

    context = {
        'user': user,
        'workers': workers,
        'items': items,
        'locations': locations,
        'items_name': items_name
    }
    return render(request, 'invent/home.html', context=context)


def items_list(request, pk):
    items = Item.objects.filter(name=pk)
    return render(request, 'invent/items_list.html', {'items': items})


def worker_items_list(request, pk):
    worker = Worker.objects.get(id=pk)
    items = Item.objects.filter(worker=worker)
    context = {
        'items': items,
        'worker': worker,
    }
    return render(request, 'invent/worker_items_list.html', context=context)


def add_new_item(request):
    if not request.user.is_superuser:
        return Http404()

    if request.method == 'POST':
        new_item_form = AddNewItem(request.POST)
        if new_item_form.is_valid():
            new_item = new_item_form.cleaned_data
            item = Item.objects.create(
                name=new_item['name'],
                model=new_item['model'],
                serial=new_item['serial'],
                description=new_item['description'],
                date_of_purchase=new_item['date_of_purchase'],
                price=new_item['price'],
                is_reserve=new_item['is_reserve']
            )
            item.worker.set(new_item['worker'])
# log
            if new_item['worker']:
                workers = [str(worker) for worker in new_item['worker']]
                add_to_history(request.user, 'додавання', item, f'додавання для {", ".join(workers)}')
            else:
                add_to_history(request.user, 'додавання', item, 'додавання в резерв')

        return HttpResponseRedirect('/invent')

    new_item = AddNewItem()
    return render(request, 'invent/adding_new_item.html', {'add_new': new_item})


def moving_item(request):
    if not request.user.is_superuser:
        return Http404()

    if request.method == 'POST':
        response = request.POST

        try:
            if Location.objects.get(id=int(response['locations_dst'])).marker == 'shop' and response['locations_dst'] != '0':
                workers_dst = Worker.objects.filter(location__id=int(response['locations_dst']))
            else:
                workers_dst = request.POST.getlist('workers_dst') # for meny item

                # workers_dst = Worker.objects.filter(id=int(response['workers_dst'])) # fro 1 item

        except:
            pass

        items_id = response.getlist('items')
        if items_id:

            if response['locations_src'] == '0' and response['locations_dst'] != '0': # from reserve in user
                for i_id in items_id:
                    item = Item.objects.get(id=int(i_id))
                    item.is_reserve = False
                    item.worker.set(workers_dst)
                    dst = [str(i) for i in workers_dst]
                    if not dst:
                        messages.error(request, 'you have nоt chosen destination')
                    else:
                        item.save()
                        messages.success(request, 'successful transfer from reserve to user')
# log
                        add_to_history(request.user, 'переміщення', item, f'Резерв ---> {dst}')

            elif response['locations_src'] != '0' and response['locations_dst'] != '0': # from user in user
                for i_id in items_id:
                    item = Item.objects.get(id=int(i_id))
                    src = [str(i) for i in item.worker.all()]
                    item.worker.set(workers_dst)
                    dst = [str(i) for i in item.worker.all()]
                    item.save()
                    messages.success(request, 'successful transfer from user to user')
# log
                    add_to_history(request.user, 'переміщення', item, f'{src} ---> {dst}')


            elif response['locations_src'] != '0' and response['locations_dst'] == '0': # from user in reserve
                for i_id in items_id:
                    item = Item.objects.get(id=int(i_id))
                    item.is_reserve = True
                    src = [str(i) for i in item.worker.all()]
                    item.worker.set([])
                    item.save()
                    messages.success(request, 'successful transfer from user to reserve')
# log
                    add_to_history(request.user, 'переміщення', item, f'{src} ---> Резерв')

            else:
                messages.info(request, 'Nothing moved')

            return HttpResponseRedirect('/invent')

        else:
            messages.error(request, 'No item selected')

    locations = Location.objects.all()
    context = {
        'locations': locations
    }
    return render(request, 'invent/moving_item_form.html', context=context)


# TODO:
# add function deleting workers and set all items parameters 'is_reserve'


def history(request):
    if not request.user.is_superuser:
        return Http404()

    all_entries = History.objects.all().order_by('-id')
    return render(request, 'invent/history.html', {'all_entries': all_entries})



# ----------- AJAX ------------- #
# select all workplace in location by request
def ajax_location_workers(request):
    location_id = json.loads(request.body).get("locId")

    if location_id != '0':
        work_list = []
        workers = Worker.objects.filter(location=Location.objects.get(id=location_id))

        for worker in workers:
            work_list.append([worker.surname, worker.name, worker.id])

        return JsonResponse({'work_list': work_list})
    else:
        item_stock_list = []
        items = Item.objects.filter(is_reserve=True)

        for item_stock in items:
            item_stock_list.append([item_stock.id, item_stock.name, item_stock.model, item_stock.serial])

        return JsonResponse({'item_stock_list': item_stock_list})

# select all items in workplace by request
def ajax_worker_items(request):
    worker_id = json.loads(request.body).get("workId")
    items = Item.objects.filter(worker=Worker.objects.get(id=worker_id))
    items_list = []
    for item in items:
        items_list.append([item.id, item.name, item.model, item.serial])

    return JsonResponse({'items_list': items_list})

# requested item is decommissioned (предмет списанн)
def ajax_decommissioned(request):
    item_id = json.loads(request.body).get('item_id')
    item = Item.objects.get(id=item_id)
    item.is_decommissioned = True
    item.worker.set([])
    item.date_of_decommissioned = datetime.date.today()
    item.save()
# log
    add_to_history(request.user, 'списание', item)

    return JsonResponse({})
