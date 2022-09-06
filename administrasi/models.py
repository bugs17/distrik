from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Administrasi(models.Model):
    
    nama_layanan = models.CharField(max_length=100)
    persyaratan = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True,editable=False)

    def save(self):
        self.slug = slugify(self.nama_layanan)
        super(Administrasi, self).save()


    def __str__(self):
        return f"{self.nama_layanan}"