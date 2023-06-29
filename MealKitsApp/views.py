import datetime

from django.shortcuts import render, redirect
from .models import ShippingAddress, Menu, Cart, CartItem, RecipeMenu, Recipe
from django.http import JsonResponse
import json
# from .forms import PaymentForm, ShippingAddressForm, RecipeForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    qs = Menu.objects.all()
    context = {"menus": qs, }
    return render(request, "HomePage.html", context)


def cart(request):
    if request.user.is_authenticated:
        owner = request.user.buyer
        order, created = Cart.objects.get_or_create(owner=owner, complete=False)
        items = order.cartitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, "cart/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.buyer
        order, created = Cart.objects.get_or_create(owner=customer, complete=False)
        items = order.cartitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    # if request.method == "POST":
    #     form_data = ShippingAddressForm(data=request.POST)
    #     if form_data.is_valid():
    #         shipping = form_data.save(commit=False)
    #         shipping = request.user
    #         #shipping.order = order
    #         shipping.save()
    #     form_data_payment = PaymentForm(data=request.POST)
    #     if form_data_payment.is_valid():
    #         payment = form_data_payment.save(commit=False)
    #         payment.customer.user = request.user
    #         payment.save()
    #         return redirect("cart/checkout")

    context = {'items': items, 'order': order}
    return render(request, "cart/checkout.html", context)


def menu(request):
    menuId = request.session['menuId']
    qs = RecipeMenu.objects.filter(menu_id=menuId).all()
    context = {"recipes": qs, }
    return render(request, "Menu.html", context)


def go_to_detailed_view_menu(request):
    data = json.loads(request.body)
    menuId = data['menuId']
    request.session['menuId'] = menuId
    return JsonResponse("Got to detail page", safe=False)


def detailedView(request):
    productId = request.session['productId']
    product = Recipe.objects.get(id=productId)
    # sizes = ProductSizes.objects.filter(product = product).all()
    context = {'product': product}
    return render(request, 'detailedView.html', context)


def go_to_detailed_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    request.session['productId'] = productId
    return JsonResponse("Got to detail page", safe=False)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    request.session['productId'] = productId
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.buyer
    product = Recipe.objects.get(id=productId)
    order, created = Cart.objects.get_or_create(owner=customer, complete=False)

    orderItem, created = CartItem.objects.get_or_create(cart=order, recipe=product)

    if action == 'add':
        print('Added')
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        print('Removed')
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


# @csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.buyer
        order, created = Cart.objects.get_or_create(owner=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            country=data['shipping']['country'],
            zipcode=data['shipping']['zipcode'],
            shipping_time_start=data['shipping']['shipping_time_start'],
            shipping_time_end=data['shipping']['shipping_time_end'],

        )

    return JsonResponse('Payment submitted..', safe=False)


# def insertRecipe(request):
#     if request.user ==
#     if request.method == "POST":
#         form_data = RecipeForm(data=request.POST, files=request.FILES)
#         if form_data.is_valid():
#             recipe = form_data.save(commit=False)
#             recipe.pic = form_data.cleaned_data['pic']
#             recipe.save()
#             return redirect("InsertRecipe")
#     context = {"form": RecipeForm}
#     return render(request, "InsertRecipe.html", context)

