from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from products.models import Product, ProductReal
from questions.models import Question
from elasticsearch7 import Elasticsearch
from elasticsearch7.client import SqlClient
from pprint import pprint as pp
# 제품 리스트 보기


def getProductList(request):

    search = request.GET.get("search", "")
    if search != "":
        pass

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

def exampleElasticsearch(request):
    search_keyword = request.GET.get("search" "")
    elasticsearch = Elasticsearch("http://es01:9200")
    keyword_list = elasticsearch.sql.query(body={'query': f"""
            SELECT id 
            FROM "article"
            WHERE MATCH(name, '{search_keyword}') 
            ORDER BY score() DESC
            """})
    GHList = []
    #for hit in keyword_list['rows']['rows']:
    #        GHList.append(hit['_source']['name'])
    
    #for item in GHList:
    #    print(item)
    if search_keyword != "":
        #res = elasticsearch.query(
        #    f"""
        #    SELECT score(), name 
        #    FROM "article"
        #    WHERE MATCH(name, '{search_keyword}') 
        #    ORDER BY score() DESC
        #    """
        #)
        pass
    context = {}
    return render(request, 'example.html', context)
