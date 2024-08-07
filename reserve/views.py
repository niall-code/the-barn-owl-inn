from django.shortcuts import render


def reservations_page(request):
    reservations = Reservation.objects.all()

    return render(
        request,
        "reserve/my_reservations.html",
        {
            'reservations': reservations,
        },
    )
