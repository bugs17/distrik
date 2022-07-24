from django.db import models
from ckeditor.fields import RichTextField


class Geografis(models.Model):
    judul = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.judul}"

