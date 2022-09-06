from django.contrib import admin
from .models import Administrasi


class AdministrasiAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]

admin.site.register(Administrasi,AdministrasiAdmin)
