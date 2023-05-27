from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import AppointmentForm
from .models import Procedure, Appointment, Master, Salon


def get_index(request):
    return render(request, 'control_panel/index.html')


def get_procedures(request):
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    return render(request, 'control_panel/procedures.html', context=context)


def get_day_slots(day_increment):
    number_of_masters = Master.objects.all().count()
    tomorrow = datetime.now() + timedelta(day_increment)
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
        x for x in Appointment.TIME_SLOTS if x[0] in tomorrow_timeslots
    ]
    return available_timeslots


def get_procedure(request, procedure_id):
    procedure = get_object_or_404(Procedure, id=procedure_id)
    tomorrow_slots = get_day_slots(1)
    after_tomorrow_slots = get_day_slots(2)
    in_two_days_slots = get_day_slots(3)
    context = {
        'procedure': procedure,
        'procedure_id': procedure_id,
        'salon': 1,
        'master': 'any',
        'tomorrow_slots': tomorrow_slots,
        'after_tomorrow_slots': after_tomorrow_slots,
        'in_two_days_slots': in_two_days_slots,
    }
    return render(request, 'control_panel/procedure.html', context=context)


def get_master_id(master, date, timeslot):
    if master == 'any':
        all_masters = {master.id: 1 for master in Master.objects.all()}
        appointments_at_time = [
            appointment.master.id
            for appointment in Appointment.objects.filter(
                date=date, time_slot=timeslot
            )
        ]
        for appointment_at_time in appointments_at_time:
            all_masters[appointment_at_time] -= 1
        for master_id, master_free in all_masters.items():
            if master_free > 0:
                return master_id
    return master


def create_appointment(request, day, timeslot, master, salon, procedure):
    if request.method == 'POST':
        days = {
            'tomorrow': 1,
            'after-tomorrow': 2,
            'in-two-days': 3,
        }
        date = datetime.now() + timedelta(days[day])
        master_id = get_master_id(master, date, timeslot)
        master = get_object_or_404(Master, id=master_id)
        salon = get_object_or_404(Salon, id=salon)
        procedure = get_object_or_404(Procedure, id=procedure)
        form = AppointmentForm(
            {
                'date': date.date(),
                'time_slot': timeslot,
                'master': master,
                'procedure': procedure,
                'salon': salon,
                'phone_number': request.POST['phone_number'],
            }
        )
        if form.is_valid():
            obj = form.save()
            return redirect(
                reverse('control_panel:success_page', kwargs={'id': obj.id})
            )
    else:
        form = AppointmentForm()
    return render(request, 'control_panel/procedure_form.html', {'form': form})


def get_success_page(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    context = {
        'date': appointment.date,
        'time': next(appointment.get_timeslot_repr()),
        'salon': appointment.salon.title,
    }
    return render(request, 'control_panel/success.html', context=context)
