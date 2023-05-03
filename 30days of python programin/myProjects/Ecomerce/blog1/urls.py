from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fashion',views.fashion, name='fashion'),
    path('electronic',views.electronic,name="electronic"),
    path('jewellery',views.jewellery,name="jewellery")
]