
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models.farmers import Farmer
from .models.products import Product
from .models.orders import Order
from .forms import FarmerProfileForm,ProductForm
from django.views import View

def farmer_dashboard(request):
    # Get the category from the URL parameters
    category = request.GET.get('category', None)
    
    # Filter the products by category if provided, otherwise show all products
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'farmer_dashboard.html', context)

def manage_profile(request, farmer_id):
    """
    View to manage (edit/update) a farmer's profile.
    """
    farmer = get_object_or_404(Farmer, id=farmer_id)

    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmer_profile', farmer_id=farmer.id)
    else:
        form = FarmerProfileForm(instance=farmer)

    context = {
        'form': form,
        'farmer': farmer
    }
    return render(request, 'farmers/farmer_profile.html', context)


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user.farmerprofile
            product.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'farmer/add_product.html', {'form': form})

@login_required
def view_products(request):
    products = Product.objects.filter(farmer=request.user.farmerprofile)
    return render(request, 'farmer/view_products.html', {'products': products})

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, farmer=request.user.farmerprofile)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'farmer/update_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, farmer=request.user.farmerprofile)
    if request.method == "POST":
        product.delete()
        return redirect('view_products')
    return render(request, 'farmer/delete_product.html', {'product': product})

@login_required
def view_orders(request):
    orders = Order.objects.filter(product__farmer=request.user.farmerprofile)
    return render(request, 'farmer/view_orders.html', {'orders': orders})


def product_list(request):
    # Get the category from the URL parameter, if provided
    category = request.GET.get('category', None)
    
    # Filter the products based on the category if specified, otherwise show all products
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    # Render the products in the template
    context = {
        'products': products
    }
    
    return render(request, 'products/product_list.html', context)

class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders,})
