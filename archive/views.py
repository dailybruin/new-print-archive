from django.shortcuts import render
from django.db.models import F
from django.conf import settings

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from .models import ArchivePage

es = Elasticsearch(settings.ELASTIC_CONFIG['URL'])

def index(request):
    return render(request, 'archive/index.html')

def search(request):
    query = request.GET.get('search_text')

    if not query:
        return render(request, 'archive/search.html')

    s = Search(using=es, index=settings.ELASTIC_CONFIG['INDEX_NAME']) \
        .query("match", text=query)

    response = s.execute()
    print(response)
    #vector = SearchVector('tsv')
    #q = SearchQuery(query, config='english')
    #results = ArchivePage.objects.filter(tsv=query)[:10]
    #This is really really slow :(
    #results = ArchivePage.objects.annotate(rank=SearchRank(F('tsv'), q)).order_by('-rank')[:10]
    #print(results.query)
    context = {
        'results': response
    }
    return render(request, 'archive/search.html', context)

def slow_search(request):
    query = request.GET.get('search_text')
    #vector = SearchVector('tsv')
    #q = SearchQuery(query, config='english')
    #results = ArchivePage.objects.filter(tsv=query)[:10]
    #This is really really slow :(
    #results = ArchivePage.objects.annotate(rank=SearchRank(F('tsv'), q)).order_by('-rank')[:10]
    #print(results.query)
    #context = {
    #    'results': results
    #}
    #return render(request, 'archive/search.html', context)
