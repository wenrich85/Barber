from django.contrib import admin

from .models import Appointment, Service, Availability

@admin.register(Appointment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'date','time']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(Availability)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['start', 'end']