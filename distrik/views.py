from django.shortcuts import render

from django.db.models import Sum

from berita.models import Berita
from pemerintah.models import Pemerintah
from administrasi.models import Administrasi
from statistik.models import DataPerKampung

def index(request):
    berita = Berita.objects.all().order_by('-update')[:6]
    pemerintah = Pemerintah.objects.all().order_by('-id')
    administrasi = Administrasi.objects.all().order_by('-id')
    datastatistik = DataPerKampung.objects.all()

    # kk = KepalaKeluarga.objects.all()
    # semuaKampung= Populasi.objects.filter(jenisKelamin='P')

    # kalkulasi jumlah jiwa berdasarkan kampung laki-laki + perempuan
    # ninati = Populasi.objects.filter(kampung_id__nama='ninati').aggregate(Sum('jumlah'))
    # abonggo = Populasi.objects.filter(kampung_id__nama='abonggo').aggregate(Sum('jumlah'))
    # harapan = Populasi.objects.filter(kampung_id__nama='harapan').aggregate(Sum('jumlah'))
    # mindip = Populasi.objects.filter(kampung_id__nama='mindip').aggregate(Sum('jumlah'))


    # jumlahJiwa = [ninati, abonggo, harapan, mindip]
    



    context = {
        'title': 'Beranda',
        'berita': berita,
        'pemerintah': pemerintah,
        'administrasi': administrasi,
        'data': datastatistik,


    }
    return render(request, 'index.html', context)


