from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'priority', 'assignee', 'attachment', 'end_date']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
