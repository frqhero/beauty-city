from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Procedure, Appointment, Master


def get_index(request):
    return render(request, 'control_panel/index.html')


def get_procedures(request):
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    return render(request, 'control_panel/procedures.html', context=context)


def get_day_slots(day_increment):
    number_of_masters = Master.objects.all().count()
    tomorrow = (datetime.now() + timedelta(day_increment))
    tomorrow_appoinments = Appointment.objects.filter(date__day=tomorrow.day)
    timeslot_indexes = {str(x): number_of_masters for x in range(0, 10)}
    for appointment in tomorrow_appoinments:
        timeslot_indexes[appointment.time_slot] -= 1
    tomorrow_timeslots = [
        timeslot_val
        for timeslot_val, num_of_availabilities in timeslot_indexes.items()
        if num_of_availabilities > 0
    ]
    available_timeslots = [
        x
        for x in Appointment.TIME_SLOTS
        if x[0] in tomorrow_timeslots
    ]
    return available_timeslots


def get_procedure(request, id):
    procedure = get_object_or_404(Procedure, id=id)
    tomorrow_slots = get_day_slots(1)
    after_tomorrow_slots = get_day_slots(2)
    in_two_days_slots = get_day_slots(3)
    context = {
        'procedure': procedure,
        'tomorrow_slots': tomorrow_slots,
        'after_tomorrow_slots': after_tomorrow_slots,
        'in_two_days_slots': in_two_days_slots
    }
    return render(request, 'control_panel/procedure.html', context=context)


def create_appointment(request, day, timeslot):
    pass
