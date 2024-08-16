from . import views
from django.urls import path


urlpatterns = [
    path('delete_reservation/<int:reserv_id>', views.reservation_delete, name='reservation_delete'),
    path('edit_reservation/<int:reserv_id>', views.reservation_edit, name='reservation_edit'),
    path('', views.reservations_page, name='reserve'),
]
