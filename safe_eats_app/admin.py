from django.contrib import admin
from .models import RestaurantInfo, InspectionReport, InspectionResult, HealthInspectionSource

# Register your models here.
admin.site.register(RestaurantInfo)
admin.site.register(InspectionReport)
admin.site.register(InspectionResult)
admin.site.register(HealthInspectionSource)
