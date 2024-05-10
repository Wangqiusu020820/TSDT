from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     new_item_text = request.POST.get('item_text', '')
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''

    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text,
    # })
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-new-page/')
    return render(request, 'home.html')
    # items = Item.objects.all()
    # return render(request, 'home.html', {'items': items})

def view_list(request, list_id):
    list_user = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_user)
    return render(request, 'list.html', {'list': list_user})

def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')

def add_item(request, list_id):
    list_user = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/{list_user.id}/')