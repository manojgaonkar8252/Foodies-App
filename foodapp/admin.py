from django.contrib import admin

from foodapp.models import Restaurant, Item, Menu

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
