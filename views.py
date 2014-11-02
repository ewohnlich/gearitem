from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views import generic
from tools import slots

from models import GearItem

class IndexView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    paginate_by = 50

    def get_queryset(self):
      """ Returns gear sorted by name """
      return GearItem.objects.order_by('name')

class IlvlSortView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    paginate_by = 50

    def get_queryset(self):
      """ Returns gear sorted by name """
      itms = GearItem.objects.annotate(max_ilvl=models.Max('ilvl')).order_by('-max_ilvl')
      return itms
      #GearItem.objects.aggregate(models.Max('ilvl'))['ilvl__max']

class SlotView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    paginate_by = 50

    def get_queryset(self):
      """ Returns gear sorted by name """
      return GearItem.objects.order_by('name').filter(slot=int(self.kwargs['slot']))

    def slotName(self):
      return slots[int(self.kwargs['slot'])]

class ZoneView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    paginate_by = 50

    def get_queryset(self):
      """ Returns gear sorted by name """
      return GearItem.objects.order_by('name').filter(zone=self.kwargs['zone'])

class DetailsView(generic.DetailView):
    model = GearItem
    template_name = 'gearitem/details.html'

    def slotName(self):
      return slots[self.slot]