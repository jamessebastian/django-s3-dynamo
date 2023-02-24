from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('testboto_createtable', views.testboto_createtable, name='testboto_createtable'),
]