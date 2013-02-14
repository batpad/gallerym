from django.db import models
import datetime

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

    def get_title(self):
        if hasattr(self, 'title'):
            return self.title
        elif hasattr(self, 'name'):
            return self.name
        else:
            return self.__unicode__()

    class Meta:
        abstract = True

