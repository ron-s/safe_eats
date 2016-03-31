from .models import RestaurantInfo, InspectionReport, InspectionResult
from django.shortcuts import render
import json
from django.core import serializers


def safe_eats_index(request):
    # restaurants = RestaurantInfo.objects.all()
    # r = serializers.serialize("json", RestaurantInfo.objects.all(), fields=('longitude', 'latitude'))
    restaurants = {}
    for place in RestaurantInfo.objects.all():
        restaurants[place.business_id] = {"name": place.business_name,
                                          "address": place.address,
                                          "longitude": place.longitude,
                                          "latitude": place.latitude,
                                          "bus_id": place.business_id
                                          }
        results = {}
        num = 1
        for rpt in InspectionReport.objects.filter(restaurant=place.business_id):
            for rslts in InspectionResult.objects.filter(inspection=rpt.inspection_serial_num):
                results['result_' + str(num)] = {"inspection_result": rslts.inspection_result,
                                                 "description": rslts.violation_description}
            num += 1
        restaurants[place.business_id]["results"] = results
    print(json.dumps(restaurants, indent=4, sort_keys=True))
    r = json.dumps(restaurants)
    return render(request, 'safe_eats/safe_eats.html', {"restaurants": r})


def rest(request, restaurant):
    restaurant_info = RestaurantInfo.objects.get(business_id=restaurant)
    reports = InspectionReport.objects.filter(restaurant=restaurant_info.business_id)
    for repor in reports:
        rep = []
        for x in InspectionResult.objects.filter(inspection=repor.inspection_serial_num):
            rep.append(x)
        repor.related_set = rep
    return render(request, 'safe_eats/restaurant.html', {'rest_info': restaurant_info,
                                                         "reports": reports
                                                         })
