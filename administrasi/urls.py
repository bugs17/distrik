from django.urls import path
from . import views

app_name = 'administrasi'
urlpatterns = [
    path('',views.index, name='index'),
    path('<str:slug>/',views.detail_administrasi, name='detail'),
]