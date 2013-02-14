from django.contrib import admin
from models import *


class ArtistWorkInline(admin.StackedInline):
    model = ArtistWork

class ArtistReviewInline(admin.StackedInline):
    model = ArtistReview

class ArtistPressReleaseInline(admin.StackedInline):
    model = ArtistPressRelease

class ExhibitionReviewInline(admin.StackedInline):
    model = ExhibitionReview

class ExhibitionPressReleaseInline(admin.StackedInline):
    model = ExhibitionPressRelease

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
