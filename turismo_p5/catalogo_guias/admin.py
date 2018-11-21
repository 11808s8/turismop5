from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

from .models import Ponto


admin.site.register(Ponto,LeafletGeoAdmin)