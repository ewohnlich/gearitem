from django.conf.urls import patterns, url

from gearitem import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='listing'),
    url(r'^ilvl/', views.IlvlSortView.as_view(), name='ilvl'),
    url(r'^slot/(?P<slot>\d+)', views.SlotView.as_view(), name='slot'),
    url(r'^zone/(?P<zone>\w+)', views.ZoneView.as_view(), name='zone'),
    # ex: /gearitem/5/
    url(r'^(?P<pk>\d+)/$', views.DetailsView.as_view(), name='details'),
)