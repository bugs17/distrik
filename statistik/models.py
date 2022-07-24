
from django.db import models

# Create your models here.



class KampungData(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


jenisKelamin = [
    ('L', 'laki-laki'),
    ('P', 'perempuan'),
]

class Populasi(models.Model):
#   'L' 'laki-laki', 'P' 'Perempuan'
    jenisKelamin = models.CharField(max_length=1, choices=jenisKelamin, default='L')
    jumlah = models.IntegerField()
    kampung_id = models.ForeignKey(KampungData, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.jenisKelamin}-{self.jumlah}-{self.kampung_id}'

class KepalaKeluarga(models.Model):
    kampung_id = models.ForeignKey(KampungData, on_delete=models.CASCADE, null=True)
    jumlahKK = models.IntegerField()

    def __str__(self):
        return f'{self.kampung_id}-{self.jumlahKK}'

