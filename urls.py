from django.conf.urls import patterns, url

from gearitem import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /gearitem/5/
    url(r'^(?P<pk>\d+)/$', views.DetailsView.as_view(), name='details'),
    # ex: /gearitem/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /gearitem/5/comment/
    url(r'^(?P<gear_id>\d+)/comment/$', views.comment, name='comment'),
)