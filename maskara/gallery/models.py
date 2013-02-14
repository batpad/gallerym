from django.db import models
from maskara.base.models import BaseModel

class Review(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    translated_by = models.CharField(max_length=1024, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = models.FileField(blank=True, upload_to='review_pdfs/')
    published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title


class PressRelease(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=512, blank=True)
    publisher = models.CharField(max_length=1024)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='pressrelease_images/')
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = models.FileField(blank=True, upload_to='pressrelease_pdfs/')
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title



class Artist(BaseModel):
    name = models.CharField(max_length=512)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='artist_images/')
    url = models.URLField(blank=True)
    published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name


WORK_CATEGORIES = (
    ('painting', 'Painting'),
    ('sculpture', 'Sculpture'),
    ('photography', 'Photography'),
    ('video', 'Video'),
    ('installation', 'Installation'),
)

class ArtistWork(BaseModel):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='work_images/', blank=True)
    category = models.CharField(choices=WORK_CATEGORIES, max_length=64)
    code = models.CharField(max_length=128, blank=True)
    size = models.CharField(max_length=1024, blank=True)
    material = models.CharField(max_length=1024, blank=True)
    year = models.IntegerField(max_length=4, blank=True, null=True)
    theme = models.TextField(blank=True)
    attribution = models.TextField(blank=True)
    price = models.CharField(max_length=128)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class ArtistReview(Review):
    artist = models.ForeignKey("Artist")
    

class ArtistPressRelease(PressRelease):
    artist = models.ForeignKey("Artist")


class Exhibition(BaseModel):
    title = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField()
    autopublish_date = models.DateField()
    image = models.ImageField(blank=True, upload_to='exhibition_images/')
    featured_artists = models.ManyToManyField("Artist", blank=True, null=True)
    featured_work = models.ManyToManyField("ArtistWork", blank=True, null=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class ExhibitionReview(Review):
    exhibition = models.ForeignKey(Exhibition)


class ExhibitionPressRelease(PressRelease):
    exhibition = models.ForeignKey(Exhibition)


class Event(BaseModel):
    title = models.CharField(max_length=1024)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    featured_artist = models.ForeignKey(Artist, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='event_images/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Publication(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    editor = models.CharField(max_length=1024, blank=True)
    publisher = models.CharField(max_length=1024, blank=True)
    isbn = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='publication_images/', blank=True)
    pdf = models.FileField(upload_to='publication_pdfs/', blank=True)
    available = models.BooleanField(default=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

# Create your models here.
