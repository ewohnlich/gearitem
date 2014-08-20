from django.conf.urls import patterns, url

from gearitem import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='listing'),
    # ex: /gearitem/5/
    url(r'^(?P<pk>\d+)/$', views.DetailsView.as_view(), name='details'),
)