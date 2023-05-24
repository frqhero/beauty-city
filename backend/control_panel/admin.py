from django.contrib import admin
from .models import (
    Master,
    Procedure,
    Salon,
    Client,
    Appointment
)


admin.site.register(Master)
admin.site.register(Procedure)
admin.site.register(Salon)
admin.site.register(Client)
admin.site.register(Appointment)
