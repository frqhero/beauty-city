from django.urls import path

from .views import (
    get_index, get_procedures, get_procedure, create_appointment
)


app_name = 'control_panel'

urlpatterns = [
    path('', get_index),
    path('procedures', get_procedures, name='procedures'),
    path('procedure/<int:id>', get_procedure, name='procedure'),
    path(
        'create-appointment/<str:day>/<str:timeslot>',
        create_appointment,
        name='create_appointment'
    )
]