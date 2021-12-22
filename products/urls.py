from django.urls.conf import include, path
from . import views

app_name = "products"

urlpatterns = [
    path('<int:product_id>/', include([
        path('', views.getProductDetail, name="detail"),
        path('question/', include('questions.urls')),
    ])),
    path('list/', views.getProductList, name="list"),
]
