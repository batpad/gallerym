from django.db import models
from maskara.base.models import BaseModel
#from adminsortable.models import Sortable
#from adminsortable.fields import models.ForeignKey
from image_cropping import ImageRatioField
from tasks import create_tiles, update_index
from os.path import basename
from django.db.models.signals import post_save
from django.contrib.admin.models import LogEntry



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
    order = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        ordering = ['order']
    
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
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order']


    def __unicode__(self):
        return self.title



class Artist(BaseModel):
    name = models.CharField(max_length=512)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='artist_images/')
    url = models.URLField(blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        pass

#    def save(self, *args, **kwargs):
#        super(Artist, self).save(*args, **kwargs)
#        do_update_index()
   
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
    size = models.CharField(max_length=1024, blank=True) #FIXME: change to DecimalField
    material = models.CharField(max_length=1024, blank=True)
    year = models.IntegerField(max_length=4, blank=True, null=True)
    theme = models.TextField(blank=True)
    attribution = models.TextField(blank=True)
    price = models.CharField(max_length=128)
    published = models.BooleanField(default=False)
    order = models.PositiveIntegerField()

    

    class Meta:
        ordering = ['order']


    def __unicode__(self):
        return self.title

class ArtistWorkImage(BaseModel):
    work = models.ForeignKey(ArtistWork)
    image = models.ImageField(upload_to='work_images/')
    caption = models.CharField(max_length=512, blank=True)
    is_hires = models.BooleanField(default=True)
    order = models.PositiveIntegerField()



    class Meta:
        ordering = ['order']


    def __unicode__(self):
        return self.caption

    @property
    def tms_url(self):
        return "/media/tiles/%s/{z}/{x}/{y}.png" % basename(self.image.path)        

    def save(self):
        super(ArtistWorkImage, self).save()
        if self.is_hires:
            create_tiles.delay(self.image.path)


class ArtistReview(Review):
    test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")




    

class ArtistPressRelease(PressRelease):
    test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")





class Exhibition(BaseModel):
    title = models.CharField(max_length=1024)
    start_date = models.DateField()
    end_date = models.DateField()
    preview_date = models.DateField(blank=True, null=True)
    preview_start_time = models.TimeField(blank=True, null=True)
    preview_end_time = models.TimeField(blank=True, null=True)
    autopublish_date = models.DateField()
    curated_by = models.CharField(max_length=512, blank=True)
    image = models.ImageField(blank=True, upload_to='exhibition_images/')
    cropping = ImageRatioField('image', '430x360', size_warning=True)
    featured_artists = models.ManyToManyField("Artist", blank=True, null=True)
    featured_work = models.ManyToManyField("ArtistWork", blank=True, null=True)
    published = models.BooleanField(default=False)



    class Meta:
        pass

    def __unicode__(self):
        return self.title


class ExhibitionReview(Review):
    test = models.CharField(max_length=128)
    exhibition = models.ForeignKey(Exhibition)




class ExhibitionPressRelease(PressRelease):
    test = models.CharField(max_length=128)
    exhibition = models.ForeignKey(Exhibition)
    

    class Meta:
        pass



class Event(BaseModel):
    title = models.CharField(max_length=1024)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    featured_artist = models.ForeignKey(Artist, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='event_images/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    


    class Meta:
        pass

    def __unicode__(self):
        return self.title



class Publication(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    editor = models.CharField(max_length=1024, blank=True)
    publisher = models.CharField(max_length=1024, blank=True)
    featured = models.BooleanField(default=False, help_text="display on front page?")
    isbn = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='publication_images/', blank=True)
    pdf = models.FileField(upload_to='publication_pdfs/', blank=True)
    available = models.BooleanField(default=True)
    published = models.BooleanField(default=False)

    @property
    def class_name(self):
        return(self._meta.verbose_name)


    class Meta:
        pass


    def __unicode__(self):
        return self.title


def do_update_index(*args, **kwargs):
    sender = kwargs['sender']
    if sender not in [LogEntry]:
        update_index.delay()

post_save.connect(do_update_index)

# Create your models here.
# ^^ They are above, mind turning your head up ? :P
