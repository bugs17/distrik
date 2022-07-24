from django.shortcuts import render
from statistik.models import KampungData, KepalaKeluarga, Populasi
from django.db.models import Sum

def index(request):


    kk = KepalaKeluarga.objects.all()
    semuaKampung= Populasi.objects.filter(jenisKelamin='P')

    # kalkulasi jumlah jiwa berdasarkan kampung laki-laki + perempuan
    ninati = Populasi.objects.filter(kampung_id__nama='ninati').aggregate(Sum('jumlah'))
    abonggo = Populasi.objects.filter(kampung_id__nama='abonggo').aggregate(Sum('jumlah'))
    harapan = Populasi.objects.filter(kampung_id__nama='harapan').aggregate(Sum('jumlah'))
    mindip = Populasi.objects.filter(kampung_id__nama='mindip').aggregate(Sum('jumlah'))


    jumlahJiwa = [ninati, abonggo, harapan, mindip]
    

    context = {
        'title': 'Beranda',
        'kk': kk,
        'all': jumlahJiwa,
        'semuaKampung': semuaKampung,

    }
    return render(request, 'index.html', context)