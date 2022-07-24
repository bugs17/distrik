from django.urls import path
from . import views

app_name = 'sejarah'
urlpatterns = [
    path('',views.index, name='index'),
]