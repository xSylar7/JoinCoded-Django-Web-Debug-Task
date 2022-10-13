from django.contrib import admin
from cinescape.models import (
    Category, 
    Movies, 
    Location, 
    Theater)
admin.site.register([Category,Movies,Location,Theater])

# admin.site.register(
#     [
#         Category, 
#         Movies, 
#         Location, 
#         Theater,
#     ]
# )