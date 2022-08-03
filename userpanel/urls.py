from django.urls import path

from . import views


app_name = 'userpanel'
urlpatterns = [
    path('',views.login_panel, name='index'),
    
]