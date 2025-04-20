from django.contrib import admin
from .models import FarmVisit

@admin.register(FarmVisit)
class FarmVisitAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farm_id', 'visit_date', 'visit_type', 'officer_name')
    list_filter = ('visit_date', 'visit_type', 'farm_type')
    search_fields = ('farmer_name', 'farm_id', 'location')
    date_hierarchy = 'visit_date'
