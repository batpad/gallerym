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
from django.utils.safestring import mark_safe
from filebrowser.fields import FileBrowseField
from sortable.models import Sortable
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from easy_thumbnails.files import get_thumbnailer
import datetime
from maskara.base.managers import PublishedManager

class OrderableBase(BaseModel):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.order:
            return super(OrderableBase, self).save(*args, **kwargs)
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


class Review(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    date = models.DateField()
    author = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    translated_by = models.CharField(max_length=1024, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    published = models.BooleanField(default=False)
    display_on_artists = models.BooleanField(default=True, help_text="Display on artists' press pages?")
#    display_on_about = models.BooleanField(default=False, help_text="Display on main gallery about press?")
#    order = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
        ordering = ['-date', 'id']
    
    def __unicode__(self):
        return self.title

class AboutReview(BaseModel):
    title = models.CharField(max_length=1024)
    date = models.DateField()
    author = models.CharField(max_length=1024, blank=True)
    source = models.CharField(max_length=1024, blank=True)
    translated_by = models.CharField(max_length=1024, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date', 'id']

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

    def get_absolute_url(self):
        return "/about/people/%d" % self.id

    def list_image(self):
        return self.get_image({'size': ((150,150,)), 'crop': True, 'upscale': True})

    def get_main_image(self):
        return self.get_image({'size': (450,450), 'upscale': True})        

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
    catalog_pdf = FileBrowseField("Catalog PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #bio_pdf = models.FileField(blank=True, upload_to='artist_bio_pdfs/')
    #press_pdf = models.FileField(blank=True, upload_to='artist_press_pdfs/')
    pdf = FileBrowseField("Press PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #press_pdf = FileBrowseField("Press PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='artist_images/')
    url = models.URLField(blank=True)
    is_represented = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    videos = generic.GenericRelation("Video")
    objects = PublishedManager()

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)

    def get_absolute_url(self):
        return "/artist/%s" % self.slug

    def get_works(self):
        return self.artistwork_set.all()

    def get_press(self):
        own_press = list(self.artistreview_set.filter(published=True))
        exhibs = self.exhibition_set.all()
        exhib_press = list(ExhibitionReview.objects.filter(published=True).filter(exhibition__in=exhibs).filter(display_on_artists=True))
        events = self.event_set.all()
        event_press = list(EventReview.objects.filter(published=True).filter(event__in=events).filter(display_on_artists=True))
        all_press = own_press + exhib_press + event_press
        all_press.sort(lambda x,y: -1 if x.date > y.date else 1)
        return all_press


    def get_list_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.get_absolute_url(),
            'image': self.list_image()
        }

    def list_image(self):
        return self.get_image({'size': ((150,150,)), 'crop': True, 'upscale': True})

    def get_main_image(self):
        return self.get_image({'size': (450,450), 'upscale': True})

    class Meta:
        ordering = ['name']

#    def save(self, *args, **kwargs):
#        super(Artist, self).save(*args, **kwargs)
#        do_update_index()
   
    def __unicode__(self):
        return self.name

    def has_selected(self):
        return self.artistwork_set.filter(is_selected=True).count() > 0

    def has_available(self):
        return self.artistwork_set.filter(is_available=True).count() > 0

    def has_exhibitions(self):
        return Exhibition.objects.filter(featured_artists=self).exclude(published=False).count() > 0

    def has_events(self):
        return self.event_set.count() > 0

    def has_education(self):
        return self.artisteducation_set.count() > 0

    def has_solo_exhibs(self):
        return self.artistsoloexhib_set.count() > 0

    def has_group_exhibs(self):
        return self.artistgroupexhib_set.count() > 0

    def has_collections(self):
        return self.artistcollection_set.count() > 0

    def has_awards(self):
        return self.artistaward_set.count() > 0

    def has_cv(self):
        return self.has_education() or self.has_solo_exhibs() or self.has_group_exhibs() or self.has_collections() or self.has_awards()

    def has_press(self):
        return len(self.get_press()) > 0
        #return self.artistpress_set.count() > 0

    def has_publications(self):
        return self.publication_set.count() > 0

    def has_news(self):
        return self.artistnews_set.count() > 0

    def has_videos(self):
        return self.videos.count() > 0    



    

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

    @classmethod
    def get_by_year(kls, artist):
        years = {}
        for obj in kls.objects.filter(artist=artist).order_by('year'):
            year = obj.year
            if year not in years.keys():
                years[year] = []
            item = {
                'text': obj.text,
                'link': obj.link
            }            
            years[year].append(item)
        return years

    class Meta:
        abstract = True
        ordering = ['-year']

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

'''
class ArtistPress(ArtistInfoBase):
    pass
'''

class ArtistNews(BaseModel):
    artist = models.ForeignKey(Artist)
    date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=512)
    text = models.TextField(blank=True)
    link = models.URLField(blank=True, verify_exists=False)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)    
    #image = models.FileField(blank=True, upload_to='artist_news/')

    def __unicode__(self):
        return self.title


