
from django.db import models


class Pemerintah(models.Model):
    opsi = (
        ('Camat', 'CAMAT'),
        ('Sekretaris', 'SEKRETARIS')

    )
    nama = models.CharField(max_length=100)
    golongan = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    struktur_organisasi = models.CharField(max_length=30, choices=opsi, null=True)
    nip = models.CharField(max_length=20,null=True)
    foto = models.ImageField(blank=True, null=True, upload_to="image/")

    def __str__(self):
        return f"{self.nama}"


class Organisasi(models.Model):
    judul = models.CharField(max_length=100)
    gambar = models.ImageField(blank=True, null=True, upload_to="image/")

    def __str__(self):
        return f"{self.judul}"
