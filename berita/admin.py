from django.contrib import admin
from .models import Berita



class BeritaAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'publish', 'update']

admin.site.register(Berita,BeritaAdmin)
