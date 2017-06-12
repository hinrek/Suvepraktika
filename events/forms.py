""" Django forms """
from django import forms

from .models import Event, Comment



class MapForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =('city', 'location')

class EventForm(forms.ModelForm):
    """ Form to create new events """
    class Meta:
        """ Tell Django which model should be used to create this form  """
        model = Event

        fields = ('title', 'descripton', 'city', 'location',  'category', 'event_date',
                  'register_limit_date')



class CommentForm(forms.ModelForm):
    """ Form to create new events """
    class Meta:
        model = Comment
        # fields = ('author', 'text',)
        fields = ('text',)
