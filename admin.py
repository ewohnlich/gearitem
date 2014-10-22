from django.conf.urls import patterns, url
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import fetcher

# Register your models here.
from gearitem.models import GearItem, Gem

class GearItemAdmin(admin.ModelAdmin):
    def get_urls(self):
      urls = super(GearItemAdmin, self).get_urls()
      my_urls = patterns('',
          (r'^populate_gear/$', self.populate_view),
          (r'^update_gear/$', self.update_view),
      )
      return my_urls + urls

    def update_view(self,request):
      ids = GearItem.objects.values_list('id',flat=True)
      for data in fetcher.fetch_items(ids):
        if data: # might be null if it can't find the id - like new items
          self.update_gear(data)
      return render(request, 'gearitem/done.html')

    def populate_view(self, request):
      for data in fetcher.fetch_items():
        print 'Populating item: %d' % data['id']
        try:
          GearItem.objects.get(id=data['id'])
        except ObjectDoesNotExist:
          GearItem.objects.create(id=data['id'])
        self.update_gear(data)
      return render(request, 'gearitem/done.html')

    def update_gear(self, gear):
      print 'Updating item: %d' % gear['id']
      obj = GearItem.objects.get(id=gear['id'])
      if obj.name != gear['name']:
        print 'Warning: %d renamed from %s to %s' % (gear['id'],obj.name,gear['name'])
      obj.name = gear['name']
      obj.nameDescription = gear['desc']
      obj.agility = gear['stats'].get('agility',0)
      obj.crit = gear['stats'].get('crit',0)
      obj.haste = gear['stats'].get('haste',0)
      obj.mastery = gear['stats'].get('mastery',0)
      obj.versatility = gear['stats'].get('versatility',0)
      obj.multistrike = gear['stats'].get('multistrike',0)
      obj.weapon_min = gear.get('weapon_min',0)
      obj.weapon_max = gear.get('weapon_max',0)
      obj.weapon_speed = gear.get('weapon_speed',0)
      if gear.get('sockets'):
        obj.socket1 = gear['sockets']['sockets'][0]['type'].lower() or 'none'
        obj.socket2 = len(gear['sockets']['sockets']) > 1 and gear['sockets']['sockets'][1]['type'].lower() or 'none'
        obj.socket3 = len(gear['sockets']['sockets']) > 2 and gear['sockets']['sockets'][2]['type'].lower() or 'none'
        obj.socket_bonus = gear['sockets']['socketBonus'].replace('+','') or ''
      obj.icon = gear['icon']
      obj.ilvl = gear['ilvl']
      obj.slot = gear['slot']
      obj.quality = gear['quality']
      obj.save()

admin.site.register(GearItem, GearItemAdmin)
admin.site.register(Gem)