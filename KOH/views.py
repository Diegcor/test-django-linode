from django.shortcuts import render
from utilities import get_king

def home_page(request):
    return render(
        request,
        'KOH/home_page.html',
        {
            'king': get_king(),
        }
    )