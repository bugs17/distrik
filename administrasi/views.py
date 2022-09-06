from django.shortcuts import render
from .models import Administrasi

def index(request):

    subtitle = 'Layanan Administrasi Distrik Ninati'
    administrasi = Administrasi.objects.all()
    

    context= {
        'title' : 'Administrasi',
        'subtitle': subtitle,
        'administrasi': administrasi,

    }
    return render(request, 'administrasi/index.html', context)

def detail_administrasi(request, slug):
    administrasi = Administrasi.objects.filter(slug=slug)
    subtitle = administrasi.get(slug=slug)
    context = {
        'title' : 'Administrasi',
        'administrasi': administrasi,
        'subtitle': subtitle

    }
    return render(request, 'administrasi/detail_administrasi.html', context)