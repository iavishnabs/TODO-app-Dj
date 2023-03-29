from django.contrib import admin
from . models import taskList
# Register your models here.

class tList(admin.ModelAdmin):
    l = ['name','desc','date']


admin.site.register(taskList,tList)