from django.contrib import admin
from .models import Room, Building, Ticket


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)

class BuildingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Building, BuildingAdmin)
