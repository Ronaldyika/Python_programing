from django.contrib import admin
from .models import Detailinfo

# Register your models here.
class Postadmin(admin.ModelAdmin):
    class Meta:
        model = Detailinfo
        list_display = ('name','school','department','subjects')
admin.site.register(Detailinfo,Postadmin)