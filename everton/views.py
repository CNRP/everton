from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsPost
from .models import PlayerTransfers
from .models import Tag
from .models import Fixture
from analytics.models import ObjectViewed
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count

def index(request):
    news = NewsPost.objects.all().filter(visible='1')[:5]
    transfers = PlayerTransfers.objects.all().filter(visible='1')
    context = {
        'title': 'Homepage',
        'news' : news, 
        'transfers': transfers,
    }
    return render(request, 'pages/home.html', context)

def index2(request):
    news = NewsPost.objects.all().filter(visible='1')[:4]
    transfers = PlayerTransfers.objects.all().filter(visible='1').order_by('-date')[0:3]
    fixtures = Fixture.objects.all().filter(visible='1')
    tags = Tag.objects.all();

    transferIn = PlayerTransfers.objects.all().filter(visible='1').filter(type='1')
    transferOut = PlayerTransfers.objects.all().filter(visible='1').filter(type='2')
    loanIn = PlayerTransfers.objects.all().filter(visible='1').filter(type='3')
    loanOut = PlayerTransfers.objects.all().filter(visible='1').filter(type='4')
    inFA = PlayerTransfers.objects.all().filter(visible='1').filter(type='5')
    released = PlayerTransfers.objects.all().filter(visible='1').filter(type='6')

    context = {
        'title': 'Homepage',
        'news' : news, 
        'transfers': transfers,
        'fixtures': fixtures,
        'tags': tags,
        'transfers': transfers,
        'transferIn': transferIn,
        'transferOut': transferOut,
        'loanIn': loanIn,
        'loanOut': loanOut,
        'inFA': inFA,
        'released': released,
    }
    return render(request, 'pages/home2.html', context)

def transfers(request):
    transfers = PlayerTransfers.objects.all().filter(visible='1').order_by('-date')

    transferIn = PlayerTransfers.objects.all().filter(visible='1').filter(type='1')
    transferOut = PlayerTransfers.objects.all().filter(visible='1').filter(type='2')
    loanIn = PlayerTransfers.objects.all().filter(visible='1').filter(type='3')
    loanOut = PlayerTransfers.objects.all().filter(visible='1').filter(type='4')
    inFA = PlayerTransfers.objects.all().filter(visible='1').filter(type='5')
    released = PlayerTransfers.objects.all().filter(visible='1').filter(type='6')

    context = {
        'title': 'Transfers',
        'transfers': transfers,
        'transferIn': transferIn,
        'transferOut': transferOut,
        'loanIn': loanIn,
        'loanOut': loanOut,
        'inFA': inFA,
        'released': released,
    }
    return render(request, 'pages/transfers.html', context)

def fixtures(request):
    fixtures = Fixture.objects.all().filter(visible='1')
    context = {
        'title': 'Fixtures',
        'fixtures': fixtures,
    }
    return render(request, 'pages/fixtures.html', context)

def analytics(request):
    news = NewsPost.objects.all()
    objects = ObjectViewed.objects.all()
    q = NewsPost.objects.values('id').distinct()

    dict = {}
    newdict = {}
    
    values = ObjectViewed.objects.values('object_id').annotate(c=Count('ip_address', distinct=True)).order_by('-c') 

    for obj in values:
        dict[obj['object_id']] = obj['c']

    for key, value in dict.items():
        obj = NewsPost.objects.all().filter(id=key)
        newdict.update({str(obj[0]): value})

    totalclicks = sum(newdict.values())

    context = {
        'data': newdict,
        'news': news,
        'totalclicks': totalclicks,
        'title' : 'Anlytics',
    }
    return render(request, 'pages/analytics.html', context)