WORK_CATEGORIES = (
    ('0', 'Painting'),
    ('1', 'Sculpture'),
    ('2', 'Photography'),
    ('3', 'Video'),
    ('4', 'Installation'),
    ('5', 'Print'),
    ('6', 'Uncategorized'),
)

class ArtistWork(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=1024)
    image = FileBrowseField("Image", help_text="not used, just for reference from old database", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    #image = models.ImageField(upload_to='work_images/', blank=True)
    pdf = FileBrowseField("PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    is_selected = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
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

    def get_absolute_url(self):
        return "/artist/%s/works/%d" % (self.artist.slug, self.id,)

    def get_zoom_url(self):
        return "/zoom/%d" % self.id

    def get_zoomables_qset(self):
        return self.artistworkimage_set.filter(is_hires=True).filter(is_tiled=True)

    def get_zoom_dict(self):
        return [i.get_dict() for i in self.get_zoomables_qset()]

    def get_image(self, options):
        if self.artistworkimage_set.count() > 0:
            image_obj = self.artistworkimage_set.all()[0].image
        elif hasattr(self, 'image') and self.image:
            image_obj = self.image
        else:
            image_obj = None
        if image_obj:
            return get_thumbnailer(image_obj.path).get_thumbnail(options).url   
        else:
            size = options['size']
            width = size[0]
            height = size[1] if len(size) > 1 else int(width * 0.75)
            return "http://placehold.it/%dx%d" % (width, height,)

    def get_thumbnail(self):
        '''
            for admin view
        '''
        options = {'size': (60, 60), 'crop': True}
        url = self.get_image(options)
        #url = get_thumbnailer(self.image.path).get_thumbnail(options).url
        return "<img src='%s' />" % url


    get_thumbnail.allow_tags = True
    get_thumbnail.short_description = "Thumbnail"

    def has_zoom(self):
        return self.get_zoomables_qset().count() > 0

    def thumb(self):
        options = {'size': (60, 60)}
        return self.get_image(options)


    def list_image(self):
        options = {'size': (150, 200)}
        return self.get_image(options)

    def medium_image(self):
        options = {'size': (800,600)}
        return self.get_image(options)


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
        return "%d - %s: %s" % (self.id, self.artist.name, self.title,)


class ArtistWorkImage(BaseModel):
    work = models.ForeignKey(ArtistWork)
    #image = models.ImageField(upload_to='work_images/')
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    caption = models.CharField(max_length=512, blank=True)
    is_hires = models.BooleanField(default=True)
    #is_main = models.BooleanField(default=False, help_text='Is the main image for this work')
    order = models.PositiveIntegerField()
    is_tiled = models.BooleanField(editable=False, default=False)


    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.caption

    def get_dict(self):
        return {
            'id': self.id,
            'tms_url': self.tms_url,
            'caption': self.caption,
            'thumb': self.zoom_thumb(),
            'width': self.image.width,
            'height': self.image.height
        }

    def thumb(self):
        options = {'size': (60, 60), 'crop': True}
        return self.get_image(options)       

    def zoom_thumb(self):
        options = {'size': (180, 180)}
        return self.get_image(options)

    def has_zoom(self):
        return self.is_hires and self.is_tiled

    def medium_image(self):
        options = {'size': (800,800)}
        return self.get_image(options)

    @property
    def tms_url(self):
        return "/media/tiles/%d/{z}/{x}/{y}.png" % self.id        

    def save(self):
        super(ArtistWorkImage, self).save()
        if self.is_hires:
            pass #create_tiles.delay(self)


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
    blurb = models.CharField(max_length=512, blank=True, default="Current Exhibition")

    class Meta(Sortable.Meta):
        pass

    def clean(self):
        if not (self.event or self.exhibition):
            raise ValidationError("Requires either an event or exhibition")
        if (self.event and self.exhibition):
            raise ValidationError("Please chose only one of either an event or exhibition")

    def get_type(self):
        if self.event:
            return "Event"
        elif self.exhibition:
            return "Exhibition"
        else:
            raise

    def get_data(self):
        if self.event:
            return self.get_event_data()
        else:
            return self.get_exhib_data()

    def get_event_data(self):
        return {
            'id': self.event.id,
            'url': self.event.get_absolute_url(),
            'title': self.event.title,
            'large_image': self.event.get_image({'size': (800,600,)}),
            'thumb': self.event.get_image({'size': (150,150,), 'crop': True}),
            'artists': self.event.get_artists_string(),
            'start_date': self.event.date,
            'end_date': None,
            'text_lines': self.event.get_text_lines()
        }

    def get_exhib_data(self):
        return {
            'id': self.exhibition.id,
            'url': self.exhibition.get_absolute_url(),
            'title': self.exhibition.title,
            'large_image': self.exhibition.get_image({'size': (800,600,)}),
            'thumb': self.exhibition.get_image({'size': (150,150,), 'crop': True}),
            'artists': self.exhibition.get_artists_string(),
            'start_date': self.exhibition.start_date,
            'end_date': self.exhibition.end_date,
            'text_lines': self.exhibition.get_text_lines()
        }

    def __unicode__(self):
        if (self.event):
            return "Event: " + unicode(self.event)
        else:
            return "Exhibition: " + unicode(self.exhibition)


class Exhibition(BaseModel):
    old_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    one_liner = models.CharField(max_length=512, blank=True)
    location = models.CharField(max_length=255, default="Gallery Maskara")
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
    pdf = FileBrowseField("Press Reviews PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    catalog_pdf = FileBrowseField("Catalog PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    press_release = FileBrowseField("Press Release PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='exhibition_images/')
    #cropping = ImageRatioField('image', '430x360', size_warning=True)
    featured_artists = models.ManyToManyField("Artist", blank=True, null=True)
    #featured_work = models.ManyToManyField("ArtistWork", blank=True, null=True)
    exhibition_works = models.ManyToManyField("ArtistWork", through="ExhibitionWork", blank=True, null=True)
    published = models.BooleanField(default=False)
    videos = generic.GenericRelation("Video")

    @property
    def class_name(self):
        return(self._meta.verbose_name)

    def get_works(self):
        return [ew.work for ew in ExhibitionWork.objects.filter(exhibition=self).order_by('order')]

    def get_press(self):
        return self.exhibitionreview_set.filter(published=True)

    @classmethod
    def get_current(kls):
        now = datetime.datetime.now()
        current_exhibs = kls.objects.filter(start_date__lte=now).filter(end_date__gte=now)
        if current_exhibs.count() > 0:
            return current_exhibs[0]
        else:
            return None
            #return kls.objects.all().order_by('-start_date')[0]  

    @classmethod
    def has_upcoming(kls):
        now = datetime.datetime.now()
        return kls.objects.filter(start_date__gt=now).count() > 0

    def is_current(self):
        return Exhibition.get_current() and self.id == Exhibition.get_current().id

    def is_upcoming(self):
        now = datetime.datetime.now().date()
        return self.start_date > now and not self.is_current() 

    def is_previous(self):
        now = datetime.datetime.now().date()
        return self.end_date < now and not self.is_current()

    def get_artists_string(self):
        return mark_safe(", ".join(["<a href='%s'>%s</a>" % (a.get_absolute_url(), a.name,) for a in self.featured_artists.all()]))

    def is_same_year(self):
        return self.start_date.year == self.end_date.year        

    def get_text_lines(self):
        lines = []
        #if self.curated_by:
        #    lines.append("Curated by %s" % self.curated_by)
        if self.location:
            lines.append("Location: %s" % self.location)
        # if self.preview_date:
        #     dtformat = self.preview_date.strftime("%B %d, %Y")
        #     lines.append("Preview Date %s" % dtformat)
        return lines

    def list_image(self):
        return self.get_image({'size': (190,140,), 'crop': True, 'upscale': True})

    def main_image(self):
        return self.get_image({'size': (800,800,), 'upscale': True})
 
    def get_absolute_url(self):
        return "/exhibition/%s" % self.slug

    class Meta:
        ordering = ['-start_date']

    def __unicode__(self):
        return self.title

    def has_works(self):
        return ExhibitionWork.objects.filter(exhibition=self).count() > 0

    def has_artists(self):
        return self.featured_artists.count() > 0

    def has_press(self):
        return self.exhibitionreview_set.filter(published=True).count() > 0

    def has_publications(self):
        return self.publication_set.count() > 0

    def has_videos(self):
        return self.videos.count() > 0
        

class ExhibitionWork(BaseModel):
    exhibition = models.ForeignKey(Exhibition)
    work = models.ForeignKey("ArtistWork")
    order = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.order is None:
            qset = ExhibitionWork.objects.filter(exhibition=self.exhibition).order_by('-order')
            if qset.count() == 0:
                self.order = 0
            else:
                last_order = qset[0].order
                self.order = last_order + 1
        return super(ExhibitionWork, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.work)


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
    location = models.CharField(max_length=512, default="Gallery Maskara", blank=True)
#    is_front_page = models.BooleanField(default=False, help_text='Should this be displayed on the front-page?')
    date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    time_from = models.TimeField()
    time_to = models.TimeField()
    #featured_artist = models.ForeignKey(Artist, null=True, blank=True)
    featured_artists = models.ManyToManyField(Artist, blank=True)
    #featured_work = models.ManyToManyField(ArtistWork, blank=True)
    image = FileBrowseField("Image", max_length=512, extensions=[".jpg", ".png", ".jpeg"], blank=True, null=True)
    pdf = FileBrowseField("Press Reviews PDF", max_length=1024, extensions=["*.pdf"], blank=True, null=True)
    catalog_pdf = FileBrowseField("Catalog PDF", max_length=512, extensions=[".pdf"], blank=True, null=True)
    press_release = FileBrowseField("Press Release PDF", max_length=1024, extensions=["*.pdf"], blank=True, null=True)
    #image = models.ImageField(blank=True, upload_to='event_images/')
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    videos = generic.GenericRelation("Video")
   
    @classmethod
    def get_current(kls):
        now = datetime.datetime.now()
        if kls.objects.filter(date__gte=now).filter(end_date__gte=now).exclude(published=False).count() > 0:
            return kls.objects.filter(date__lte=now).filter(end_date__gte=now).exclude(published=False).order_by('date')
        else:
            return None

    @classmethod
    def has_upcoming(kls):
        now = datetime.datetime.now()
        return kls.objects.filter(date__gt=now).count() > 0

    def get_works(self):
        return [ew.work for ew in EventWork.objects.filter(event=self).order_by('order')]

    def is_current(self):
        return Event.get_current() and self.id == Event.get_current().id

    def is_upcoming(self):
        now = datetime.datetime.now().date()
        return self.date > now and not self.is_current()

    def is_previous(self):
        now = datetime.datetime.now().date()
        return self.date < now and not self.is_current()
 
    @property
    def class_name(self):
        return(self._meta.verbose_name)

    def get_artists_string(self):
        return mark_safe(", ".join(["<a href='%s'>%s</a>" % (a.get_absolute_url(), a.name,) for a in self.featured_artists.all()]))

    def get_list_image(self):
        return self.get_image({'size': (190,140,)})

    def main_image(self):
        return self.get_image({'size': (800,800,)})

    def get_text_lines(self):
        lines = []
        if self.location:
            lines.append("Location: " + self.location)
        return lines

    def get_absolute_url(self):
        return "/event/%s" % self.slug

    def get_press(self):
        return self.eventpress_set.filter(published=True)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.title

    def has_works(self):
        return EventWork.objects.filter(event=self).count() > 0

    def has_artists(self):
        return self.featured_artists.count() > 0

    
    def has_press(self):
        return self.eventreview_set.filter(published=True).count() > 0
    

    def has_publications(self):
        return self.publication_set.count() > 0

    def has_videos(self):
        return self.videos.count() > 0


class EventWork(BaseModel):
    event = models.ForeignKey(Event)
    work = models.ForeignKey("ArtistWork")
    order = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.order is None:
            qset = EventWork.objects.filter(event=self.event).order_by('-order')
            if qset.count() == 0:
                self.order = 0
            else:
                last_order = qset[0].order
                self.order = last_order + 1
        return super(EventWork, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.work)


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
    description = models.TextField(blank=True)
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

    def get_frontpage_dict(self):
        return {
            'id': self.id,
            'url': self.get_absolute_url(),
            'publisher': self.publisher,
            'title': self.title,
            'image': self.list_image()
        }

    def list_image(self):
        return self.get_image({'size': (150,200,)})

    def get_absolute_url(self):
        return "/publication/%d" % self.id

    class Meta:
        pass


    def __unicode__(self):
        return self.title


class SpaceImage(BaseModel, Sortable):
    image = FileBrowseField("Image", max_length=1024, extensions=[".jpg", ".jpeg"])
    caption = models.CharField(max_length=1024, blank=True)
    displayed = models.BooleanField(default=False)

    def list_image(self):
        return self.get_image({'size': (150,200,)})

    def get_main_image(self):
        return self.get_image({'size': (450,450), 'upscale': True}) 

    def __unicode__(self):
        return self.caption


class SpaceVideo(BaseModel, Sortable):
    video_file = FileBrowseField("Video", max_length=1024, extensions=['.mp4', '.m4v'], blank=True, null=True)
    vimeo_id = models.CharField(max_length=128, blank=True)
    caption = models.CharField(max_length=1024, blank=True)
    displayed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.caption

    def clean(self):
        if not (self.video_file or self.vimeo_id):
            raise ValidationError("Please link to a video file or enter the vimeo id for the video")
        if (self.video_file and self.vimeo_id):
            raise ValidationError("Please enter only one of video file or vimeo id")


def do_update_index(*args, **kwargs):
    sender = kwargs['sender']
    if sender not in [LogEntry]:
        update_index.delay()




