from django.shortcuts import render
from statistik.models import DataPerKampung

def index(request):
    datastatistik = DataPerKampung.objects.all()

    context = {
        'title': 'Statistik',
        'subtitle': 'Data statistik distrik ninati',
        'data': datastatistik,

    }

    return render(request, 'statistik/index.html', context)