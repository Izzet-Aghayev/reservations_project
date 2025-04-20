from asyncio import Server
from django.contrib import admin

from reservations.models import (
    Service,
    Reservation
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20



@admin.register(Reservation)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service')
    search_fields = ('user',)
    list_per_page = 20