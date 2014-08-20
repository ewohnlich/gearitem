from django.conf.urls import patterns, url
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import fetcher

# Register your models here.
from gearitem.models import GearItem

class GearItemAdmin(admin.ModelAdmin):
    def get_urls(self):
      urls = super(GearItemAdmin, self).get_urls()
      my_urls = patterns('',
          (r'^populate_gear/$', self.populate_view),
          (r'^update_gear/$', self.update_view),
      )
      return my_urls + urls

    def update_view(self,request):
      ids = []
      for obj in GearItem.objects.all():
        ids.append(obj.id)
      for data in fetcher.fetch_items(ids):
        self.update_gear(data)
      return render(request, 'gearitem/done.html')

    def populate_view(self, request):
      for data in fetcher.fetch_items():
        try:
          GearItem.objects.get(id=data['id'])
        except ObjectDoesNotExist:
          GearItem.objects.create(id=data['id'])
        self.update_gear(data)
      return render(request, 'gearitem/done.html')

    def update_gear(self, gear):
      obj = GearItem.objects.get(id=gear['id'])
      obj.name = gear['name']
      obj.nameDescription = gear['desc']
      obj.agility = gear['stats'].get('agility',0)
      obj.crit = gear['stats'].get('crit',0)
      obj.haste = gear['stats'].get('haste',0)
      obj.mastery = gear['stats'].get('mastery',0)
      obj.versatility = gear['stats'].get('versatility',0)
      obj.multistrike = gear['stats'].get('multistrike',0)
      if gear.get('sockets'):
        obj.socket1 = gear['sockets']['sockets'][0]['type']
        obj.socket2 = len(gear['sockets']['sockets']) > 1 and gear['sockets']['sockets'][1]['type']
        obj.socket3 = len(gear['sockets']['sockets']) > 2 and gear['sockets']['sockets'][2]['type']
        obj.socket_bonus = gear['sockets']['socketBonus'].replace('+','')
      obj.icon = gear['icon']
      obj.slot = gear['slot']
      obj.quality = gear['quality']
      obj.save()

admin.site.register(GearItem, GearItemAdmin)