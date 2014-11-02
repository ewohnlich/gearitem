from django.conf.urls import patterns, url
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import fetcher

# Register your models here.
from gearitem.models import GearItem, Gem, GearContext

class GearItemAdmin(admin.ModelAdmin):
    def get_urls(self):
      urls = super(GearItemAdmin, self).get_urls()
      my_urls = patterns('',
          (r'^populate_gear/$', self.populate_view),
          (r'^update_gear/$', self.update_view),
      )
      return my_urls + urls

    def populate_view(self, request):
      fetcher.fetch_items()
      return render(request, 'gearitem/done.html')

    def update_view(self, request):
      ids = GearItem.objects.all().values_list('id',flat=True)
      fetcher.fetch_items(ids)
      return render(request, 'gearitem/done.html')

admin.site.register(GearItem, GearItemAdmin)
admin.site.register(GearContext)
admin.site.register(Gem)