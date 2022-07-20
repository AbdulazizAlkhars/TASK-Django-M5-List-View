from django.contrib import admin
from .models import Booking, Flight
# Register your models here.

admin.site.register(Flight)
admin.site.register(Booking)


# @admin.register(Flight)
# class FlightAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ("id", "destination", "time", "price", "miles")
#     # list_filter = ("destination",)
#     # list_display_links = ("id", "destination")
#     # fieldsets = (
#     #     (None, {"fields": ("destination", "time", "price")}),
#     # )
