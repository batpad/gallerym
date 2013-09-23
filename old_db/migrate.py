from maskara.gallery import models as new_models
import models as old_models
from django.template.defaultfilters import slugify as django_slugify, linebreaks
import datetime
import codecs
import os
from os.path import join
from shutil import copyfile
from maskara.settings import MEDIA_ROOT
#from datetime.datetime import fromtimestamp
ERRORS = []
OLD_ASSETS_PATH = '/var/www/gallerymaskara.com/site/'

def slugify(txt, id=""):
    old_id = str(id)
    txt = txt[0:32]
    if old_id != '':
        txt = txt + "-" + old_id
    if txt == '':
        txt = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(15)])
    return django_slugify(txt.strip())

def get_asset(filename, new_path):
    new_path = join('Old Site', new_path)
    if filename.endswith("pdf"):
        old_path = join(OLD_ASSETS_PATH, "pdf")
    else:
        old_path = join(OLD_ASSETS_PATH, "assets")
    src = join(old_path, filename)
    if not os.path.exists(src):
        ERRORS.append("FILE NOT FOUND: " + src + "\n\n")
        return ''    
    dst = join(MEDIA_ROOT, 'files', new_path, filename)
    copyfile(src, dst)
    return join('files', new_path, filename)

def import_artists():
    for o in old_models.Artists.objects.using('old').all():
        data = {
            'old_id': o.id,
            'name': o.title,
            'image': get_asset(o.image, 'old_artist_images') if o.image != '' else '',
            'slug': slugify(o.title, o.id),
            'bio': linebreaks(o.copy_text),
            'is_represented': True if o.is_gm_artist == 1 else False,
            'published': True if o.publish == 1 else False
        }
        a = new_models.Artist(**data)
        a.save()
        print str(a.id) + ": " + a.slug

def import_bios():
    for o in old_models.Bios.objects.using('old').all():
        try:
            artist = new_models.Artist.objects.get(old_id = o.artist_id)
        except:
            error = "Artist Bio Error for id %d\n\n" % o.artist_id
            ERRORS.append(error)
            continue
        artist.birth_location = o.birth
        artist.bio_pdf = get_asset(o.pdf, 'artist_bio_pdfs') if o.pdf != '' else ''
        artist.save()
        add_artist_data(artist, new_models.ArtistEducation, get_artist_data(o.edu))
        add_artist_data(artist, new_models.ArtistSoloExhib, get_artist_data(o.solo))
        add_artist_data(artist, new_models.ArtistGroupExhib, get_artist_data(o.grp))
        add_artist_data(artist, new_models.ArtistAward, get_artist_data(o.awards))
        add_artist_data(artist, new_models.ArtistCollection, get_artist_data(o.coll))
        

def import_artist_works():
    for o in old_models.Work.objects.using('old').all():
        try:
            artist = new_models.Artist.objects.get(old_id=o.artist_id)
        except:
            error = "ARTIST WORK ERROR:\nold work id: %d, artist_id = %d, work title: %s\n\n" % (o.id, o.artist_id, o.title,) 
            ERRORS.append(error)
            print "ERROR: " + str(o.artist_id)
            continue
        data = {
            'artist': artist,
            'old_id': o.id,
            'title': o.title,
            'image': get_asset(o.image, 'old_artist_work_images') if o.image != '' else '',
            'category': o.cat,
            'code': o.code,
            'size_text': o.size,
            'material': o.material,
            'year': getYear(o.yr),
            'theme': linebreaks(o.theme),
            'attribution': linebreaks(o.attribution),
            'price': o.price,
            'published': True if o.publish == 1 else False
        }
        w = new_models.ArtistWork(**data)
        w.save()
        if o.ex_id and o.ex_id != 0:
            exhib = new_models.Exhibition.objects.get(old_id=o.ex_id)
            exhib_work = new_models.ExhibitionWork(exhibition=exhib, work=w)
            exhib_work.save()
            #exhib.featured_work.add(w)

        print str(w.id) + ": " + w.title


def getYear(yr):
    try:
        year = int(yr)
    except:
        year = None
    return year

def import_exhibitions():
    for o in old_models.ExDetails.objects.using('old').all():
        fromtimestamp = datetime.datetime.fromtimestamp
        data = {
            'old_id': o.id,
            'title': o.title,
            'slug': slugify(o.title),
            'start_date': fromtimestamp(o.date1),
            'end_date': fromtimestamp(o.date2),
            'autopublish_date': fromtimestamp(o.date3),
            'published': True if o.publish == 1 else False        
        }
        ex = new_models.Exhibition(**data)
        ex.save()
        print str(ex.id) +  ": " + ex.title

def import_exhibition_artists():
    for o in old_models.ExArtists.objects.using('old').all():
        try:
            artist = new_models.Artist.objects.get(old_id=o.artist_id)
            exhibition = new_models.Exhibition.objects.get(old_id=o.ex_id)
        except:
            error = "ExArtist Error:\n artist old id: %d, ex old id: %d\n\n" % (o.artist_id, o.ex_id,)
            ERRORS.append(error)    
            continue
        exhibition.featured_artists.add(artist) 

def delete_all():
    n = new_models
    classes = [n.Artist, n.ArtistWork, n.Exhibition, n.Event, n.Publication]
    for c in classes:
        for obj in c.objects.all():
            obj.delete()    

