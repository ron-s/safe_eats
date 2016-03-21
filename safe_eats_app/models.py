from django.db import models


# Create your models here.
class RestaurantInfo(models.Model):
	"""Describes data saved in Restaurant Info table"""

	business_id = models.SlugField(max_length=15)
	google_restaurant_id = models.CharField(max_length=100, blank=True)
	yelp_restaurant_id = models.CharField(max_length=100, blank=True)
	business_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	zip_code = models.SlugField(max_length=15)
	longitude = models.FloatField()
	latitude = models.FloatField()
	health_inspection_src = models.ForeignKey('HealthInspectionSource')

	def __str__(self):
		return self.business_name




class InspectionReport(models.Model):
	"""Describes the Inspection Report ID"""

	restaurant = models.ForeignKey('RestaurantInfo')
	inspection_serial_num = models.SlugField(max_length=15)
	inspection_business_name = models.CharField(max_length=100)
	inspection_date = models.DateField()

	def __str__(self):
		return self.inspection_business_name



class InspectionResult(models.Model):
	"""Describes data saved in the Inspection Report table"""

	inspection = models.ForeignKey('InspectionReport')
	inspection_score = models.CharField(max_length=3)
	inspection_type = models.CharField(max_length=100)
	inspection_result = models.CharField(max_length=15)
	violation_description = models.CharField(max_length=15, blank=True)
	violation_points = models.CharField(max_length=15)
	violation_record_id = models.CharField(max_length=15, blank=True)



class HealthInspectionSource(models.Model):
	"""Describes the source of data used for each municipality"""

	name = models.CharField(max_length=100)
	website = models.URLField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, blank=True)

	def __str__(self):
		return self.name
