from . import views
from django.urls import path
from helloworld.views import PacienteListView

app_name = 'website'

urlpatterns = [
    path('/website/templates/website/pacientes', PacienteListView.as_view(), name="pacientes"),
]