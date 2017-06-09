""" URL Congfiguration """
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change,
    password_change_done
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/password/change/$',
        password_change, {
            'template_name': 'registration/password_change_form.html'},
        name='password_change'),
    url(r'^accounts/password/change/done/$',
        password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'),
    url(r'^accounts/password/reset/$',
        password_reset,
        {'template_name':
             'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
             'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name':
             'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name':
             'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'', include('events.urls')),
]
