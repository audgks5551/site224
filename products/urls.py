from django.urls.conf import path
from . import views

app_name = "products"

urlpatterns = [
    path('list/', views.getProductList, name="list"),
    path('<int:product_id>/', views.getProductDetail, name="detail"),
]
