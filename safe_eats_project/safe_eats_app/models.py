from django.db import models

# Create your models here.
class RestaurantInfo(model.Models):
	"""Restaurant name and info"""

	name = models.CharField(max_length=200)
	google_restaurant_id = models.CharField(max_length=200)
	yelp_restaurant_id = models.CharField(max_length=200)
	socrates_business_id = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()





class InspectionReport(model.Models):
	"""Describes the Inspection Report ID"""
	inspection_serial_num = 






class InspectionResult(model.Models):
	"""descriptions of the InspectionReport"""
	result = models.ManyToMany(RestaurantInfo)

