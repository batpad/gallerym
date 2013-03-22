from celery import task
from subprocess import call
from maskara import settings
from os.path import join, basename
from django.core.management import call_command


@task()
def create_tiles(image_path):
    outpath = join(settings.MEDIA_ROOT, "tiles", basename(image_path))
    cmd = ["gdal2tiles.py", "-p", "raster", image_path, outpath]
    call(cmd)    


@task()
def update_index():
    call_command("update_index")
