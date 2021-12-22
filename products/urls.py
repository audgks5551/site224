from django.urls.conf import path
from . import views

urlpatterns = [
    path('list/', views.index, name="index"),
]
