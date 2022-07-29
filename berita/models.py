from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Berita(models.Model):
    judul = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    gambar = models.ImageField(blank=True, null=True, upload_to="image/")
    slug = models.SlugField(blank=True,editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Berita, self).save()

    def __str__(self):
        return f"{self.id} - {self.judul}"


