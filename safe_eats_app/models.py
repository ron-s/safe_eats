from django.db import models


# Create your models here.
class RestaurantInfo(models.Model):
    """Describes data saved in Restaurant Info table"""

    business_id = models.CharField(primary_key=True, max_length=100)
    business_name = models.CharField(max_length=100)
    inspection_closed_business = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.business_name


class InspectionReport(models.Model):
    """Describes the Inspection Report ID"""

    restaurant = models.ForeignKey('RestaurantInfo')
    inspection_serial_num = models.CharField(primary_key=True, max_length=100)
    inspection_business_name = models.CharField(max_length=100)
    inspection_date = models.DateField()

    def __str__(self):
        return self.inspection_business_name


class InspectionResult(models.Model):
    """Describes data saved in the Inspection Report table"""

    inspection = models.ForeignKey('InspectionReport')
    inspection_score = models.IntegerField()
    inspection_type = models.CharField(max_length=100)
    inspection_result = models.CharField(max_length=100)
    violation_description = models.CharField(max_length=100, blank=True)
    violation_points = models.CharField(max_length=100)
    violation_record_id = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.violation_description
