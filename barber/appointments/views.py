from django.shortcuts import render
from .models import Appointment, Service
from django.views import generic

# Create your views here.
class ServiceListView(generic.ListView):
    template_name = 'appointments/index.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.all()