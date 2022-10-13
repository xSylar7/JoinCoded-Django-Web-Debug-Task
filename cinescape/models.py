from django.db import models
from unittest.util import _MAX_LENGTH

class Category(Model):
    class CategoryType(models.TextChoices):
        GENERAL = "G"
        PARENTAL_GUIDANCE = "PG"
        ADULT_GUARDIAN = "R"
        RESTRICTED = "X"

    rating = models.CharField(_MAX_LENGTH=1, choices=CategoryType)
    name = models.CharField(_MAX_LENGTH=50)

    def __str__(self):
        return self.name + ' ' + self.rating.CategoryType


class Movies(models.Model):
    name = models.CharField(_MAX_LENGTH=50)
    released_at = models.DateField()
    description = models.TextField()
    poster = models.URLField()

    def __str__(self):
        return self.name 

class Location(models):
    geolocation = models.CharField(_MAX_LENGTH=250)
    area_name = models.CharField(_MAX_LENGTH=50)
    address_one = models.CharField(_MAX_LENGTH=250)
    address_two = models.CharField(_MAX_LENGTH=250)

    def __str__(self):
        return self.name

class Theater(Model.models):
    name = models.CharField(_MAX_LENGTH=50)
    capacity = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name 

    @property
    def check_availablity(self):
        return self.capacity > self.booked_seats