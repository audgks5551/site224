from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from products.models import Product, ProductReal
from questions.models import Question

# 제품 리스트 보기


def getProductList(request):

    product_list = Product.objects.order_by('-update_date')
    context = {'product_list': product_list}

    return render(request, 'product_list.html', context)

# 제품 상세보기


def getProductDetail(request, product_id):

    product = Product.objects.get(id=product_id)
    product_reals = ProductReal.objects.filter(product=product)
    question_list = Question.objects.filter(object_id=product_id)
    context = {'product': product, 'question_list': question_list,
               'product_reals': product_reals}

    return render(request, 'product_detail.html', context)
