from django.contrib import admin
from .models import postmodel

# Register your models here.

class detialseen(admin.ModelAdmin):
    list_display = ('title','datecreated')
admin.site.register(postmodel)
