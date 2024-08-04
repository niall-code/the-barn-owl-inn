from django.shortcuts import render


def home_page(request):
    """
    Renders the Home page
    """
    # home = Home.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "home/index.html"
        # { "home": home, },
    )
