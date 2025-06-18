from django.shortcuts import render, redirect , get_object_or_404
from app.models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login



# Create your views here.

def home(request):
    all_products = Product.objects.all()
    return render(request, 'app/home.html', {'products': all_products})


@login_required(login_url='login')
def products(request):
    query = request.GET.get('q')  
    if query:
        all_products = Product.objects.filter(name__icontains=query)
    else:
        all_products = Product.objects.all()
    return render(request, 'app/products.html', {'products': all_products, 'query': query})


def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')  
    products = Product.objects.all()
    return render(request, 'app/admin_dashboard.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'app/add_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('admin_dashboard')
    return render(request, 'app/edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    return render(request, 'app/delete_product.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'app/product_detail.html', {'product': product})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('products')
        else:
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'app/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')

