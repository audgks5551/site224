from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from products.models import Product, ProductReal
from questions.models import Question
from elasticsearch7 import Elasticsearch
from django.db.models import Case, When

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
    keyword_list = elasticsearch.sql.query(body={
        "query": f"""
        SELECT id, name, price
        FROM article
        WHERE MATCH(name, '{search_keyword}')
        ORDER BY score() DESC
        """,
        "fetch_size": 10
    })
    print(keyword_list)
    print(keyword_list['rows'])
    print("======================================")
    cursor = keyword_list['cursor']
    paging = elasticsearch.sql.query(body={
        "cursor": f"{cursor}"
    })
    print(paging['rows'])
    print(cursor == paging['cursor'])

    GHList = []
    # for hit in keyword_list['rows']['rows']:
    #        GHList.append(hit['_source']['name'])

    # for item in GHList:
    #    print(item)
    if search_keyword != "":
        # res = elasticsearch.query(
        #    f"""
        #    SELECT score(), name
        #    FROM "article"
        #    WHERE MATCH(name, '{search_keyword}')
        #    ORDER BY score() DESC
        #    """
        # )
        pass
    context = {}
    return render(request, 'example.html', context)


def exampleElasticsearchv(request):
    search_keyword = request.GET.get("search" "")
    elasticsearch = Elasticsearch("http://es01:9200")
    keyword_list = elasticsearch.sql.query(body={
        "query": f"""
        SELECT id
        FROM question4
        WHERE MATCH(name, '{search_keyword}')
        ORDER BY score() DESC
        """,
        "fetch_size": 2
    })

    list_list = []
    for row in keyword_list['rows']:
        list_list.append(row[0])
    print(list_list)
    print("======================================")
    cursor = keyword_list['cursor']
    paging = elasticsearch.sql.query(body={
        "cursor": f"{cursor}"
    })
    print(paging['rows'])

    order = Case(*[When(id=id, then=pos) for pos, id in enumerate(list_list)])
    queryset = Product.objects.filter(id__in=list_list).order_by(order)
    for article in queryset:
        print(article.id)
    context = {}
    return render(request, 'example.html', context)
