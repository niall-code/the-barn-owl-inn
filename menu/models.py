from django.db import models


class Dish(models.Model):
    course = models.IntegerField(
        choices=((1, "Starters"), (2, "Main Course"), (3, "Desserts")),
        blank=False)
    name = models.CharField(max_length=100, blank=False, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, blank=False)
