from django.contrib.sitemaps import Sitemap
from gallery.models import *

'''
Priority:

Exibition
Event
Artist

Artist work not sitemapped ( as it is linked to an artist )

'''

class ExhibitionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9


    
    def items(self):
        return  Exhibition.objects.filter(published = True)


    
    def items(self):
        return  Exhibition.objects.filter(published=True)

    def last_mod(self):
        return obj.pub_date



class EventSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8
    
    def items(self):
        return  Event.objects.filter(published = True)



    def last_mod(self):
        return obj.pub_date



class ArtistSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7
    
    def items(self):

        return  Artist.objects.filter(published = True)



    def last_mod(self):
        return obj.pub_date
    
