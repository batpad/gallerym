from django.contrib import admin
from models import *
# from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
#from adminsortable.admin import SortableAdmin, admin.StackedInline
from image_cropping import ImageCroppingMixin

class ArtistWorkImageInline(admin.StackedInline):
    model = ArtistWorkImage
    sortable_field_name = 'order'
    extra = 0

class ArtistWorkInline(admin.StackedInline):
    model = ArtistWork
    sortable_field_name = 'order'


class ArtistReviewInline(admin.StackedInline):
    model = ArtistReview
    inlines = []
    sortable_field_name = 'order'

    

class ArtistEducationInline(admin.StackedInline):
    model = ArtistEducation

class ArtistSoloExhibInline(admin.StackedInline):
    model = ArtistSoloExhib

class ArtistGroupExhibInline(admin.StackedInline):
    model = ArtistGroupExhib

class ArtistCollectionInline(admin.StackedInline):
    model = ArtistCollection

class ArtistAwardInline(admin.StackedInline):
    model = ArtistAward

class ArtistPressInline(admin.StackedInline):
    model = ArtistPress

class ArtistNewsInline(admin.StackedInline):
    model = ArtistNews



class ArtistPressReleaseInline(admin.StackedInline):
    model = ArtistPressRelease
    sortable_field_name = 'order'

class ExhibitionReviewInline(admin.StackedInline):
    model = ExhibitionReview
    sortable_field_name = 'order'

class ExhibitionPressReleaseInline(admin.StackedInline):
    model = ExhibitionPressRelease
    sortable_field_name = 'order'

class BaseAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]
    list_display = ('__unicode__', 'published',)
    list_editable = ('published',)
     

class ArtistAdmin(BaseAdmin):
    search_fields = ['name']
    list_filter = ('is_represented', 'published',)
    inlines = [ArtistWorkInline, ArtistEducationInline, ArtistReviewInline, ArtistSoloExhibInline, ArtistGroupExhibInline, ArtistAwardInline, ArtistCollectionInline, ArtistPressReleaseInline, ArtistPressInline, ArtistNewsInline]

class ArtistWorkAdmin(BaseAdmin):
    search_fields = ['title', 'artist__name']
    raw_id_fields = ('artist',)
    autocomplete_lookup_fields = {
        'fk': ['artist']
    }
    inlines = [ArtistWorkImageInline]
    list_filter = ('artist', 'published',)
    exclude = ('order',)

class EventAdmin(BaseAdmin):
    search_fields = ['title'] 
    list_filter = ('featured_artists', 'published',)
    raw_id_fields = ('featured_artists',)
    autocomplete_lookup_fields = {
        'm2m': ['featured_artists']
    }    

class PublicationAdmin(BaseAdmin):
    search_fields = ['title', 'author', 'editor', 'publisher', 'isbn']
    list_filter = ('artist', 'exhibition', 'event', 'available', 'published',)

class ExhibitionAdmin(BaseAdmin):
    search_fields = ['title', 'description']
    list_filter = ('featured_artists',)
    raw_id_fields = ('featured_artists', 'featured_work',)
    autocomplete_lookup_fields = {
        'm2m': ['featured_artists', 'featured_work'],
    }    
    inlines = [ExhibitionReviewInline, ExhibitionPressReleaseInline]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(ArtistWork, ArtistWorkAdmin)
#admin.site.register(ArtistReview, BaseAdmin)

