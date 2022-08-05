from django.urls import path
from . import views



app_name = 'panel'
urlpatterns = [
    
    path('loginpanel/',views.login_panel, name='login'),
    path('logoutpanel/',views.logout_panel, name='logout'),
    path('register/',views.register, name='register'),
    path('user/',views.user_page, name='user'),


    # ------------------------------ #
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
    path('berita/',views.berita, name='berita'),
    path('addberita/',views.add_berita, name='addberita'),
    path('updateberita/<str:pk>',views.update_berita, name='updateberita'),
    path('hapusberita/<str:pk>',views.hapus_berita, name='hapusberita'),
    path('data/',views.data, name='data'),
    path('adddata/',views.add_data, name='adddata'),
    path('updatedata/<str:pk>',views.update_data, name='updatedata'),
    path('hapusdata/<str:pk>',views.hapus_data, name='hapusdata'),
    path('galery/',views.galery, name='galery'),
    path('addgalery/',views.add_galery, name='addgalery'),
    path('updategalery/<str:pk>',views.update_galery, name='updategalery'),
    path('hapusgalery/<str:pk>',views.hapus_galery, name='hapusgalery'),
    
]
