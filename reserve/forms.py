from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'duration', 'tables', 'contact',]
        widgets = {
            'date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'type': 'date'}
                ),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'tables': forms.CheckboxSelectMultiple()
        }
