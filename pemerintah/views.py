from django.shortcuts import render

from .models import Pemerintah, Organisasi



# get pemerintah
def index(request):
    pemerintah = Pemerintah.objects.all().order_by('-id')

    context = {
        'title' : 'Pemerintah',
        'subtitle' : 'Pemerintah Distrik Ninati',
        'pemerintah': pemerintah,
    }
    return render(request, 'pemerintah/index.html', context)


# get organisasi
def organisasi(request):

    organisasi = Organisasi.objects.all()

    context = {
        'title' : 'Organisasi',
        'subtitle' : 'Struktur Organisasi Distrik Ninati',
        'organisasi': organisasi,
    }
    return render(request, 'pemerintah/organisasi.html', context)