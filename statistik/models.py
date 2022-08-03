
from django.db import models




class DataPerKampung(models.Model):
    nama_kampung = models.CharField(max_length=100, null=True)
    jumlah_jiwa = models.IntegerField()
    kk = models.IntegerField()
    puskesmas = models.IntegerField()
    sekolah = models.IntegerField()


    def __str__(self):
        return f'{self.nama_kampung}'



