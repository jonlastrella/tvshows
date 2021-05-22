from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.


def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)


def singleShow(request, showId):
    context = {
        'show': Show.objects.get(id=showId)
    }
    return render(request, 'singleShow.html', context)


def editShow(request, showId):
    context = {
        'show': Show.objects.get(id=showId)
    }
    return render(request, 'editShow.html', context)


def updateShow(request, showId):
    update = Show.objects.get(id=showId)
    update.title = request.POST['title']
    update.network = request.POST['network']
    update.release_date = request.POST['release_date']
    update.save()
    return redirect('/shows')


def create(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
    )
    return redirect('/shows')


def newShow(request):
    return render(request, 'newShow.html')


def deleteShow(request, showId):
    delete = Show.objects.get(id=showId)
    delete.delete()
    return redirect('/shows')
