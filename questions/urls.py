from django.urls.conf import path, include
from . import views

app_name = "questions"

urlpatterns = [
    path('', views.showQuestion, name="show"),
    path('create/', views.createQuestion, name="create"),
    path('<int:question_count>/modify', views.modifyQuestion, name="modify"),
]
