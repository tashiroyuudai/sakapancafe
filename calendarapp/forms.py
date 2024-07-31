from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'date', 'time_slot' ,'guests']
        widgets = {
            'user': forms.HiddenInput(),
            'date': forms.HiddenInput(),
            'time_slot': forms.HiddenInput(),
            'guests': forms.HiddenInput(),
        }
