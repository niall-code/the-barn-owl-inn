from django.db import models
from django.contrib.auth.models import User


class Table(model.Models):
    table_num = models.CharField(max_length=3, blank=False, unique=True)
    seats = models.IntegerField(blank=False)
    booked = models.ManyToManyField()


class Reservation(model.Models):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    length = models.IntegerField(choices=((2, "2 hours"), (4, "4 hours")), blank=False)
    tables = models.ManyToManyField(Table, on_delete=models.CASCADE, unique_for_date=True)
