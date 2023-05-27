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


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Appointment._meta.get_fields()]


class SalonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Master)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Client)
admin.site.register(Appointment, AppointmentAdmin)
