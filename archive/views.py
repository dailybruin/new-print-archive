from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import F

from .models import ArchivePage

# Create your views here.
def index(request):
    return render(request, 'archive/index.html')

def searchbydate(request):
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
