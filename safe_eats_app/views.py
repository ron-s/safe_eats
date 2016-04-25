from .models import RestaurantInfo, InspectionReport, InspectionResult
from django.shortcuts import render
import json
from django.core import serializers
from django.db.models import Q




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








def restaurant_search(request):
    """ Searches for a restaurant by name """
    if request.method == "POST":
        query = request.POST["name"]

        #create a dict called restaurants that identifies each object by the retaurant's business_id
        restaurants = {}
        for place in RestaurantInfo.objects.filter(Q(business_name__contains=query)):
            restaurants[place.business_id] = {"name": place.business_name,
                                                "address": place.address,
                                                "longitude": place.longitude,
                                                "latitude": place.latitude,
                                                "bus_id": place.business_id
                                                }
            #create a dict containing the inspection report for each restaurant
            results = {}
            num = 1
            for rpt in InspectionReport.objects.filter(restaurant=place.business_id):
                for rslts in InspectionResult.objects.filter(inspection=rpt.inspection_serial_num):
                    results['result_' + str(num)] = {"inspection_result": rslts.inspection_result,
                                                    "description": rslts.violation_description,
                                                    "inspection_score": rslts.inspection_score
                                                    }
                num += 1
            restaurants[place.business_id]["results"] = results
        #print(json.dumps(restaurants, indent=4, sort_keys=True))

        #export the results as a JSON to pass to the template
        r = json.dumps(restaurants)
        print(r)
        return render(request, 'safe_eats/safe_eats.html', {"restaurants": r})






def worst_offenders(request):
    """ Searches for all restaurants with an inspection score greater than 170  """


    #create a dict called restaurants that we'll place all the offenders into
    restaurants = {}

    #locate all inspection results with a score greater than or equal to 130.
    offenders = InspectionResult.objects.filter(inspection_score__gte=170)

    for place in offenders:
        restaurants[place.inspection.restaurant.business_id] = {"name": place.inspection.restaurant.business_name,
                                                "address": place.inspection.restaurant.address,
                                                "longitude": place.inspection.restaurant.longitude,
                                                "latitude": place.inspection.restaurant.latitude,
                                                "bus_id": place.inspection.restaurant.business_id,
                                                "inspection_result": place.inspection_result,
                                                "inspection_date": date_handler(place.inspection.inspection_date),
                                                "description": place.violation_description,
                                                "inspection_score": place.inspection_score,
                                                }



    #export the results as a JSON to pass to the template
    r = 0#json.dumps(offenders)

    data = json.dumps(restaurants)

    print(data)
    #print(offenders[0].inspection.restaurant.business_name)

    return render(request, 'safe_eats/worst_offenders.html', {"restaurants": data})





def date_handler(obj):
    """serialize date-time from the python model for use in a json object"""

    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    #print (json.dumps(data, default=date_handler))





def downtown(request):
    """ Searches for all restaurants in 98101 zip code """

    # create a dict called restaurants that identifies each object by the retaurant's business_id
    restaurants = {}
    for place in RestaurantInfo.objects.filter(zip_code=98101):
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
    return render(request, 'safe_eats/downtown.html', {"restaurants": r})




def pioneer_square(request):
    """ Searches for all restaurants in 98104 zip code """

    # create a dict called restaurants that identifies each object by the retaurant's business_id
    restaurants = {}
    for place in RestaurantInfo.objects.filter(zip_code=98104):
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
    return render(request, 'safe_eats/pioneer_square.html', {"restaurants": r})



def neighborhood(request):

    """ returns all restaurants in a neighborhood by zip code"""



    if request.method == "POST":
        query = request.POST["name"]
        print(query)

        zip_codes = {"Downtown": ["98101"],
                    "Pioneer Square / Chinatown": ["98104"],
                    "Belltown / Denny Triangle": ["98121"],
                    "Kirkland": ["98033"],
                    "Magnolia": ["98199"],
                    "Redmond": ["98052"],
                    "Queen Anne": ["98119", "98109"]
                    }

        #create a dict called restaurants that identifies each object by the retaurant's business_id
        restaurants = {}

        for place in RestaurantInfo.objects.filter(zip_code__in=zip_codes[query]):
            restaurants[place.business_id] = {"name": place.business_name,
                                                "address": place.address,
                                                "longitude": place.longitude,
                                                "latitude": place.latitude,
                                                "bus_id": place.business_id
                                                }
            #create a dict containing the inspection report for each restaurant
            results = {}
            num = 1
            for rpt in InspectionReport.objects.filter(restaurant=place.business_id):
                for rslts in InspectionResult.objects.filter(inspection=rpt.inspection_serial_num):
                    results['result_' + str(num)] = {"inspection_result": rslts.inspection_result,
                                                    "description": rslts.violation_description,
                                                    "inspection_score": rslts.inspection_score
                                                    }
                num += 1
            restaurants[place.business_id]["results"] = results


        #export the results as a JSON to pass to the template
        r = json.dumps(restaurants)
        print(r)
        return render(request, 'safe_eats/neighborhood.html', {"restaurants": r})
