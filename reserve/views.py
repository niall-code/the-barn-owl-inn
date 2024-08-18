from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Reservation, Table
from .forms import ReservationForm


def reservations_page(request):
    """
    Reads the existing reservations data. Renders the My Reservations page,
    which displays any instances of :model:`reserve.Reservation` where the
    reserver attribute matches the authenticated user, as well as
    :form:`reserve.ReservationForm` for creating and editing reservations.

    If request method is POST, validates form data, adds reserver attribute,
    saves to database, then refreshes page.

    **Context**
    ``reservations``
        All instances of :model:`reserve.Reservation`
    ``tables``
        All instances of :model:`reserve.Table`
    ``reservation_form``
        An instance of :form:`reserve.ReservationForm`
        OR, if post method,
        an instance of :model:`reserve.Reservation`
    ``user``
        An instance of :model:`User`
    
    **Template**
    :template:`reserve/my_reservations.html`
    """

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

            return HttpResponseRedirect('/my-reservations')

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
    """
    Validates form data, adds reserver attribute and primary key of instance
    of :model:`reserve.Reservation` targeted to update, saves to database,
    then refreshes page.

    **Context**
    ``reservation_form``
        An instance of :model:`reserve.Reservation`
    ``reserv_id``
        The primary key of an instance of :model:`reserve.Reservation`
        targeted to be overwitten with new attribute values.
    ``user``
        An instance of :model:`User`
    
    **Template**
    :template:`reserve/my_reservations.html`
    """

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
    """
    Deletes an instance of :model:`reserve.Reservation` with a given
    primary key from the database, then refreshes page.

    **Context**
    ``reserv_id``
        The primary key of an instance of :model:`reserve.Reservation`
        targeted to be erased.
    ``unwanted_reservation``
        The retrieved instance of :model:`reserve.Reservation`
    
    **Template**
    :template:`reserve/my_reservations.html`
    """

    unwanted_reservation = get_object_or_404(Reservation, pk=reserv_id)
    unwanted_reservation.delete()

    return HttpResponseRedirect('/my-reservations')
