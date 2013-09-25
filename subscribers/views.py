from django.shortcuts import render
from models import Subscriber
from forms import SubscriberForm
from django.http import HttpResponse


def subscribe(request):
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
            return HttpResponse("saved")
        else:
            return HttpResponse("error")
            #return render(request, "subscribe.html", {'form': subscriber_form})

    return render(request, "subscribe.html")
