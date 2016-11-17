from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import F

from .models import ArchivePage


def index(request):

    return render(request, 'archive/index.html')

def getYear(request, decade):
     
    i=0
    returned_years = []
    decade = int(decade)
    print (decade)
    if decade != 2010:
        while(i<10):
            returned_years.append(decade+i)
            print (decade+i)
            i+=1
    else:
        while(i<7):
            returned_years.append(decade+i)
            print (decade+i)
            i+=1   
    
    return render(request, 'archive/overlay.html', {'returned_years': returned_years, 'decade': decade})

def getMonths(request, decade,year):
    print (decade, year)
    return render(request, 'archive/overlaymonths.html', {'decade':decade, 'year':year} )

def getDays(request, decade, year, month):
    print (decade, year, month)
    thirtyone_days = [1,3,5,7,8,10,12]
    thirty_days = [4,6,9,11]
    days = []
    if month in thirtyone_days:
        i=0
        while(i<=31):
            days.append(i)
    elif month in thirty_days:
        i=0
        while(i<=30):
            days.append(i)
    else: #feb
        i=0
        while(i<=28):
            days.append(i)

    print (days)

    return render(request, 'archive/overlaydays.html', {'decade':decade, 'year':year, 'month': month, 'days': days})

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
