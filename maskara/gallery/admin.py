from django.contrib import admin
from models import *
#from adminsortable.admin import SortableAdmin, admin.StackedInline


class ArtistWorkInline(admin.StackedInline):
    model = ArtistWork
    sortable_field_name = 'order'

class ArtistReviewInline(admin.StackedInline):
    model = ArtistReview
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


class ExhibitionAdmin(BaseAdmin):
    inlines = [ExhibitionReviewInline, ExhibitionPressReleaseInline]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Event, BaseAdmin)
admin.site.register(Publication, BaseAdmin)
#admin.site.register(ArtistReview, BaseAdmin)

