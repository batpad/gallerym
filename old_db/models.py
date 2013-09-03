# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AddressBook(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=45)
    mname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    postcode = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    mphone = models.CharField(max_length=60)
    dphone = models.CharField(max_length=60)
    fax = models.CharField(max_length=60)
    class Meta:
        db_table = u'address_book'

class Artists(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=90)
    image = models.CharField(max_length=75)
    copy_text = models.TextField()
    url = models.CharField(max_length=150)
    is_gm_artist = models.IntegerField()
    publish = models.IntegerField()
    ex_id = models.IntegerField()
    class Meta:
        db_table = u'artists'

class Bios(models.Model):
    id = models.IntegerField(primary_key=True)
    artist_id = models.IntegerField()
    birth = models.CharField(max_length=150)
    edu = models.TextField()
    solo = models.TextField()
    grp = models.TextField()
    awards = models.TextField()
    coll = models.TextField()
    pdf = models.CharField(max_length=75)
    publish = models.IntegerField()
    class Meta:
        db_table = u'bios'

class ContactDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    address1 = models.TextField()
    address2 = models.TextField()
    timing = models.CharField(max_length=765)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=90)
    fax = models.CharField(max_length=90)
    floor_image = models.CharField(max_length=90)
    floor_pdf = models.CharField(max_length=90)
    map_image = models.CharField(max_length=90)
    map_pdf = models.CharField(max_length=90)
    class Meta:
        db_table = u'contact_details'

class EvDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    date1 = models.IntegerField()
    date2 = models.IntegerField()
    time1 = models.CharField(max_length=60)
    time2 = models.CharField(max_length=60)
    artist = models.CharField(max_length=180)
    image = models.CharField(max_length=180)
    copy_text = models.TextField()
    pdf = models.CharField(max_length=75)
    publish = models.IntegerField()
    class Meta:
        db_table = u'ev_details'

class ExArtists(models.Model):
    id = models.IntegerField(primary_key=True)
    artist_id = models.IntegerField()
    ex_id = models.IntegerField()
    class Meta:
        db_table = u'ex_artists'

class ExDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    date1 = models.IntegerField()
    date2 = models.IntegerField()
    date3 = models.IntegerField()
    image = models.CharField(max_length=75)
    publish = models.IntegerField()
    class Meta:
        db_table = u'ex_details'

class Gen(models.Model):
    id = models.IntegerField(primary_key=True)
    a_cat_browsing = models.IntegerField()
    ex_cat_browsing = models.IntegerField()
    ex_auto_publish = models.IntegerField()
    ev_auto_publish = models.IntegerField()
    current_ex_id = models.IntegerField()
    current_ev_id = models.IntegerField()
    color1 = models.CharField(max_length=30)
    color2 = models.CharField(max_length=30)
    logo_id = models.IntegerField()
    default_staff_id = models.IntegerField()
    mailing_list = models.TextField()
    why_register = models.TextField()
    class Meta:
        db_table = u'gen'

class Pages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    copy_text = models.TextField()
    class Meta:
        db_table = u'pages'

class Press(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    date = models.IntegerField()
    image = models.CharField(max_length=300)
    copy_text = models.TextField()
    url = models.CharField(max_length=150)
    pdf = models.CharField(max_length=120)
    publish = models.IntegerField()
    type = models.CharField(max_length=75)
    type_id = models.IntegerField()
    class Meta:
        db_table = u'press'

class Previews(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=75)
    comment = models.CharField(max_length=765)
    publish = models.IntegerField()
    type = models.CharField(max_length=75)
    type_id = models.IntegerField()
    class Meta:
        db_table = u'previews'

class Pubs(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=90)
    editor = models.CharField(max_length=90)
    publisher = models.CharField(max_length=765)
    isbn = models.CharField(max_length=90)
    image = models.CharField(max_length=90)
    pdf = models.CharField(max_length=90)
    availability = models.IntegerField()
    publish = models.IntegerField()
    type = models.CharField(max_length=75)
    type_id = models.IntegerField()
    class Meta:
        db_table = u'pubs'

class Reviews(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=90)
    source = models.CharField(max_length=765)
    translated_by = models.CharField(max_length=300)
    date = models.IntegerField()
    copy_text = models.TextField()
    url = models.CharField(max_length=300)
    pdf = models.CharField(max_length=75)
    publish = models.IntegerField()
    type = models.CharField(max_length=75)
    type_id = models.IntegerField()
    class Meta:
        db_table = u'reviews'

class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=105)
    image = models.CharField(max_length=75)
    copy_text = models.TextField()
    publish = models.IntegerField()
    class Meta:
        db_table = u'staff'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=60)
    pwd = models.CharField(max_length=60)
    class Meta:
        db_table = u'users'

class Work(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=75)
    cat = models.CharField(max_length=45)
    code = models.CharField(max_length=30)
    size = models.CharField(max_length=765)
    material = models.CharField(max_length=765)
    yr = models.CharField(max_length=12)
    theme = models.TextField()
    attribution = models.CharField(max_length=765)
    availability = models.IntegerField()
    price = models.CharField(max_length=30)
    artist_id = models.IntegerField()
    publish = models.IntegerField()
    ex_id = models.IntegerField()
    class Meta:
        db_table = u'work'

