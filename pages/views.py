from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.

def index(request):
    # Gets only 3
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)[:3]
    context ={
        'listings': listings
    }
    return render(request,'pages/index.html',context)

def about(request):
     return render(request,'pages/about.html')


