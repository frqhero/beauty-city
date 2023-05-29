from django.urls import path

from .views import (
    get_index,
    get_make_appointment,
    get_scenarios,
    get_procedures,
    get_procedure,
    create_appointment,
    get_success_page,
)

app_name = 'control_panel'

urlpatterns = [
    path('', get_index),
    path('make-appointment', get_make_appointment, name='make_appointment'),
    path('choose-scenario', get_scenarios, name='choose_scenario'),
    path('procedures', get_procedures, name='procedures'),
    path('procedure/<int:procedure_id>', get_procedure, name='procedure'),
    path(
        'create-appointment/<str:day>/<str:timeslot>/<str:master>/<str:salon>/<int:procedure>',
        create_appointment,
        name='create_appointment',
    ),
    path(
        'success/<int:appointment_id>', get_success_page, name='success_page'
    ),
]
