from tasks import create_tiles
from models import *
from os.path import join
from subprocess import check_call
from django.conf import settings

def make_all_tiles():
    for w in ArtistWorkImage.objects.filter(is_hires=True).filter(is_tiled=False):
        if w.image and w.image != '':
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

def make_pdf_images():
    for p in Publication.objects.all():
        if not p.image and p.pdf:
            outpath = p.pdf.path[:-4] + ".jpg"
            infile = join(settings.MEDIA_ROOT, p.pdf.path)
            outfile = join(settings.MEDIA_ROOT, outpath)
            cmd = ["convert", infile, outfile]
            check_call(cmd)
            p.image = outpath
            p.save()
            print p.title

