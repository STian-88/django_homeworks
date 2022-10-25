from django.contrib import admin

from .models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement
    list_display = ['create_at']
    extra = 0

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at']
    inlines = [MeasurementInline, ]


