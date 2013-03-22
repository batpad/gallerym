from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maskara.views.home', name='home'),
    # url(r'^maskara/', include('maskara.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple', 
    url(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^artists$', 'direct_to_template', {'template': 'artists.html'}),
    url(r'^artist$', 'direct_to_template', {'template': 'artist.html'}),
    url(r'^selected$', 'direct_to_template', {'template': 'selected.html'}),
    url(r'^single$', 'direct_to_template', {'template': 'single.html'}),
    url(r'^biography$', 'direct_to_template', {'template': 'biography.html'}),
    url(r'^cv$', 'direct_to_template', {'template': 'cv.html'}),
    url(r'^publications$', 'direct_to_template', {'template': 'publications.html'}),
    url(r'^press$', 'direct_to_template', {'template': 'press.html'}),
    url(r'^news$', 'direct_to_template', {'template': 'news.html'}),
    url(r'^talks$', 'direct_to_template', {'template': 'talks.html'}),
    url(r'^exhibitions$', 'direct_to_template', {'template': 'exhibitions.html'}),
    url(r'^publications$', 'direct_to_template', {'template': 'publications.html'}),
    url(r'^exhibitions/current$', 'direct_to_template', {'template': 'exhibitions-current.html'}),
    url(r'^exhibitions/upcoming$', 'direct_to_template', {'template': 'exhibitions-upcoming.html'}),
    url(r'^exhibitions/previous$', 'direct_to_template', {'template': 'exhibitions-previous.html'}),
    url(r'^exhibition$', 'direct_to_template', {'template': 'exhibition.html'}),
    url(r'^events/current$', 'direct_to_template', {'template': 'events-current.html'}),
    url(r'^events/upcoming$', 'direct_to_template', {'template': 'events-upcoming.html'}),
    url(r'^events/previous$', 'direct_to_template', {'template': 'events-previous.html'}),
    url(r'^event$', 'direct_to_template', {'template': 'events.html'}),
    url(r'^about$', 'direct_to_template', {'template': 'mission.html'}),
    url(r'^about/mission$', 'direct_to_template', {'template': 'mission.html'}),
    url(r'^about/people$', 'direct_to_template', {'template': 'people.html'}),
    url(r'^about/press$', 'direct_to_template', {'template': 'press.html'}),
    url(r'^about/publications$', 'direct_to_template', {'template': 'publications.html'}),
    url(r'^about/space$', 'direct_to_template', {'template': 'space.html'}),
    url(r'^contact$', 'direct_to_template', {'template': 'contact.html'}),
)