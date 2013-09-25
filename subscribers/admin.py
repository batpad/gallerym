from django.contrib import admin
from models import *

class SubscriberAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subscriber, SubscriberAdmin)