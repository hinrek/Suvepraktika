""" To make our models visible on the admin page """
from django.contrib import admin
from .models import Event, Comment, EventCategory

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(EventCategory)
