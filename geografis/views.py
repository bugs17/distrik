from django.shortcuts import render
from .models import Geografis

def index(request):

    geografis = Geografis.objects.all()
    subtitle = 'Geografis distrik ninati'
    peta = f'<iframe class="position-relative w-100 h-100" style="min-height: 450px; border: 0" allowfullscreen="" aria-hidden="false" tabindex="0" src="https://maps.google.com/maps?q=ninati&t=&z=11&ie=UTF8&iwloc=&output=embed" frameborder="0"></iframe>'

    context = {
        'title' : 'Geografis',
        'subtitle': subtitle,
        'geografis': geografis,
        'peta' : peta,
        
    }
    return render(request, 'geografis/index.html', context)
