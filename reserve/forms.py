from .models import Reservation, Table
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'duration', 'tables', 'contact',]
        widgets = {
            'date': forms.DateInput(
                format='Y-m-d',
                attrs={'type': 'date'}
                ),
            'start_time': forms.TimeInput(
                format='HH:mm',
                attrs={'type': 'time'}
                ),
            'tables': forms.CheckboxSelectMultiple()
        }
