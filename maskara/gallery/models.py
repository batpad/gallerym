from django.db import models
from maskara.base.models import BaseModel
#from adminsortable.models import Sortable
#from adminsortable.fields import models.ForeignKey
from image_cropping import ImageRatioField
#from tasks import create_tiles, update_index
from os.path import basename
from django.db.models.signals import post_save
from django.contrib.admin.models import LogEntry
from django.utils.html import strip_tags
from filebrowser.fields import FileBrowseField
from sortable.models import Sortable
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class OrderableBase(BaseModel):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.order:
            return super(self, Orderable).save(*args, **kwargs)
        else:
            fk_field = self.fk_field
            fk_obj = self.__getattribute__(fk_field)
            qset = self.__class__.objects.filter(**{fk_field: fk_obj})
            if qset.count() == 0:
                self.order = 0
            else:
                last_order = qset.order_by('-order')[0].order
                self.order = last_order + 1
            return super(OrderableBase, self).save(*args, **kwargs)             


class Review(OrderableBase):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    translated_by = models.CharField(max_length=1024, blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #pdf = models.FileField(blank=True, upload_to='review_pdfs/')
    published = models.BooleanField(default=False)
    order = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        ordering = ['order', 'id']
    
    def __unicode__(self):
        return self.title


class Video(BaseModel):
    title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    duration = models.IntegerField(help_text="in minutes", blank=True, null=True)
    video_file = FileBrowseField("Video", max_length=1024, extensions=['.mp4', '.m4v'], blank=True, null=True)
    vimeo_id = models.CharField(max_length=128, blank=True)
    order = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['order', 'id']

    def __unicode__(self):
        return self.title

    def clean(self):
        if not (self.video_file or self.vimeo_id):
            raise ValidationError("Please link to a video file or enter the vimeo id for the video")
        if (self.video_file and self.vimeo_id):
            raise ValidationError("Please enter only one of video file or vimeo id")

class PressRelease(OrderableBase):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=512, blank=True)
    publisher = models.CharField(max_length=1024)
    date = models.DateField(blank=True, null=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #pdf = models.FileField(blank=True, upload_to='pressrelease_pdfs/')
    published = models.BooleanField(default=False)
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order', 'id']


    def __unicode__(self):
        return self.title



class GalleryPerson(BaseModel):
    name = models.CharField(max_length=512)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    text = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Artist(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=512)
    slug = models.SlugField(unique=True)
    dob = models.DateField(blank=True, null=True)
    birth_location = models.CharField(max_length=1024, blank=True)
    bio = models.TextField(blank=True)
    bio_pdf = FileBrowseField("Bio PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #bio_pdf = models.FileField(blank=True, upload_to='artist_bio_pdfs/')
    #press_pdf = models.FileField(blank=True, upload_to='artist_press_pdfs/')
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='artist_images/')
    url = models.URLField(blank=True)
    is_represented = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    videos = generic.GenericRelation("Video")

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def get_absolute_url(self):
        return "/artist/%s/" % self.slug

    class Meta:
        ordering = ['name']

#    def save(self, *args, **kwargs):
#        super(Artist, self).save(*args, **kwargs)
#        do_update_index()
   
    def __unicode__(self):
        return self.name

'''
class ArtistNews(BaseModel):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=1024)
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return self.title
'''


class ArtistInfoBase(BaseModel):
    artist = models.ForeignKey(Artist)
    year = models.IntegerField(max_length=4)
    text = models.TextField()
    link = models.URLField(blank=True, verify_exists=False)

    def __unicode__(self):
        return "%s: %s" % (self.year, strip_tags(self.text),)

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
        return strip_tags(self.text)


WORK_CATEGORIES = (
    ('0', 'Uncategorized'),
    ('1', 'Painting'),
    ('2', 'Sculpture'),
    ('3', 'Photography'),
    ('4', 'Video'),
    ('5', 'Installation'),
)

class ArtistWork(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=1024)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(upload_to='work_images/', blank=True)
    is_selected = models.BooleanField(default=False)
    category = models.CharField(choices=WORK_CATEGORIES, max_length=64)
    code = models.CharField(max_length=128, blank=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) #FIXME: change to DecimalField
    size_text = models.CharField(max_length=1024, blank=True)
    material = models.CharField(max_length=1024, blank=True)
    year = models.IntegerField(max_length=4, blank=True, null=True)
    theme = models.TextField(blank=True)
    attribution = models.TextField(blank=True)
    price = models.CharField(max_length=128, blank=True, null=True)
    published = models.BooleanField(default=False)
    order = models.PositiveIntegerField()
    videos = generic.GenericRelation("Video")

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

    def save(self, *args, **kwargs):
        if self.order is None:
            artist = self.artist
            curr_works = ArtistWork.objects.order_by('-order').filter(artist=artist)
            if curr_works.count() > 0:
                new_order = curr_works[0].order + 1
            else:
                new_order = 0
            self.order = new_order
        super(ArtistWork, self).save(*args, **kwargs)

    class Meta:
        ordering = ['artist', 'order']

    def __unicode__(self):
        return "%s: %s" % (self.artist.name, self.title,)


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
    #test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")
    fk_field = 'artist'


class ArtistPressRelease(PressRelease):
    #test = models.CharField(max_length=128)
    artist = models.ForeignKey("Artist")
    fk_field = 'artist'

class FrontPageItem(BaseModel, Sortable):
    event = models.ForeignKey("Event", blank=True, null=True)
    exhibition = models.ForeignKey("Exhibition", blank=True, null=True)

    class Meta(Sortable.Meta):
        pass

    def clean(self):
        if not (self.event or self.exhibition):
            raise ValidationError("Requires either an event or exhibition")
        if (self.event and self.exhibition):
            raise ValidationError("Please chose only one of either an event or exhibition")

    def __unicode__(self):
        if (self.event):
            return "Event: " + unicode(self.event)
        else:
            return "Exhibition: " + unicode(self.exhibition)


class Exhibition(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)
#    is_front_page = models.BooleanField(default=False, help_text='Should this be displayed on the front-page?')
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
    videos = generic.GenericRelation("Video")

    @property
    def class_name(self):
        return(self._meta.verbose_name)
    
    def get_absolute_url(self):
        return "/exhibition/%s/" % self.slug

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class ExhibitionReview(Review):
    exhibition = models.ForeignKey(Exhibition)
    fk_field = 'exhibition'


class ExhibitionPressRelease(PressRelease):
    exhibition = models.ForeignKey(Exhibition)
    fk_field = 'exhibition'

    class Meta:
        pass


class Event(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True)
#    is_front_page = models.BooleanField(default=False, help_text='Should this be displayed on the front-page?')
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    #featured_artist = models.ForeignKey(Artist, null=True, blank=True)
    featured_artists = models.ManyToManyField(Artist, blank=True)
    featured_work = models.ManyToManyField(ArtistWork, blank=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='event_images/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    videos = generic.GenericRelation("Video")
    
    @property
    def class_name(self):
        return(self._meta.verbose_name)

    def get_absolute_url(self):
        return "/event/%s/" % self.slug

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class EventReview(Review):
    event = models.ForeignKey(Event)
    fk_field = 'event'


class EventPressRelease(PressRelease):
    event = models.ForeignKey(Event)

    class Meta:
        pass

class Publication(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
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

