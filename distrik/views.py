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


    context = {
        'title': 'Beranda',
        'berita': berita,
        'pemerintah': pemerintah,
        'administrasi': administrasi,
        'data': datastatistik,


    }
    return render(request, 'index.html', context)


