from django.db import models
from django.utils.text import slugify



class Galery(models.Model):
    deskripsi = models.CharField(max_length=100)
    file = models.ImageField(blank=True, null=True, upload_to="image/")
    slug = models.SlugField(blank=True,editable=False)

    def save(self):
        self.slug = slugify(self.deskripsi)
        super(Galery, self).save()

    def __str__(self):
        return f"{self.id} - {self.deskripsi}"
