from django.contrib import admin
from models import *
# from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
#from adminsortable.admin import SortableAdmin, admin.StackedInline
from image_cropping import ImageCroppingMixin
from sortable.admin import SortableAdmin
from chunks.models import Chunk
from django.contrib.contenttypes import generic
from django import forms

class ArtistWorkImageInline(admin.StackedInline):
    model = ArtistWorkImage
    sortable_field_name = 'order'
    extra = 0

class ArtistWorkInline(admin.StackedInline):
    model = ArtistWork
    sortable_field_name = 'order'
    extra = 0

class ExhibitionWorkInline(admin.StackedInline):
    raw_id_fields = ('work',)
    autocomplete_lookup_fields = {
        'fk': ['work'],
    }    
    model = ExhibitionWork
    sortable_field_name = 'order'
    extra = 0

class EventWorkInline(admin.StackedInline):
    raw_id_fields = ('work',)
    autocomplete_lookup_fields = {
        'fk': ['work'],
    }    
    model = EventWork
    sortable_field_name = 'order'
    extra = 0

class EventReviewInline(admin.StackedInline):
    model = EventReview
    extra = 0

'''
class ArtistNews(admin.StackedInline):
    model = ArtistNews
'''


class ArtistReviewInline(admin.StackedInline):
    model = ArtistReview
    extra = 0
    #inlines = []
    #sortable_field_name = 'order'

class VideoInline(generic.GenericStackedInline):
    model = Video    
    sortable_field_name = 'order'
    extra = 0

class ArtistInfoForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'style':'width:800px'}))

class ArtistInfoInlineBase(admin.StackedInline):
    form = ArtistInfoForm
    extra = 0

class ArtistEducationInline(ArtistInfoInlineBase):
    model = ArtistEducation
    

class ArtistSoloExhibInline(ArtistInfoInlineBase):
    model = ArtistSoloExhib

class ArtistGroupExhibInline(ArtistInfoInlineBase):
    model = ArtistGroupExhib

class ArtistCollectionInline(ArtistInfoInlineBase):
    model = ArtistCollection

class ArtistAwardInline(ArtistInfoInlineBase):
    model = ArtistAward

'''
class ArtistPressInline(admin.StackedInline):
    model = ArtistPress
'''

class ArtistNewsInline(admin.StackedInline):
    model = ArtistNews
    extra = 0


class ArtistPressReleaseInline(admin.StackedInline):
    model = ArtistPressRelease
    sortable_field_name = 'order'
    extra = 0

class ExhibitionReviewInline(admin.StackedInline):
    model = ExhibitionReview
    #sortable_field_name = 'order'
    extra = 0

class ExhibitionPressReleaseInline(admin.StackedInline):
    model = ExhibitionPressRelease
    sortable_field_name = 'order'
    extra = 0

class BaseAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]
    list_display = ('__unicode__', 'id', 'published',)
    list_editable = ('published',)
     

class ArtistAdmin(BaseAdmin):
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
    list_display = BaseAdmin.list_display + ('is_represented',)
    list_editable = ['published', 'is_represented']
    list_filter = ('is_represented', 'published',)
    inlines = [ArtistNewsInline, ArtistWorkInline, ArtistEducationInline, ArtistReviewInline, ArtistSoloExhibInline, ArtistGroupExhibInline, ArtistAwardInline, ArtistCollectionInline]

class ArtistWorkAdmin(BaseAdmin):
    search_fields = ['title', 'artist__name']
    list_display = BaseAdmin.list_display + ('code', 'category', 'year', 'is_selected', 'is_available', 'get_thumbnail')
    list_editable = ['published', 'category', 'is_selected', 'is_available']
    raw_id_fields = ('artist',)
    autocomplete_lookup_fields = {
        'fk': ['artist']
    }
    inlines = [ArtistWorkImageInline, VideoInline]
    list_filter = ('artist', 'exhibitionwork__exhibition', 'eventwork__event', 'category', 'published',)
    exclude = ('order',)

class EventAdmin(BaseAdmin):
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}
    list_display = BaseAdmin.list_display + ('date', 'time_from', 'time_to',)
    list_filter = ('featured_artists', 'published',)
    raw_id_fields = ('featured_artists',)
    inlines = [EventWorkInline, EventReviewInline]
    autocomplete_lookup_fields = {
        'm2m': ['featured_artists'],
    }    

class FrontPageItemAdmin(SortableAdmin):
    list_display = SortableAdmin.list_display + ('__unicode__',)
    list_display_links = ('__unicode__', )
    exclude = ('position',)
    raw_id_fields = ('exhibition', 'event',)
    autocomplete_lookup_fields = {
        'fk': ['event', 'exhibition']
    }

class SpaceImageAdmin(SortableAdmin):
    list_display = SortableAdmin.list_display + ('__unicode__',)
    list_display_links = ('__unicode__', )
    exclude = ('position',)

class SpaceVideoAdmin(SortableAdmin):
    list_display = SortableAdmin.list_display + ('__unicode__',)
    list_display_links = ('__unicode__', )
    exclude = ('position',)

class GalleryPersonAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]


class PublicationAdmin(BaseAdmin):
    search_fields = ['title', 'author', 'editor', 'publisher', 'isbn']
    list_filter = ('artist', 'exhibition', 'event', 'available', 'published',)

class ExhibitionAdmin(BaseAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    list_display = BaseAdmin.list_display + ('start_date', 'end_date',)
    list_filter = ('featured_artists',)
    raw_id_fields = ('featured_artists',)
    autocomplete_lookup_fields = {
        'm2m': ['featured_artists'],
    }    
    inlines = [ExhibitionWorkInline, ExhibitionReviewInline]

class ChunkAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]

class AboutReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(ArtistWork, ArtistWorkAdmin)
admin.site.register(FrontPageItem, FrontPageItemAdmin)
admin.site.register(SpaceImage, SpaceImageAdmin)
admin.site.register(SpaceVideo, SpaceVideoAdmin)
admin.site.register(GalleryPerson, GalleryPersonAdmin)
admin.site.unregister(Chunk)
admin.site.register(Chunk, ChunkAdmin)
admin.site.register(AboutReview, AboutReviewAdmin)
#admin.site.register(ArtistReview, BaseAdmin)

