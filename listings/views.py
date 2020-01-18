from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices
# Create your views here.

from .models import Listing


def index(request):
    # Add the minus for descending
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    # gets all the lisitngs
    queryset_list = Listing.objects.order_by('-listDate')
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        # second check for empty string
        if keywords:
            # For checking if the word is there in the paragraph
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #City 
    if 'city' in request.GET:
        city = request.GET['city']
        # second check for empty string
        if city:
            # For checking if the word is there in the paragraph
            # I exact case insensitive
            queryset_list = queryset_list.filter(city__iexact=city)
    
    #State 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedRooms__lte=bedrooms)

    #Bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context ={
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'listings/search.html' ,context)
