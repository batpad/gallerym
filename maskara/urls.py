from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import Sitemap

from filebrowser.sites import site
from maskara.sitemaps import *


# from django.contrib.sitemaps import Sitemap




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
from os.path import join
#sitemaps = {'exhibition': ExhibitionSitemap,'event':EventSitemap,'artist':ArtistSitemap} 

#sitemaps = {'artist': ArtistSitemap, 'event': EventSitemap, 'exhibition': ExhibitionSitemap} 

sitemaps = {'artist': ArtistSitemap, 'event': EventSitemap, 'exhibition': ExhibitionSitemap} 

urlpatterns = patterns('',
    
    # Examples:
    # url(r'^$', 'maskara.views.home', name='home'),
    # url(r'^maskara/', include('maskara.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subscribe$', 'subscribers.views.subscribe', name='subscribe'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),                    
)

urlpatterns += patterns('maskara.gallery.views',
    url(r'^$', 'home', name='home'),
    url(r'^artists$', 'artists', name='artists'),
    url(r'^artists/represented$', 'artists', {'represented': True }, name='represented_artists'),
    url(r'^(?P<object_type>[\w]+)/(?P<slug>[\w\-]+)/works/(?P<work_id>[0-9]*)$', 'work', name='work'),
    url(r'^artist/(?P<slug>[\w\-]+)/(?P<view>[\w\-]*?)$', 'artist', name='artist'),
    url(r'^exhibitions/current$', 'current_exhibition', name='current_exhibition'),
    url(r'^exhibitions/upcoming$', 'exhibitions', {'when': 'upcoming'}, name='upcoming_exhibitions'),
    url(r'^exhibitions/previous$', 'exhibitions', {'when': 'previous'}, name='previous_exhibitions'),
    url(r'^exhibition/(?P<slug>[\w\-]+)/(?P<view>[\w\-]*?)$', 'exhibition', name='exhibition'),
    url(r'^events/current$', 'current_event', name='current_event'),
    url(r'^events/upcoming$', 'events', {'when': 'upcoming'}, name='upcoming_events'),
    url(r'^events/previous$', 'events', {'when': 'previous'}, name='previous_events'),
    url(r'^event/(?P<slug>[\w\-]+)/(?P<view>[\w\-]*?)$', 'event', name='event'),
#   url(r'^test_work_image/(?P<id>[0-9]*)', 'artist_work_image'),
    url(r'^zoom/(?P<id>[0-9]*)', 'zoom'),
)

urlpatterns += patterns('django.views.generic.simple', 
    url(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^artists$', 'direct_to_template', {'template': 'artists.html'}),
    url(r'^artist$', 'direct_to_template', {'template': 'artist.html'}),
    url(r'^selected$', 'direct_to_template', {'template': 'artist-selected.html'}),
    url(r'^available$', 'direct_to_template', {'template': 'artist-available.html'}),
    url(r'^single/images$', 'direct_to_template', {'template': 'artist-single-image.html'}),    
    url(r'^single/videos$', 'direct_to_template', {'template': 'artist-single-video.html'}),    
    url(r'^exhibitions$', 'direct_to_template', {'template': 'artist-exhibitions.html'}),
    url(r'^biography$', 'direct_to_template', {'template': 'artist-biography.html'}),
    url(r'^cv$', 'direct_to_template', {'template': 'artist-cv.html'}),
    url(r'^publications$', 'direct_to_template', {'template': 'artist-publications.html'}),
    url(r'^publications-detail$', 'direct_to_template', {'template': 'publications-detail.html'}),
    url(r'^press$', 'direct_to_template', {'template': 'artist-press.html'}),
    url(r'^news$', 'direct_to_template', {'template': 'artist-news.html'}),
    url(r'^videos$', 'direct_to_template', {'template': 'artist-videos.html'}),
    url(r'^exhibitions$', 'direct_to_template', {'template': 'exhibitions.html'}),
    url(r'^publications$', 'direct_to_template', {'template': 'publications.html'}),
    url(r'^exhibitions/current$', 'direct_to_template', {'template': 'exhibitions-current.html'}),
    url(r'^exhibitions/exhib-name/works$', 'direct_to_template', {'template': 'exhibitions-works.html'}),
    url(r'^exhibitions/exhib-name/artists$', 'direct_to_template', {'template': 'exhibitions-artists.html'}),
    url(r'^exhibitions/exhib-name/press$', 'direct_to_template', {'template': 'exhibitions-press.html'}),
    url(r'^exhibitions/exhib-name/publications$', 'direct_to_template', {'template': 'exhibitions-publications.html'}),
    url(r'^exhibitions/exhib-name/videos$', 'direct_to_template', {'template': 'exhibitions-videos.html'}),
    url(r'^exhibitions/upcoming$', 'direct_to_template', {'template': 'exhibitions-upcoming.html'}),
    url(r'^exhibitions/previous$', 'direct_to_template', {'template': 'exhibitions-previous.html'}),
    url(r'^exhibition$', 'direct_to_template', {'template': 'exhibition.html'}),
    url(r'^events/current$', 'direct_to_template', {'template': 'events-current.html'}),
    url(r'^events/upcoming$', 'direct_to_template', {'template': 'events-upcoming.html'}),
    url(r'^events/previous$', 'direct_to_template', {'template': 'events-previous.html'}),
    url(r'^events/event-name/works$', 'direct_to_template', {'template': 'event-works.html'}),
    url(r'^events/event-name/biography$', 'direct_to_template', {'template': 'event-biography.html'}),
    url(r'^events/event-name/press$', 'direct_to_template', {'template': 'event-press.html'}),
    url(r'^events/event-name/publications$', 'direct_to_template', {'template': 'event-publications.html'}),
    url(r'^events/event-name/videos$', 'direct_to_template', {'template': 'event-videos.html'}),
    url(r'^events/event-name/press$', 'direct_to_template', {'template': 'event-press.html'}),
    url(r'^event$', 'direct_to_template', {'template': 'events.html'}),
    url(r'^about$', 'direct_to_template', {'template': 'about-mission.html'}),
    url(r'^about/mission$', 'direct_to_template', {'template': 'about-mission.html'}),
    url(r'^about/people$', 'direct_to_template', {'template': 'about-people.html'}),
    url(r'^about/people/abhay-maskara$', 'direct_to_template', {'template': 'abhay-maskara.html'}),
    url(r'^about/people/rivka-sadarangani$', 'direct_to_template', {'template': 'rivka-sadarangani.html'}),
    url(r'^about/press$', 'direct_to_template', {'template': 'about-press.html'}),
    url(r'^about/publications$', 'direct_to_template', {'template': 'about-publications.html'}),
    url(r'^about/space$', 'direct_to_template', {'template': 'about-space.html'}),
    url(r'^contact$', 'direct_to_template', {'template': 'contact.html'}),
    url(r'^selected$', 'direct_to_template', {'template': 'selected.html'}),
    url(r'^single$', 'direct_to_template', {'template': 'single.html'}),
    url(r'^views$', 'direct_to_template', {'template': 'views.html'}),
    
    # sitemap

    # Search (haystack)                    
    url(r'^search/', include('haystack.urls')),
#    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})

                    

)


if settings.LOCAL_DEVELOPMENT:
  urlpatterns += patterns('',
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(settings.PROJECT_ROOT, "media")}),
)

