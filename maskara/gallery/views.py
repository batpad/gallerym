# Create your views here.
from models import *
from django.shortcuts import render, get_object_or_404
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

def home(request):
    main_item = FrontPageItem.objects.all()[0]
    fp_items = FrontPageItem.objects.all()[1:4]
    publications = Publication.objects.all()[0:12]
    context = {
        'main_item': main_item.get_data(),
        'main_item_type': main_item.get_type(),
        'items': [item.get_data() for item in fp_items],
        'publications': [p.get_frontpage_dict() for p in publications]
    }
    return render(request, "index.html", context)


def artists(request, represented=False):
    qset = Artist.objects.published()
    if represented:
        qset = qset.filter(is_represented=True)
    artists = [a.get_list_dict() for a in qset]
    return render(request, 'artists.html', {'artists': artists})

'''
def represented_artists(request):
    artists = [a.get_list_dict() for a in Artist.objects.published().filter(is_represented=True)]
    return render(request, 'artists.html', {'artists': artists})
'''

def artist(request, slug, view=''):
    artist = get_object_or_404(Artist, slug=slug)
    context = {
        'artist': artist,
        'url': artist.get_absolute_url()
    }
    works = None

    if view == '':
        if artist.has_selected():
            view = 'selected'
        elif artist.has_available():
            view = 'available'
        else:
            view = 'biography'
        return HttpResponseRedirect(artist.get_absolute_url() + "/" + view)

    if view == 'selected':
        template = "artist-works.html"
        context['works'] = ArtistWork.objects.filter(artist=artist).filter(is_selected=True)

    elif view == 'available':
        template = 'artist-works.html'
        context['works'] = ArtistWork.objects.filter(artist=artist).filter(is_available=True)    

    elif view == 'exhibitions':
        template = 'artist-exhibitions.html'
        context['exhibitions'] = Exhibition.objects.filter(featured_artists=artist)

    elif view == 'biography':
        template = 'artist-biography.html'

    elif view == 'cv':
        template = 'artist-cv.html'
        context['education'] = ArtistEducation.get_by_year(artist)
        context['solo_exhibs'] = ArtistSoloExhib.get_by_year(artist)
        context['group_exhibs'] = ArtistGroupExhib.get_by_year(artist)
        context['collections'] = ArtistCollection.get_by_year(artist)
        context['awards'] = ArtistAward.get_by_year(artist)
   
    elif view == 'press':
        template = 'artist-press.html'
        context['years'] = ArtistPress.get_by_year(artist) 
   
    elif view == 'publications':
        template = 'artist-publications.html'
        context['publications'] = artist.publication_set.all()
 
    else:
        return HttpResponseRedirect(context['url'])    

    if context.has_key('works'):
        page_no = int(request.GET.get('page', 1))
        paginator = Paginator(context['works'], 16)
        context['paginator'] = paginator
        context['page'] = paginator.page(page_no)   

    return render(request, template, context)

def artist_work_image(request, id):
    i = ArtistWorkImage.objects.get(pk=id)
    return render(request, 'test_leaflet.html', {'image': i})


def exhibitions(request, when='upcoming'):
    now = datetime.datetime.now()
    qset = Exhibition.objects.filter(autopublish_date__lte=now)
    if when == 'upcoming':
        qset = qset.filter(start_date__gte=now).order_by('start_date')
    else:
        qset = qset.filter(start_date__lt=now).order_by('-start_date')
    return render(request, 'exhibitions.html', {'exhibitions': qset})

def current_exhibition(request):
    exhib = Exhibition.get_current()
    return HttpResponseRedirect(exhib.get_absolute_url())

def exhibition(request, slug, view=''):
    exhibition = get_object_or_404(Exhibition, slug=slug)
    context = {
        'exhibition': exhibition,
        'url': exhibition.get_absolute_url()
    }

    if view == 'overview':
        template = 'exhibitions-overview.html'

    elif view == 'works':
        template = 'exhibitions-works.html'
        context['works'] = exhibition.featured_work.all()

    elif view == 'artists':
        template = 'exhibitions-artists.html'
        context['artists'] = exhibition.featured_artists.all()

    elif view == 'press':
        template = 'exhibitions-press.html'

    elif view == 'publications':
        template = 'exhibitions-publications.html'
        context['publications'] = exhibition.publication_set.all()

    elif view == 'videos':
        template = 'exhibitions-videos.html'

    else:
        return HttpResponseRedirect(context['url'] + "/overview")        

    return render(request, template, context)

def events(request, when='upcoming'):
    now = datetime.datetime.now()
    qset = Event.objects.filter(published=True)
    if when == 'upcoming':
        qset = qset.filter(date__gte=now).order_by('date')
    else:
        qset = qset.filter(date__lt=now).order_by('-date')
    return render(request, 'events.html', {'events': qset})

def current_event(request):
    event = Event.get_current()
    return HttpResponseRedirect(event.get_absolute_url())

def event(request, slug, view=''):
    event = get_object_or_404(Event, slug=slug)
    context = {
        'event': event,
        'url': event.get_absolute_url()
    }

    if view == 'overview':
        template = 'event-overview.html'

    elif view == 'works':
        template = 'event-works.html'
        context['works'] = event.featured_work.all()

    elif view == 'publications':
        template = 'event-publications.html'
        context['publications'] = event.publication_set.all()

    else:
        return HttpResponseRedirect(context['url'] + "/overview")        

    return render(request, template, context)


'''
def previous_exhibitions(request):
    now = datetime.datetime.now()
    exhibitions = Exhibition.objects.all().filter(start_date__lt=now).order_by('-start_date')
    return render(request, 'exhibitions.html', {'exhibitions': exhibitions})
'''


