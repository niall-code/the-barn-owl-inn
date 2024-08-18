from django.shortcuts import render


def home_page(request):
    """
    Renders the Home page
    """
    return render(
        request,
        "home/index.html",
    )
