from django.urls.conf import path, include
from . import views

app_name = "questions"

urlpatterns = [
    path('create/', views.createQuestion, name="create"),
]
