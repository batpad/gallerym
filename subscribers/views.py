from django.shortcuts import render
from models import Subscriber
from forms import SubscriberForm
from django.http import HttpResponse, HttpResponseRedirect
import helpers

def subscribe(request):
    errors = None
    if request.POST:
        d = request.POST
        subscriber_data = {
            'first_name': d['firstName'],
            'last_name': d['lastName'],
            'email': d['email'],
            'tel_no': d['tel'],
            'cell_no': d['cell'],
            'address': d['address'],
            'street': d['street'],
            'city': d['city'],
            'zip_code': d['zip'],
            'state': d['state'],
            'country': d['country'],
            'role': d['role']
        }
        subscriber_form = SubscriberForm(subscriber_data)
        #import pdb;pdb.set_trace()
        if subscriber_form.is_valid():
            subscriber_form.save()
            helpers.send_ack_email(subscriber_data)
            helpers.send_admin_email(subscriber_data)
            return HttpResponseRedirect("/subscribe_thanks")
        else:
            errors = subscriber_form.errors
            #return render(request, "subscribe.html", {'form': subscriber_form})

    return render(request, "subscribe.html", {'errors': errors})

def subscribe_thanks(request):
    return render(request, "subscribe_thanks.html")