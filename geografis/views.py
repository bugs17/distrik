from django.shortcuts import render

def index(request):

    subtitle = 'Geografis distrik ninati'

    context = {
        'title' : 'Geografis',
        'subtitle': subtitle,
        
    }
    return render(request, 'geografis/index.html', context)
