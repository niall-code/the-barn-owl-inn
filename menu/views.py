from django.shortcuts import render
from .models import Dish


def menu_page(request):
    starters = Dish.objects.filter(course=1)
    mains = Dish.objects.filter(course=2)
    desserts = Dish.objects.filter(course=3)

    return render(
        request,
        "menu/menu.html",
        {
            'starters': starters,
            'mains': mains,
            'desserts': desserts
        },
    )
