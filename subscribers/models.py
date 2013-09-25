from django.db import models
from maskara.base.models import BaseModel

class Subscriber(BaseModel):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512, blank=True)
    email = models.EmailField()
    tel_no = models.CharField(max_length=512, blank=True)
    cell_no = models.CharField(max_length=512, blank=True)
    address = models.CharField(max_length=1024, blank=True)
    street = models.CharField(max_length=512, blank=True)
    city = models.CharField(max_length=256, blank=True)
    zip_code = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256)
    role = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name,)    

