from django.shortcuts import render, redirect

from store.models import Category


# Create your views here.

def list_category_view(request):
    category = Category.objects.all()
    return render(request, 'list_category.html', {'category': category})


def detail_category_view(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'view_category.html', {'category': category})


def create_category_view(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        key = request.POST.get('category_key')
        category = Category.objects.create(name=name,key=key)
    return render(request, 'create_category.html')



def update_category_view(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST.get('category_name',category.name)
        category.key = request.POST.get('category_key',category.key)
        category.save()

    return render(request, 'view_category.html', {'category': category})


def delete_category_view(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('list_category')


# ----------------------------------------------------

def product_list_view(request):
    pass


def product_detail_view(request):
    pass


def product_create_view(request):
    pass


def product_update_view(request):
    pass


def product_delete_view(request):
    pass
