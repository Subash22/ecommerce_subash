from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Brand, Category, CartItem
from datetime import datetime


def index(request):
    if request.method == "GET":
        category_id = request.GET.get("category")
        brand_id = request.GET.get("brand")
        if category_id:
            filter_query = Q(category__id=category_id)
            products = Product.objects.filter(filter_query)
        elif brand_id:
            filter_query = Q(brand__id=brand_id)
            products = Product.objects.filter(filter_query)
        else:
            products = Product.objects.all()

        categories = Category.objects.all()
        brands = Brand.objects.all()
        cart_items = CartItem.objects.filter(user=request.user)
        context = {
            'products': products,
            'categories': categories,
            'brands': brands,
            'search_query': '',
            'cart_items': cart_items
        }
        return render(request, 'index.html', context)

    elif request.method == "POST":
        q = request.POST.get("query")
        if "-" in q:
            price_values = q.split("-")
            filter_query = Q(price__gte=price_values[0]) & Q(price__lte=price_values[1])
        else:
            filter_query = Q(name__icontains=q) | Q(price__icontains=q) | Q(brand__name__icontains=q)

        products = Product.objects.filter(filter_query)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        cart_items = CartItem.objects.filter(user=request.user)
        context = {
            'products': products,
            'categories': categories,
            'brands': brands,
            'search_query': q,
            'cart_items': cart_items
        }
        return render(request, 'index.html', context)


@login_required(login_url="/admin/login")
def cart(request):
    # get request data
    product_id = request.GET.get("id")
    quantity = request.GET.get("qty")
    if product_id:
        # retrieve product data
        product = Product.objects.get(id=product_id)
        try:
            # get cart item and increase quantity
            cart_item = CartItem.objects.get(user=request.user,
                                             product=product)
            cart_item.quantity += int(quantity)
            cart_item.entered_on = datetime.now()

        except CartItem.DoesNotExist:
            # initialize cart item
            cart_item = CartItem(
                user=request.user,
                product=product,
                quantity=int(quantity),
                entered_on=datetime.now(),
            )
        # save to database
        cart_item.save()
    cart_items = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    # return view
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, "cart.html", context)


def removecart(request, id):
    try:
        # get cart item and increase quantity
        product = Product.objects.get(id=id)
        cart_item = CartItem.objects.get(user=request.user,
                                         product=product)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    # redirect to cart
    return redirect(cart)


def success_page(request):
    message = request.session["message"]
    return render(request, "success.html", {"message": message})


def error_page(request):
    message = request.session["message"]
    return render(request, "error.html", {"message": message})
