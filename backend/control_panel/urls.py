from django.urls import path

from .views import get_index, get_procedures, get_procedure


app_name = 'control_panel'

urlpatterns = [
    path('', get_index),
    path('procedures', get_procedures, name='procedures'),
    path('procedure/<int:id>', get_procedure, name='procedure')
]