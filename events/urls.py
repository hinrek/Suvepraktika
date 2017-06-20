""" Events URL Configuration """
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/eventlist/$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/remove/$', views.event_remove, name='event_remove'),
    url(r'^event/(?P<pk>\d+)/comment/$', views.add_comment_to_event, name='add_comment_to_event'),
    url(r'^eventsubscription/(?P<pk>\d+)/', views.event_unjoin, name='event_unjoin'),
    url(r'^eventsubscription/(?P<pk>\d+)/', views.event_join, name='event_join'),
]
