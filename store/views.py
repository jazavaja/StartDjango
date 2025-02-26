from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from store.models import Category, Product


# Create your views here.
def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied()

        return wrapper

    return decorator


@group_required('Admin')
def list_category_view(request):
    user = request.user.groups.filter(name='Admin').exists()
    category = Category.objects.all()
    return render(request, 'list_category.html', {'category': category, 'is_admin': user})


@login_required
@permission_required('store.increase_price', raise_exception=True)
def create_category_view(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        key = request.POST.get('category_key')
        Category.objects.create(name=name, key=key)
    return render(request, 'create_category.html')


def is_admin(user):
    print("hello: ", user.is_superuser)
    if user.is_superuser:
        return True
    else:
        # return False
        raise PermissionDenied("You do not have permission to access this resource.")


@user_passes_test(is_admin, login_url="/", )
def update_category_view(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST.get('category_name', category.name)
        category.key = request.POST.get('category_key', category.key)
        category.save()

    return render(request, 'view_category.html', {'category': category})


def delete_category_view(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('list_category')


# ----------------------------------------------------

def product_list_view(request):
    search = request.GET.get('search_input')
    if search:
        products = Product.objects.filter(name__contains=search)
    else:
        products = Product.objects.all()

    return render(request, 'product_list_view.html', {'products': products})


def product_create_view(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_category = request.POST.get('product_category')

        print(f"Product name {product_name} .. price {product_price} ... category {product_category}")
        product = Product(name=product_name, price=product_price, category_id=product_category)
        product.save()

    category = Category.objects.all()
    return render(request, 'product_create.html', {'category': category})


def product_update_view(request, id):
    category = Category.objects.all()
    p = Product.objects.get(id=id)
    if request.method == "POST":
        p.name = request.POST.get('product_name')
        p.price = request.POST.get('product_price')
        p.category_id = request.POST.get('product_category')
        p.save()

    return render(request, 'product_update_view.html', {'product': p, 'category': category})


def product_delete_view(request, id):
    p = Product.objects.get(id=id)
    p.delete()
    return redirect('list_products')
