# Create your views here.
from models import *
from django.shortcuts import render

def artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})

def artist_work_image(request, id):
    i = ArtistWorkImage.objects.get(pk=id)
    return render(request, 'test_leaflet.html', {'image': i})
