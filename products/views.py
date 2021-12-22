from django.shortcuts import render
from products.models import Product


def getProductList(request):

    product_list = Product.objects.order_by('-update_date')
    context = {'product_list': product_list}

    return render(request, 'product_list.html', context)


def getProductDetail(request, product_id):

    product = Product.objects.get(id=product_id)
    context = {'product': product}

    return render(request, 'product_detail.html', context)
