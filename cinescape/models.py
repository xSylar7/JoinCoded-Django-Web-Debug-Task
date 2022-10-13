from django.db import models

class Category(models.Model):
    class CategoryType(models.TextChoices):
        GENERAL = "G"
        PARENTAL_GUIDANCE = "PG"
        ADULT_GUARDIAN = "R"
        RESTRICTED = "X"

    rating = models.CharField(max_length=1, choices=CategoryType)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'''{self.name} + ' ' + {self.rating}.CategoryType'''


class Movies(models.Model):
    name = models.CharField(max_length=50)
    released_at = models.DateField()
    description = models.TextField()
    poster = models.URLField()

    def __str__(self):
        return self.name 

class Location(models.Model):
    geolocation = models.CharField(max_length=250)
    area_name = models.CharField(max_length=50)
    address_one = models.CharField(max_length=250)
    address_two = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.name 

    @property
    def check_availablity(self):
        return self.capacity > self.booked_seats