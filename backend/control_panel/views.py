from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Procedure


def get_index(request):
    return render(request, 'control_panel/index.html')


def get_procedures(request):
    procedures = Procedure.objects.all()
    context = {'procedures': procedures}
    return render(request, 'control_panel/procedures.html', context=context)


def get_procedure(request, id):
    procedure = get_object_or_404(Procedure, id=id)
    context = {'procedure': procedure}
    return render(request, 'control_panel/procedure.html', context=context)
