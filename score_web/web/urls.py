from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('db/<int:num>', views.db, name='db'),
        path('edit/', views.edit, name='edit'),
        path('dbdel/', views.dbdel, name='dbdel'),
    ]