from domdom.apps.domapp.models import Categories
from domdom.apps.domapp.models import Products

def prodCount(razdelId, all=False):
    razdelId = int(razdelId)
    count = 0

    if(all):
        cats = allCats(razdelId, True)
        count = Products.objects.filter(enable=1, belon__in=cats).count()
    else:
        count += Products.objects.filter(enable=1, belon=razdelId).count()
    return count

def allProd(razdelId, all=False):
    razdelId = int(razdelId)
    if (all):
        cats = allCats(razdelId, True)
        prod = Products.objects.filter(enable=1, belon__in=cats)

    else:
        prod = Products.objects.filter(enable=1, belon=razdelId)

    return prod



def allCats(id, id_in = False):
    catsId = []
    try:
        id = int(id)
        subcats = Categories.objects.filter(belon=id, enable=1)
        if (subcats.count() > 0):
            i = 0
            for cats in subcats:
                catsId.append(cats.id)
                i += 1
            podcats = allCats(catsId)
            for podcat in podcats:
                catsId.append(podcat)
        if (id_in):
            catsId.append(id)
        return catsId

    except:
        try:
            catsId = []
            subcats = Categories.objects.filter(belon__in=id, enable=1)
            if (subcats.count()):
                i = 0
                for cats in subcats:
                    catsId.append(cats.id)
                    i += 1
                podcats = allCats(catsId)
                for podcat in podcats:
                    catsId.append(podcat)
            return catsId
        except:
            return catsId



def otherProd(product):
    cats = allCats(product.belon, True)
    prod = Products.objects.filter(enable=1, belon__in=cats).exclude(id=product.id)

    return prod

