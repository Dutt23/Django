from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices,price_choices,bedroom_choices

# Create your views here.

def index(request):
    # Gets only 3
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)[:3]
    context ={
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    # Get all Realtors
     realtors = Realtor.objects.order_by('-hireDate')
    #  get MVP
     mvp_realtors = filter(lambda x: x.isMvp == True ,realtors ) 
     context = {
        'realtors' :  realtors,
        'mvp_realtors': mvp_realtors
     }
     return render(request,'pages/about.html',context)


