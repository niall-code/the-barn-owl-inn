from django.shortcuts import render, get_object_or_404
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
            reservation_form.save_m2m()

            messages.add_message(
                request, messages.SUCCESS,
                'Your reservation has been made'
            )

            # return HttpResponseRedirect('/my-reservations')

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


def reservation_edit(request, reserv_id):
    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)
        if reservation_form.is_valid():
            updated_reservation = reservation_form.save(commit=False)
            updated_reservation.id = reserv_id
            updated_reservation.reserver = request.user
            updated_reservation.save()
            reservation_form.save_m2m()

    return HttpResponseRedirect('/my-reservations')


def reservation_delete(request, reserv_id):
    unwanted_reservation = get_object_or_404(Reservation, pk=reserv_id)
    unwanted_reservation.delete()

    return HttpResponseRedirect('/my-reservations')
