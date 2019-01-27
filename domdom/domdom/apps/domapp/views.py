from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from domdom.apps.domapp.config import functions
from domdom.clases.page import Page
from domdom.clases.pagination import Pagination
from bs4 import BeautifulSoup
import requests
# База данных
from domdom.apps.domapp.models import StaticPage
from domdom.apps.domapp.models import Categories
from domdom.apps.domapp.models import Products
# Create your views here.

def robots(request):

    return render(request, 'robots.txt', None, content_type="text/plain")

def index(request):
    obj = StaticPage.objects.get(id=2)
    page = Page(obj)
    context = {
        'page': page
    }
    return render(request, 'base/index.html', context)

def catalog(request):

    razdel = StaticPage.objects.get(id=1)
    page = Page(razdel)
    categories = Categories.objects.filter(belon=0, enable=1)
    i = 0
    for category in categories:
        subcats = Categories.objects.filter(belon=category.id, enable=1)
        prodCount = functions.prodCount(category.id, True)
        categories[i].subcats = subcats
        categories[i].prodCount = prodCount

        i +=1

    context = {
        'page': page,
        'categories': categories,
    }

    return render(request, 'category/catalog.html', context)

def alt_url(request, index):

    try:
        razdel = Categories.objects.get(url=index, enable=1)
        if (razdel.belon == 0):
            ret = category(request, index, razdel)
        elif razdel.belon > 0:
            ret = podcategory(request, index, razdel)

    except:
        try:
            product = Products.objects.get(url=index, enable=1)

            ret = products(request, index, product)

        except:

            HttpResponse.status_code
            return render(request, '404.html', status=404)


    return ret

def category(request, index, razdel="N"):
    page = Page(razdel)

    razdel.podrazdel = Categories.objects.filter(belon=razdel.id, enable=1)
    i = 0

    for podrazdels in razdel.podrazdel:
        prod = functions.allProd(podrazdels.id, True)[:4]
        cats = Categories.objects.filter(belon=podrazdels.id, enable=1)
        razdel.podrazdel[i].prod = prod
        razdel.podrazdel[i].prod.all = functions.prodCount(podrazdels.id, True)

        razdel.podrazdel[i].cats = cats
        ii = 0
        for podpodcats in razdel.podrazdel[i].cats:
            razdel.podrazdel[i].cats[ii].prodall = functions.prodCount(podpodcats.id, True)
            ii += 1
        i += 1

    context = {
        'page': page,
        'razdel': razdel,
    }
    return render(request, 'category/category.html', context)

def podcategory(request, index, razdel="N"):

    try:
        pagenav = int(request.GET["page"])
    except:
        pagenav = 1
    print(pagenav)
    page = Page(razdel)
    count = functions.prodCount(razdel.id, True)
    perPage = 2
    pagin = Pagination(count, pagenav, n=perPage, n_pag=3)
    if pagenav > pagin.endPage(count, perPage) or pagenav < 1:
        return render(request, '404.html', status=404)


    page.pagin = pagin.design

    razdel.podrazdel = Categories.objects.filter(belon=razdel.id, enable=1)
    i = 0
    razdel.prod = functions.allProd(razdel.id, True)[pagin.sort[0]-1:pagin.sort[0]+1]

    for podrazdels in razdel.podrazdel:
        razdel.podrazdel[i].prodall = functions.prodCount(podrazdels.id, True)
        i += 1

    context = {
        'page': page,
        'razdel': razdel,
        'leftMenuHidden': 'hidden',

    }
    return render(request, 'category/podcategory.html', context)

def products(request, index, product="N"):
    page = Page(product)
    other_prod = functions.otherProd(product)
    context = {
        'page': page,
        'other_prod': other_prod,
        'leftMenuHidden': 'hidden',

    }
    return render(request, 'products/products.html', context)


