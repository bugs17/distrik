
from django.db import models


class Pemerintah(models.Model):
    nama = models.CharField(max_length=100)
    golongan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(blank=True, null=True, upload_to="image/")

    def __str__(self):
        return f"{self.nama} - {self.golongan} - {self.jabatan}"
