

from django import forms
from .models import Ticket
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.helper import FormHelper

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('room', 'subject', 'notes')

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
             'room',
             'subject',
             'notes',
            ButtonHolder(
             Submit('create', 'Create', css_class='btn-primary')
          )
        )
