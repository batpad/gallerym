from maskara.gallery.models import *
from django.utils.html import strip_tags

def do():
    classes = [ArtistEducation, ArtistSoloExhib, ArtistGroupExhib, ArtistCollection, ArtistAward]
    for c in classes:
        for obj in c.objects.all():
            print obj.text
            new_text = strip_tags(obj.text)
            obj.text = new_text
            print new_text
            obj.save()

