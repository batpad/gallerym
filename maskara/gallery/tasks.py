from celery import task
from subprocess import check_call
from maskara import settings
from os.path import join, basename
from django.core.management import call_command


#@task()
def create_tiles(artist_work_image):
    image_path = join(settings.MEDIA_ROOT, artist_work_image.image.path)
    outpath = join(settings.MEDIA_ROOT, "tiles", str(artist_work_image.id))
    cmd = ["gdal2tiles.py", "-p", "raster", "-z", "2-6", image_path, outpath]
    check_call(cmd)    
    artist_work_image.is_tiled = True
    artist_work_image.save()


@task()
def update_index():
    call_command("update_index")
