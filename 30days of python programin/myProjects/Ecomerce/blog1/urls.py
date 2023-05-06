from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fashion',views.fashion, name='fashion'),
    path('electronic',views.electronic,name="electronic"),
    path('jewellery',views.jewellery,name="jewellery")
]
if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)