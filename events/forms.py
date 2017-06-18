""" Django forms """
from django import forms
from .models import Event, Comment


class MapForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('city', 'location')


class EventForm(forms.ModelForm):
    """ Form to create new events """
    title = forms.CharField(label='Projekti nimi')
    #description = forms.CharField(widget=forms.Textarea, label='Projekti sisu')
    #category = forms.ForeignKey(label="Kategooria")
    #location = forms.PlainLocationField(label='Asukoht')
    city = forms.CharField(label='Linn')
    event_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}), label='Algus kuupäev ja kellaaeg')
    register_limit_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label='Lõppemis kuupäev')

    class Meta:
        """ Tell Django which model should be used to create this form  """
        model = Event

        fields = ('title', 'descripton', 'city', 'location', 'category', 'event_date',
                  'register_limit_date')


class CommentForm(forms.ModelForm):
    """ Form to create new events """
    class Meta:
        model = Comment
        # fields = ('author', 'text',)
        fields = ('text',)

#class UserCreateForm(UserCreationForm):
#    email = forms.EmailField(required=True)

#    def __init__(self, *args, **kwargs):
#        super(UserCreateForm, self).__init__(*args, **kwargs)

#        for fieldname in ['username', 'password1', 'password2']:
#            self.fields[fieldname].help_text = None
