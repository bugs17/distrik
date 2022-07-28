from django.urls import path
from . import views



app_name = 'panel'
urlpatterns = [
    path('',views.index, name='index'),
    path('sejarahdistrik/',views.sejarah, name='getsejarah'),
    path('updatesejarah/<str:pk>',views.update_sejarah, name='updatesejarah'),
    path('geografisdistrik/',views.geografis, name='getgeografis'),
    path('updategeografis/<str:pk>',views.update_geografis, name='updategeografis'),
    path('pemerintahdistrik/',views.pemerintah, name='pemerintah'),
    path('addpemerintah/',views.add_pemerintah, name='addpemerintah'),
    path('updatepemerintah/<str:pk>',views.update_pemerintah, name='updatepemerintah'),
    path('hapuspemerintah/<str:pk>',views.hapus_pemerintah, name='hapuspemerintah'),
    path('organisasi/',views.organisasi, name='organisasi'),
    path('updateorganisasi/<str:pk>',views.update_organisasi, name='updateorganisasi'),
    path('administrasi/',views.administrasi, name='administrasi'),
    path('addadministrasi/',views.add_administrasi, name='addadministrasi'),
    path('updateadministrasi/<str:pk>',views.update_administrasi, name='updateadministrasi'),
    path('hapusdministrasi/<str:pk>',views.hapus_administrasi, name='hapusadministrasi'),
]
