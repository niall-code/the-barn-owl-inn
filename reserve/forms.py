from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['tables', 'date', 'start_time', 'duration', 'contact',]
        widgets = {
            'date': forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'type': 'date'}
                ),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }
