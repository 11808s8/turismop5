from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from catalogo_guias.models import CustomUser

# Register your models here.

from .models import Ponto


admin.site.register(Ponto,LeafletGeoAdmin)
admin.site.register(CustomUser)