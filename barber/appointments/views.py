from django.shortcuts import render
from .models import Appointment, Service, Availability
from django.views import generic

# Create your views here.
class ServiceListView(generic.ListView):
    template_name = 'appointments/index.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceListView, self).get_context_data(*args, **kwargs)
        context['availabilitys'] = Availability.objects.all()
        return context

# Create your views here.
class AvailabilityListView(generic.ListView):
    template_name = 'appointments/index.html'
    context_object_name = 'availabilitys'

    def get_queryset(self):
        return Availability.objects.all()



def make_schedule(request):
    timeslot = 'TESTING'

    context = {'timeslot': timeslot}
    return render(request, 'appointments/index.html',context)