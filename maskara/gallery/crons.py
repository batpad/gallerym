from tasks import create_tiles
from models import *

def make_all_tiles():
    for w in ArtistWorkImage.objects.filter(is_hires=True).filter(is_tiled=False):
        create_tiles(w)

def make_links_http():
    press_classes = [ArtistReview, EventReview, ExhibitionReview]
    for p in press_classes:
        for obj in p.objects.all():
            if obj.url and obj.url != '':
                print obj.url
                if not obj.url.startswith("http"):
                    obj.url = "http://%s" % obj.url
                    obj.save()

