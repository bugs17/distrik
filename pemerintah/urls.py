from django.urls import path
from . import views

app_name = 'pemerintah'
urlpatterns = [
    path('',views.index, name='index'),
    path('organisasi/',views.organisasi, name='organisasi'),
]