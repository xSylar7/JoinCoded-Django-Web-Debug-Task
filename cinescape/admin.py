from django.contrib import admin
from .models import (
    Category, 
    Movies, 
    Location, 
    Theather)

admin.site.register(
    [
        Category, 
        Movies, 
        Location, 
        Theather,
    ]
)