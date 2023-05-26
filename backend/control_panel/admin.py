from django.contrib import admin
from .models import (
    Master,
    Procedure,
    Salon,
    Client,
    Appointment
)


class ProcedureAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Master)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Salon)
admin.site.register(Client)
admin.site.register(Appointment)
