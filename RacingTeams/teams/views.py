from django.shortcuts import render
from .models import Driver, Race, Result

def home(request):
    drivers = Driver.objects.all()
    races = Race.objects.all()
    results = Result.objects.all()
    context = {
        'drivers': drivers,
        'races': races,
        'results': results,
    }
    return render(request, 'teams/home.html',context)
