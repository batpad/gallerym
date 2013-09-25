import Image

from maskara.gallery.models import ArtistWork
from os.path import join

MEDIA_BASE = "/srv/gallerym/maskara/media/"
def artist_works():
    for aw in ArtistWork.objects.all():
        try:
            i = Image.open(join(MEDIA_BASE, str(aw.image)))
        except:
            print aw
            aw.image = ''
            aw.save()
