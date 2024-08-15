from . import views
from django.urls import path


urlpatterns = [
    path('edit_reservation/<int:reserv_id>', views.reservation_edit, name='reservation_edit'),
    path('', views.reservations_page, name='reserve'),
]
