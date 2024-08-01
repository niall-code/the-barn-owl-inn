from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    number = models.IntegerField(blank=False, unique=True)
    seats = models.IntegerField(blank=False)

    def __str__(self):
        return f"Table {self.number}"


class Reservation(models.Model):
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
