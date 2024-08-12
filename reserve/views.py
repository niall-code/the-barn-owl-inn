from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Reservation, Table
from .forms import ReservationForm


def reservations_page(request):
    reservations = Reservation.objects.all()
    tables = Table.objects.all()

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            new_reservation = reservation_form.save(commit=False)
            new_reservation.reserver = request.user
            new_reservation.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your reservation has been made'
            )

    reservation_form = ReservationForm()

    return render(
        request,
        "reserve/my_reservations.html",
        {
            'reservations': reservations,
            'reservation_form': reservation_form,
            'tables': tables,
        },
    )
