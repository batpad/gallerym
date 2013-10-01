from haystack import indexes
from haystack import site
from gallery.models import *

class ArtistIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Artist
class ArtistWorkIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    #theme = indexes.CharField(model_attr='theme')
    
    def get_model(self):
        return ArtistWork

class ExhibitionIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Exhibition

class EventIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Event 





site.register(Artist, ArtistIndex)
site.register(ArtistWork, ArtistWorkIndex)
site.register(Exhibition, ExhibitionIndex)
site.register(Event, EventIndex)


    
    
