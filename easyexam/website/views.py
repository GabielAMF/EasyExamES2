from django.shortcuts import render
from django.views.generic import ListView
from easyexam.models import Paciente

class PacienteListView(ListView):
    template_name = "/website/templates/website/pacientes.html"
    model = Paciente
    context_object_name = "pacientes"
    