from django.test import TestCase
from .models import RestaurantInfo



# Create your tests here.
class TestExampleCase(TestCase):
    def setUp(self):
        RestaurantInfo.objects.create(business_id=100, 
                                        business_name="new_restaurant",
                                        inspection_closed_business=False,
                                        address="555 skid row",
                                        city="portland",
                                        zip_code="98765"
                                        )



    def test_restaurant(self):
        testvar = RestaurantInfo.objects.all()[0]
        print("this is the restaurant name: {}".format(testvar))
        print(testvar.business_id)




