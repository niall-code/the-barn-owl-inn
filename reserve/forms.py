from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('tables', 'date', 'start_time', 'duration', 'contact',)
