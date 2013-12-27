from tasks import create_tiles
from models import ArtistWorkImage

def make_all_tiles():
    for w in ArtistWorkImage.objects.filter(is_hires=True).filter(is_tiled=False):
        create_tiles(w)