def import_events():
    fromtimestamp = datetime.datetime.fromtimestamp
    for o in old_models.EvDetails.objects.using('old').all():
        data = {
            'old_id': o.id,
            'title': o.title,
            'slug': slugify(o.title),
            'pdf': get_asset(o.pdf, 'event_pdfs') if o.pdf != '' else '',
            'date': fromtimestamp(o.date1),
            'time_from': get_time_from_string(o.time1),
            'time_to': get_time_from_string(o.time2),
            'description': linebreaks(o.copy_text),
            'published': True if o.publish == 1 else False
        }
        ev = new_models.Event(**data)
        ev.save()
        print str(ev.id) + ": " + ev.title

def import_press():
    fromtimestamp = datetime.datetime.fromtimestamp
    for o in old_models.Press.objects.using('old').all():
        if o.type == 'gm_exhibition':
            obj = new_models.ExhibitionPressRelease()
            obj.exhibition = new_models.Exhibition.objects.get(old_id = o.type_id)
        elif o.type == 'gm_artist':
            obj = new_models.ArtistPressRelease()
            obj.artist = new_models.Artist.objects.get(old_id = o.type_id)
        obj.title = o.title
        obj.author = o.author
        obj.publisher = o.publisher
        obj.pdf = get_asset(o.pdf, "press_pdfs") if o.pdf != '' else ''
        obj.date = fromtimestamp(o.date)
        obj.description = linebreaks(o.copy_text)
        obj.url = o.url
        if o.publish == 1:
            obj.published = True
        else:
            obj.published = False
        obj.save()    

def import_reviews():
    fromtimestamp = datetime.datetime.fromtimestamp
    for o in old_models.Reviews.objects.using('old').all():
        if o.type == 'gm_exhibition':
            obj = new_models.ExhibitionReview()
            obj.exhibition = new_models.Exhibition.objects.get(old_id = o.type_id)
        elif o.type == 'gm_artist':
            obj = new_models.ArtistReview()
            obj.artist = new_models.Artist.objects.get(old_id = o.type_id)
        else:
            continue
        obj.title = o.title
        obj.author = o.author
        obj.source = o.source
        obj.pdf = get_asset(o.pdf, "review_pdfs") if o.pdf else ''
        obj.translated_by = o.translated_by
        obj.date = fromtimestamp(o.date)
        obj.description = linebreaks(o.copy_text)
        obj.url = o.url
        if o.publish == 1:
            obj.published = True
        else:
            obj.published = False                 
        obj.save()

def import_publications():
    for o in old_models.Pubs.objects.using('old').all():
        data = {
            'old_id': o.id,
            'title': o.title,
            'author': o.author,
            'editor': o.editor,
            'pdf': get_asset(o.pdf, 'publication_pdfs') if o.pdf != '' else '',
            'publisher': o.publisher,
            'isbn': o.isbn,
            'available': True if o.availability == 1 else False,
            'published': True if o.publish == 1 else False,
        }
        p = new_models.Publication(**data)
        p.save()
        print str(p.id) + ": " + p.title

def get_time_from_string(s):
    parts = s.split(":")
    hours = int(parts[0])
    ampm = parts[1][-2:].lower()
    if ampm != 'pm' and ampm != 'am':
        ampm = 'pm'
    if ampm == 'pm':
        hours = hours + 12
    if hours == 24:
        hours = 12
    minutes = int(parts[1][:2])
    return datetime.time(hours, minutes)

def get_artist_data(s):
    ret = []
    s = s.strip().replace("\r\n", "\n").replace("\r", "\n")
    lines = s.split("\n")
    year = None
    for line in lines:
        if len(line.strip()) == 4:
            try:
                y = int(line)
                if (y > 1900 and y < 2050):
                    year = int(line)
                    continue
            except:
                pass
        try:
            year = int(line[0:4])
        except:
            try:
                year = int(line[-4:])
            except:
                pass
        if not year or year < 1900 or year > 2050:
            error = "Invalid artist data: %s\n\n" % line
            ERRORS.append(error)
            continue
        text = line.replace(str(year), '').strip()
        text = text.replace('\\"', '"')
        bad_starts = [',', '-', '.']
        for bad_start in bad_starts:
            if text.startswith(bad_start):
                text = text[1:].strip()
        if text == '':
            continue
        ret.append({
            'year': year,
            'text': text
        })
    '''
    for y in year_chunks:
        lines = y.split("\n")
        try:
            year = int(lines[0].strip())
        except:
            error = "Invalid Artist Data: %s" % s
            print error
            ERRORS.append(error)
            continue
        for line in lines[1:]:
            d = {
                'year': year,
                'text': line 
            }
            ret.append(d)
    '''
    return ret

def add_artist_data(artist, cls, data):
    for d in data:
        d['artist'] = artist
        obj = cls(**d)
        obj.save()


def import_all():
    functions = [import_artists, import_exhibitions, import_events, import_publications, import_artist_works, import_exhibition_artists, import_press, import_reviews, import_bios]
    for f in functions:
        f()
    errors_file = codecs.open("import_errors.txt", encoding="utf-8", mode="w")
    for e in ERRORS:
        print e
        errors_file.write(e)
    errors_file.close()
 
