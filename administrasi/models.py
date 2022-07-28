from django.db import models
from ckeditor.fields import RichTextField


class Administrasi(models.Model):
    
    nama_layanan = models.CharField(max_length=100)
    persyaratan = RichTextField(blank=True, null=True)


    def __str__(self):
        return f"{self.nama_layanan}"