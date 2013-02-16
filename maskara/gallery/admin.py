from django.contrib import admin
from models import *
from adminsortable.admin import SortableAdmin, SortableStackedInline


class ArtistWorkInline(SortableStackedInline):
    model = ArtistWork

class ArtistReviewInline(SortableStackedInline):
    model = ArtistReview

class ArtistPressReleaseInline(SortableStackedInline):
    model = ArtistPressRelease

class ExhibitionReviewInline(SortableStackedInline):
    model = ExhibitionReview

class ExhibitionPressReleaseInline(SortableStackedInline):
    model = ExhibitionPressRelease

class BaseAdmin(SortableAdmin):
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

