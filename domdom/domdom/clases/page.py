from domdom.apps.domapp.models import Categories
from domdom.apps.domapp.config import functions
class Page:
    def __init__(self, obj, is_req=True):
        if is_req:

            self.name = obj.name
            self.title = obj.title
            self.description = obj.description
            self.h1 = obj.h1
            self.text = obj.text
            self.leftMenu = self.leftMenu()

    def leftMenu(self):

        try:
            cats = Categories.objects.filter(belon=0, enable=1)


            i=0
            for cat in cats:
                cats[i].prod = functions.allProd(cat.id, True)

                cats[i].child = Categories.objects.filter(belon=cat.id, enable=1)
                ii = 0
                for podcat in cats[i].child:
                    try:
                        cats[i].child[ii].prod = functions.allProd(podcat.id, True)
                        cats[i].child[ii].twochild = Categories.objects.filter(belon=podcat.id, enable=1)
                        ii += 1
                    except:
                        continue
                i += 1

            return cats
        except:
            pass