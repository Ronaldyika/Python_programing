from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name="signup"),
    path('signin',views.signin,name="signin"),
    path('home',views.home,name="home")
]