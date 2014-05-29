from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views import generic

from models import GearItem, Comment

class IndexView(generic.ListView):
    template_name = 'gearitem/index.html'
    context_object_name = 'name_gear_list'
    
    def get_queryset(self):
      """ Returns gear sorted by name """
      return GearItem.objects.order_by('name')

class DetailsView(generic.DetailView):
    model = GearItem
    template_name = 'gearitem/details.html'

class ResultsView(generic.DetailView):
    model = GearItem
    template_name = 'gearitem/results.html'

def comment(request, gear_id):
    ob = Comment()
    ob.note = request.POST['note']
    ob.gearid = gear_id
    ob.save()
    return HttpResponseRedirect(reverse('gearitem:results', args=(gear_id,)))