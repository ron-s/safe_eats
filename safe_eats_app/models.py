from django.db import models


# Create your models here.
class RestaurantInfo(models.Model):
	"""Describes data saved in Restaurant Info table"""

	business_id = models.CharField(max_length=15)
	google_restaurant_id = models.CharField(max_length=100)
	yelp_restaurant_id = models.CharField(max_length=100)
	business_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=15)
	longitude = models.FloatField()
	latitude = models.FloatField()
	health_inspection_src = models.CharField(max_length=100)





class InspectionReport(models.Model):
	"""Describes the Inspection Report ID"""

	restaurant = models.ForeignKey(RestaurantInfo)
	inspection_serial_num = models.CharField(max_length=15)
	inspection_business_name = models.CharField(max_length=100)
	inspection_date = models.CharField(max_length=30)





class InspectionResult(models.Model):
	"""Describes data saved in the Inspection Report table"""

	inspection = models.ForeignKey(InspectionReport)
	inspection_score = models.CharField(max_length=3)
	inspection_type = models.CharField(max_length=100)
	inspection_result = models.CharField(max_length=15)
	violation_description = models.CharField(max_length=15)
	violation_points = models.CharField(max_length=15)
	violation_record_id = models.CharField(max_length=15)



class HealthInspectionSource(models.Model):
	"""Describes the source for each municipality"""

	name = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)