from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name="logout"),
    path('find/', views.getID, name="find"),
]
