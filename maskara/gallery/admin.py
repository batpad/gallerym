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
    list_display = ('__unicode__', 'published',)
    list_editable = ('published',)
     

class ArtistAdmin(BaseAdmin):
    inlines = [ArtistWorkInline, ArtistReviewInline, ArtistPressReleaseInline]

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

