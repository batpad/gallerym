from celery import task
from subprocess import call
from maskara import settings
from os.path import join, basename

@task()
def create_tiles(image_path):
    outpath = join(settings.MEDIA_ROOT, "tiles", basename(image_path))
    cmd = ["gdal2tiles.py", "-p", "raster", image_path, outpath]
    call(cmd)    
