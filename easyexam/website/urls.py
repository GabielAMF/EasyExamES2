from . import views
from django.urls import path
from website.views import PacienteListView

app_name = 'website'

urlpatterns = [
    path('easyexam/website/templates/website/pacientes', PacienteListView.as_view(), name="pacientes"),
]