from django.contrib import admin
from domdom.apps.domapp.models import StaticPage
from domdom.apps.domapp.models import Categories
from domdom.apps.domapp.models import Products

# Register your models here.

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(StaticPage)
