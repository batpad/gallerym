from models import *
from django.shortcuts import render, get_object_or_404
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.contrib.contenttypes.models import ContentType
import json
from haystack.query import SearchQuerySet

def home(request):
    main_item = FrontPageItem.objects.all()[0]
    fp_items = FrontPageItem.objects.all()[1:4]
    publications = Publication.objects.all()[0:12]
    context = {
        'main_item': main_item.get_data(),
        'main_item_type': main_item.get_type(),
        'items': [item.get_data() for item in fp_items],
        'publications': [p.get_frontpage_dict() for p in publications],
        'title': 'Home'
    }
    return render(request, "index.html", context)

def search(request):
    q = request.GET.get("q", "")
    search_model = request.GET.get("in", None)
    if search_model:
        is_single_model = True
        try:
            model_class = ContentType.objects.get_by_natural_key('gallery', search_model)
        except:
            raise Http404("Tried to search for a type that does not exist, mis-typed in= parameter")
        search_models = [model_class]
    else:
        is_single_model = False
        search_models = [Artist, Event, Exhibition, ArtistWork, Publication]
    context = {}
    for model in search_models:
        model_name = model._meta.module_name
        qset = SearchQuerySet().filter(content=q).models(*[model])
        page_count = 40 if is_single_model else 5
        context[model_name] = Paginator(qset, page_count)
    return render(request, "search/search.html", context)

def artists(request, represented=False):
    qset = Artist.objects.published()
    if represented:
        qset = qset.filter(is_represented=True)
    artists = [a.get_list_dict() for a in qset]
    context = {
        'artists': artists,
        'menu': 'artists',
        'title': 'All Artists' if not represented else 'Represented Artists'
    }
    return render(request, 'artists.html', context)

'''
def represented_artists(request):
    artists = [a.get_list_dict() for a in Artist.objects.published().filter(is_represented=True)]
    return render(request, 'artists.html', {'artists': artists})
'''

