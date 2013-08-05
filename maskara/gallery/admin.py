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
    inlines = [ArtistWorkInline, ArtistReviewInline, ArtistPressReleaseInline, ArtistEducationInline, ArtistSoloExhibInline, ArtistGroupExhibInline, ArtistCollectionInline, ArtistAwardInline, ArtistPressInline, ArtistNewsInline]

class ArtistWorkAdmin(admin.ModelAdmin):
    inlines = [ArtistWorkImageInline]
    list_filter = ('artist',)

class ExhibitionAdmin(ImageCroppingMixin, BaseAdmin):
    inlines = [ExhibitionReviewInline, ExhibitionPressReleaseInline]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Event, BaseAdmin)
admin.site.register(Publication, BaseAdmin)
admin.site.register(ArtistWork, ArtistWorkAdmin)
#admin.site.register(ArtistReview, BaseAdmin)

