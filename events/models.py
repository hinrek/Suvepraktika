# -*- coding: UTF-8 -*-
""" Model for events """
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField



class Event(models.Model):
    """ Event class """
    author = models.ForeignKey('auth.User')
    members = models.TextField()
    title = models.CharField(verbose_name="Projekti nimi",max_length=200)
    descripton = models.TextField(verbose_name="Projekti sisu")
    city = models.CharField(verbose_name="Linn",max_length=255, default='Tallinn')
    location = PlainLocationField(verbose_name="Asukoht",based_fields=['city'], zoom=150, default='59.43696079999999,24.75357459999998')
    category = models.ForeignKey('EventCategory', on_delete=models.PROTECT, default='Sport')
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(verbose_name="Algus kuupäev ja kellaaeg",default=timezone.now,blank=True, null=True)
    register_limit_date = models.DateField(verbose_name="Lõppemis kuupäev",default=timezone.now,blank=True, null=True)

    def publish(self):
        """ Publishes event and sets created_date to timezone.now() """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Comment class for event comments """
    post = models.ForeignKey('events.Event', related_name='comments')
    # author = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """ Method for approving comments """
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class EventCategory(models.Model):
    """ Category field class for event categories """
    category = models.TextField()

    def __str__(self):
        return self.category
