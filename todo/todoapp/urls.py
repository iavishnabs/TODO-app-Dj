from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('edit/<int:taskid>',views.edit,name='edit'),
]