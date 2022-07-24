from django.shortcuts import render
from .models import Sejarah

def index(request):

    subtitle = 'Sejarah Distrik Ninati'
    sejarah = Sejarah.objects.all()
    

    context= {
        'title' : 'Sejarah',
        'subtitle': subtitle,
        'sejarah': sejarah,

    }
    return render(request, 'sejarah/index.html', context)
