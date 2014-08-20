from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views import generic
from tools import slots

from models import GearItem

class IndexView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    
    def get_queryset(self):
      """ Returns gear sorted by name """
      return GearItem.objects.order_by('name')

class DetailsView(generic.DetailView):
    model = GearItem
    template_name = 'gearitem/details.html'
    
    def slotName(self):
      return slots[self.slot]