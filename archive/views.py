from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import F

from .models import ArchivePage


def index(request):

    return render(request, 'archive/index.html')

def getYear(request, year):
        
    if(int(year) == 2010):
        returned_years = {'2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'}
        
 
    return render(request, 'archive/overlay.html', {'returned_years': returned_years})

# Called when user clicks on a date
def searchbydate(request):
    #need to search google drive for jpgs in selected date folder
    return render(request, 'archive/searchbydate.html')

def search(request):
    query = request.GET.get('search_text')
    #vector = SearchVector('tsv')
    q = SearchQuery(query, config='english')
    results = ArchivePage.objects.filter(tsv=query)[:10]
    #This is really really slow :(
    #results = ArchivePage.objects.annotate(rank=SearchRank(F('tsv'), q)).order_by('-rank')[:10]
    #print(results.query)
    context = {
        'results': results
    }
    return render(request, 'archive/search.html', context)

def slow_search(request):
    query = request.GET.get('search_text')
    #vector = SearchVector('tsv')
    q = SearchQuery(query, config='english')
    #results = ArchivePage.objects.filter(tsv=query)[:10]
    #This is really really slow :(
    results = ArchivePage.objects.annotate(rank=SearchRank(F('tsv'), q)).order_by('-rank')[:10]
    #print(results.query)
    context = {
        'results': results
    }
    return render(request, 'archive/search.html', context)
