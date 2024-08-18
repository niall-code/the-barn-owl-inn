from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    """
    A class to represent a Table at the restaurant.
    """
    number = models.IntegerField(blank=False, unique=True)
    seats = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.number}"


class Reservation(models.Model):
    """
    A class to represent a customer's Reservation.
    """
    reserver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reservations",
        blank=False
    )
    tables = models.ManyToManyField(
        Table,
        related_name="reservations",
        blank=False
    )
    date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    duration = models.IntegerField(
        choices=[(2, "2 hours"), (4, "4 hours")],
        blank=False
    )
    contact = models.CharField()

    def __str__(self):
        return f"{self.reserver} | {self.date}"
