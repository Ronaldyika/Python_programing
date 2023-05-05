from django.urls import path
from . import views


urlpatterns = [
    path('customer',views.customer, name="customer"),
    path('',views.dashbord, name='dashbord'),
    path('products',views.products, name='products'),
]