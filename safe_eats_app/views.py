from .models import RestaurantInfo, InspectionReport, InspectionResult
from django.shortcuts import render
import json
from django.core import serializers


def safe_eats_index(request):
    """creates a json string containing every restaurant and its associated info that will be placed on the homepage map as a marker with info window"""

    # restaurants = RestaurantInfo.objects.all()
    # r = serializers.serialize("json", RestaurantInfo.objects.all(), fields=('longitude', 'latitude'))

    # create a dict called restaurants that identifies each object by the retaurant's business_id
    restaurants = {}
    for place in RestaurantInfo.objects.all()[:50]:
        restaurants[place.business_id] = {"name": place.business_name,
                                          "address": place.address,
                                          "longitude": place.longitude,
                                          "latitude": place.latitude,
                                          "bus_id": place.business_id
                                          }
        # create a dict containing the inspection report for each restaurant
        results = {}
        num = 1
        for rpt in InspectionReport.objects.filter(restaurant=place.business_id):
            for rslts in InspectionResult.objects.filter(inspection=rpt.inspection_serial_num):
                results['result_' + str(num)] = {"inspection_result": rslts.inspection_result,
                                                 "description": rslts.violation_description,
                                                 "inspection_score": rslts.inspection_score}

            num += 1
        restaurants[place.business_id]["results"] = results
    # print(json.dumps(restaurants, indent=4, sort_keys=True))

    # export the results as a JSON to pass to the template
    r = json.dumps(restaurants)
    return render(request, 'safe_eats/safe_eats.html', {"restaurants": r})


def rest(request, restaurant):
    """Grabs the details of the inspection report for an individual restaurant and passes it to the restaurant template"""

    restaurant_info = RestaurantInfo.objects.get(business_id=restaurant)
    # sort the results by decending date
    reports = InspectionReport.objects.filter(restaurant=restaurant_info.business_id).order_by('-inspection_date')
    # locate all the results associated for each inspection report
    for repor in reports:
        print(InspectionResult.objects.filter(inspection=repor.inspection_serial_num))
        rep = []

        for x in InspectionResult.objects.filter(inspection=repor.inspection_serial_num):
            # append all results to each inspection report
            print(x)
            rep.append(x)
        repor.related_set = rep

    return render(request, 'safe_eats/restaurant.html', {'rest_info': restaurant_info,
                                                         "reports": reports
                                                         })







    # def restaurants_search(request):
    #   """creates a json string containing every restaurant that has been closed down due to failing a restaurant inspection and place a marker on the google map with an info window"""

    #   # restaurants = RestaurantInfo.objects.all()
    #   # r = serializers.serialize("json", RestaurantInfo.objects.all(), fields=('longitude', 'latitude'))

    #   #create a dict called restaurants that identifies each object by the retaurant's business_id
    #   restaurants = {}
    #   for place in RestaurantInfo.objects.all()[:50]:
    #       restaurants[place.business_id] = {"name": place.business_name,
    #                                         "address": place.address,
    #                                         "longitude": place.longitude,
    #                                         "latitude": place.latitude,
    #                                         "bus_id": place.business_id
    #                                         }
    #       #create a dict containing the inspection report for each restaurant
    #       results = {}
    #       num = 1
    #       for rpt in InspectionReport.objects.filter(restaurant=place.business_id):
    #           for rslts in InspectionResult.objects.filter(inspection=rpt.inspection_serial_num):
    #               results['result_' + str(num)] = {"inspection_result": rslts.inspection_result,
    #                                                 "description": rslts.violation_description,
    #                                                 "inspection_score": rslts.inspection_score}
    #           num += 1
    #       restaurants[place.business_id]["results"] = results
    #   #print(json.dumps(restaurants, indent=4, sort_keys=True))

    #   #export the results as a JSON to pass to the template
    #   r = json.dumps(restaurants)
    #   return render(request, 'safe_eats/safe_eats.html', {"restaurants_closed": r})
