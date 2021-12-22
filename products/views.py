from django.shortcuts import render
from products.models import Product


def index(request):
    product_list = Product.objects.order_by('-update_date')
    context = {'product_list': product_list}
    return render(request, 'product_list.html', context)
