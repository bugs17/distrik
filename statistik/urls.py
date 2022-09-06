from django.urls import path
from . import views

app_name = 'statistik'
urlpatterns = [
    path('',views.index, name='index'),

]