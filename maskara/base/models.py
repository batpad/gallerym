from django.db import models
import datetime
from easy_thumbnails.files import get_thumbnailer
from django.core import serializers
import json

class BaseModel(models.Model):
    changed = models.DateTimeField(null=True, editable=False)
    created = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.changed = datetime.datetime.today()
        if self.created == None:
            self.created = self.changed
        super(BaseModel, self).save(*args, **kwargs)

    def get_dict(self):
        data = json.loads(serializers.serialize("json", [self]))
        fields = data[0]['fields']
        fields['id'] = data[0]['pk']
        return fields    

    def get_title(self):
        if hasattr(self, 'title'):
            return self.title
        elif hasattr(self, 'name'):
            return self.name
        else:
            return self.__unicode__()

    def get_image(self, options):
        if hasattr(self, 'image') and self.image:
            return get_thumbnailer(self.image.path).get_thumbnail(options).url    
        else:
            size = options['size']
            width = size[0]
            height = size[1] if len(size) > 1 else int(width * 0.75)
            return "http://placehold.it/%dx%d" % (width, height,)

    @property
    def class_name(self):
        return(self._meta.verbose_name)


    class Meta:
        abstract = True