def artist(request, slug, view=''):
    artist = get_object_or_404(Artist, slug=slug)
    context = {
        'artist': artist,
        'url': artist.get_absolute_url(),
        'menu': 'artists',
        'title': 'Artist: %s' % artist.name
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

    elif view == 'events':
        template = 'artist-events.html'
        context['events'] = artist.event_set.all()

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
        context['press'] = artist.get_press() 
   
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

def zoom(request, id):
    work = get_object_or_404(ArtistWork, pk=id)
    d = work.get_zoom_dict()
    context = {
        'zoomables': d,
        'title': work.title,
        'zoomables_json': json.dumps(d)
    }
    return render(request, "zoom.html", context)


def work(request, object_type, slug, work_id):
    context = {}
    object_types = {
        'artist': Artist,
        'exhibition': Exhibition,
        'event': Event
    }
    if object_type not in object_types:
        raise Http404()
    kls = object_types[object_type]
    obj = kls.objects.get(slug=slug)
    context[object_type] = obj
    context['kls'] = kls
    context['url'] = obj.get_absolute_url()
    work = ArtistWork.objects.get(pk=work_id)
    context['work'] = work
    context['has_slides'] = work.artistworkimage_set.all().count() > 1
    base_name = 'artist' if object_type == 'artist' else object_type + 's'
    context['base_template'] = base_name + 'base.html'        
    context['menu'] = object_type + 's'
    if object_type == 'artist':
        context['obj_title'] = obj.name

    works_qset = obj.get_works()
    try:
        context['works_count'] = works_qset.count()
    except:
        context['works_count'] = len(works_qset)
    for i, o in enumerate(works_qset):
        if o.id == work.id:
            work_index = i + 1
    if not work_index:
        raise Http404("this should never happen")
    context['work_index'] = work_index
    base_url = obj.get_absolute_url()
    if work_index > 1:
        previous_work = works_qset[work_index - 2]
        context['previous_work'] = base_url + "/works/" + str(previous_work.id)
    if work_index < context['works_count']:
        next_work = works_qset[work_index]   
        context['next_work'] = base_url + "/works/" + str(next_work.id)
    return render(request, "work.html", context)  




def exhibitions(request, when='upcoming'):
    now = datetime.datetime.now()
    qset = Exhibition.objects.filter(autopublish_date__lte=now)
    if when == 'upcoming':
        if not Exhibition.has_upcoming():
            return HttpResponseRedirect("/exhibitions/previous")
        qset = qset.filter(start_date__gte=now).order_by('start_date')
    else:
        qset = qset.filter(start_date__lt=now).order_by('-start_date')
    context = {
        'exhibitions': qset,
        'kls': Exhibition,
        'menu': 'exhibitions',
        'title': '%s Exhibitions' % when.title()
    }
    return render(request, 'exhibitions.html', context)

def current_exhibition(request):
    exhib = Exhibition.get_current()
    if exhib:
        return HttpResponseRedirect(exhib.get_absolute_url())
    elif Exhibition.has_upcoming():
        return HttpResponseRedirect("/exhibitions/upcoming")
    else:
        return HttpResponseRedirect("/exhibitions/previous")

def exhibition(request, slug, view=''):
    exhibition = get_object_or_404(Exhibition, slug=slug)
    context = {
        'exhibition': exhibition,
        'url': exhibition.get_absolute_url(),
        'menu': 'exhibitions',
        'kls': Exhibition,
        'title': 'Exhibition: %s' % exhibition.title
    }

    if view == 'overview':
        template = 'exhibitions-overview.html'

    elif view == 'works':
        template = 'exhibitions-works.html'
        context['works'] = exhibition.get_works()

    elif view == 'artists':
        template = 'exhibitions-artists.html'
        context['artists'] = exhibition.featured_artists.all()

    elif view == 'press':
        context['press'] = exhibition.get_press()
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
    if when == 'current':
        qset = qset.filter(date__lte=now).filter(end_date__gte=now).order_by('date')
    if when == 'upcoming':
        if not Event.has_upcoming():
            return HttpResponseRedirect("/events/previous")
        qset = qset.filter(date__gte=now).order_by('date')
    elif when == 'previous':
        qset = qset.filter(date__lt=now).exclude(end_date__gte=now).order_by('-date')
    context = {
        'events': qset,
        'menu': 'events',
        'kls': Event,
        'title': '%s Events' % when.title()
    }
    return render(request, 'events.html', context)

def credits(request):
    return render(request, 'credits.html')

def terms(request):
    return render(request, 'terms-and-conditions.html')

def privacy(request):
    return render(request, 'privacy-policy.html')

def search_static(request):
    return render(request, 'search_static.html')

def current_event(request):
    events = Event.get_current()
    if not events:
        if Event.has_upcoming():
            return HttpResponseRedirect("/events/upcoming")
        else:
            return HttpResponseRedirect("/events/previous")
    else:
        if events.count() == 1:
            return HttpResponseRedirect(events[0].get_absolute_url())
        else:
            return events(request, when='current') 

def event(request, slug, view=''):
    event = get_object_or_404(Event, slug=slug)
    context = {
        'event': event,
        'url': event.get_absolute_url(),
        'menu': 'events',
        'kls': Event,
        'title': 'Event: %s' % event.title
    }

    if view == 'overview':
        template = 'event-overview.html'

    elif view == 'works':
        template = 'event-works.html'
        context['works'] = event.get_works()

    elif view == 'artists':
        template = 'event-artists.html'
        context['artists'] = event.featured_artists.all()

    elif view == 'publications':
        template = 'event-publications.html'
        context['publications'] = event.publication_set.all()

    elif view == 'press':
        template = 'event-press.html'
        context['press'] = event.get_press()

    else:
        return HttpResponseRedirect(context['url'] + "/overview")        

    return render(request, template, context)


'''
def previous_exhibitions(request):
    now = datetime.datetime.now()
    exhibitions = Exhibition.objects.all().filter(start_date__lt=now).order_by('-start_date')
    return render(request, 'exhibitions.html', {'exhibitions': exhibitions})
'''



