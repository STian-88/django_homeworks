from django.contrib import admin
from advertisements.models import Advertisement, AdvertisementStatusChoices

@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status',
            'creator', 'created_at', 'updated_at']
    list_filter = ['status', 'creator', 'created_at', 'updated_at']
