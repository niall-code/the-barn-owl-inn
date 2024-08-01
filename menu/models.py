from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    course = models.IntegerField(
        choices=[(1, "Starters"), (2, "Main Course"), (3, "Desserts")],
        blank=False
    )
    price = models.DecimalField(decimal_places=2, max_digits=4, blank=False)

    def __str__(self):
        return self.name
