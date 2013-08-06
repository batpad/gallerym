from django.db import models
from maskara.base.models import BaseModel
#from adminsortable.models import Sortable
#from adminsortable.fields import models.ForeignKey
from image_cropping import ImageRatioField
#from tasks import create_tiles, update_index
from os.path import basename
from django.db.models.signals import post_save
from django.contrib.admin.models import LogEntry
from filebrowser.fields import FileBrowseField


class Review(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    translated_by = models.CharField(max_length=1024, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("Image", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #pdf = models.FileField(blank=True, upload_to='review_pdfs/')
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
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("Image", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #pdf = models.FileField(blank=True, upload_to='pressrelease_pdfs/')
    published = models.BooleanField(default=False)
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order']


    def __unicode__(self):
        return self.title



class GalleryPerson(BaseModel):
    name = models.CharField(max_length=512)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    text = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Artist(BaseModel):
    name = models.CharField(max_length=512)
    dob = models.DateField(blank=True, null=True)
    birth_location = models.CharField(max_length=1024, blank=True)
    bio = models.TextField(blank=True)
    bio_pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #bio_pdf = models.FileField(blank=True, upload_to='artist_bio_pdfs/')
    #press_pdf = models.FileField(blank=True, upload_to='artist_press_pdfs/')
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='artist_images/')
    url = models.URLField(blank=True)
    is_represented = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/artist/%i/" % self.id

    class Meta:
        ordering = ['name']

#    def save(self, *args, **kwargs):
#        super(Artist, self).save(*args, **kwargs)
#        do_update_index()
   
    def __unicode__(self):
        return self.name

class ArtistInfoBase(BaseModel):
    artist = models.ForeignKey(Artist)
    year = models.IntegerField(max_length=4)
    text = models.TextField()
    link = models.URLField(blank=True, verify_exists=False)

    def __unicode__(self):
        return "%s: %s" % (self.year, self.text,)

    class Meta:
        abstract = True

class ArtistEducation(ArtistInfoBase):
    pass

class ArtistSoloExhib(ArtistInfoBase):
    pass

class ArtistGroupExhib(ArtistInfoBase):
    pass

class ArtistCollection(ArtistInfoBase):
    pass

class ArtistAward(ArtistInfoBase):
    pass

class ArtistPress(ArtistInfoBase):
    pass

class ArtistNews(BaseModel):
    artist = models.ForeignKey(Artist)
    date = models.DateField(blank=True, null=True)
    text = models.TextField()
    link = models.URLField(blank=True, verify_exists=False)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)    
    #image = models.FileField(blank=True, upload_to='artist_news/')

    def __unicode__(self):
        return self.text


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
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(upload_to='work_images/', blank=True)
    is_selected = models.BooleanField(default=False)
    category = models.CharField(choices=WORK_CATEGORIES, max_length=64)
    code = models.CharField(max_length=128, blank=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #FIXME: change to DecimalField
    size_text = models.CharField(max_length=1024, blank=True)
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
    #image = models.ImageField(upload_to='work_images/')
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    caption = models.CharField(max_length=512, blank=True)
    is_hires = models.BooleanField(default=True)
    #is_main = models.BooleanField(default=False, help_text='Is the main image for this work')
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
            pass #create_tiles.delay(self.image.path)


class ArtistReview(Review):
    test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")


class ArtistPressRelease(PressRelease):
    test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")


class Exhibition(BaseModel):
    title = models.CharField(max_length=1024)
    is_front_page = models.BooleanField(default=False, help_text='Should this be displayed on the front-page?')
    start_date = models.DateField()
    end_date = models.DateField()
    preview_date = models.DateField(blank=True, null=True)
    preview_start_time = models.TimeField(blank=True, null=True)
    preview_end_time = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    autopublish_date = models.DateField()
    curated_by = models.CharField(max_length=512, blank=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='exhibition_images/')
    #cropping = ImageRatioField('image', '430x360', size_warning=True)
    featured_artists = models.ManyToManyField("Artist", blank=True, null=True)
    featured_work = models.ManyToManyField("ArtistWork", blank=True, null=True)
    published = models.BooleanField(default=False)

    @property
    def class_name(self):
        return(self._meta.verbose_name)
    
    def get_absolute_url(self):
        return "/exhibition/%i/" % self.id

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class ExhibitionReview(Review):
    exhibition = models.ForeignKey(Exhibition)


class ExhibitionPressRelease(PressRelease):
    exhibition = models.ForeignKey(Exhibition)

    class Meta:
        pass


class Event(BaseModel):
    title = models.CharField(max_length=1024)
    is_front_page = models.BooleanField(default=False, help_text='Should this be displayed on the front-page?')
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    featured_artist = models.ForeignKey(Artist, null=True, blank=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='event_images/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    
    @property
    def class_name(self):
        return(self._meta.verbose_name)

    def get_absolute_url(self):
        return "/event/%i/" % self.id

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class EventReview(Review):
    event = models.ForeignKey(Event)


class EventPressRelease(PressRelease):
    event = models.ForeignKey(Event)

    class Meta:
        pass

class Publication(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    date = models.DateField(blank=True, null=True)
    editor = models.CharField(max_length=1024, blank=True)
    publisher = models.CharField(max_length=1024, blank=True)
    featured = models.BooleanField(default=False, help_text="display on front page?")
    artist = models.ForeignKey(Artist, blank=True, null=True)
    exhibition = models.ForeignKey(Exhibition, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    isbn = models.CharField(max_length=128, blank=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)    
    #image = models.ImageField(upload_to='publication_images/', blank=True)
    #pdf = models.FileField(upload_to='publication_pdfs/', blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
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

#post_save.connect(do_update_index)

# Create your models here.
# ^^ They are above, mind turning your head up ? :P
