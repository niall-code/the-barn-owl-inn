from django.shortcuts import render
from .models import Dish


def menu_page(request):
    """
    Reads the current restaurant menu data. Renders the Menu page.
    Displays all instances of :model:`menu.Dish`, grouped by course attribute.

    **Context**
    ``starters``
        Instances of :model:`menu.Dish` with course attribute value of 1.
    ``mains``
        Instances of :model:`menu.Dish with course attribute value of 2.
    ``desserts``
        Instances of :model:`menu.Dish with course attribute value of 3.
    
    **Template**
    :template:`menu/menu.html`
    """

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
