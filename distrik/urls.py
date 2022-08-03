
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('secret/', admin.site.urls),
    path('', views.index, name='index'),
    path('panel/',include(('panel.urls'), namespace='panel')),
    path('panel/',include('django.contrib.auth.urls')),
    path('sejarah/',include(('sejarah.urls'), namespace='sejarah')),
    path('geografis/',include(('geografis.urls'), namespace='geografis')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
