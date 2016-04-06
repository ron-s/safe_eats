import requests
import json

rests = []
inspect_report = []
inspect_results = []


def get_restaurant_info():
    """Contact the King county API to obtain a JSON list of objects containing restaurant health inspection info that will be saved to 3 separate JSON files. """
    #url to all king county restaurant health inspections since 2006
    url = "https://data.kingcounty.gov/resource/f29f-zza5.json"
    #url = "https://data.kingcounty.gov/resource/gkhn-e8mn.json?&inspection_business_name=Subway&$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-22T14:00:00%27"
    r = requests.get(url)

    data = r.json()
    # print(type(data))

    count = 0
    pk = 0

    for val in data:
        #parse the JSON into a dict of keys called restaurant
        try:

            restaurant = {}
            restaurant["fields"] = {}
            restaurant["model"] = "safe_eats_app.restaurantinfo"
            restaurant["pk"] = val["business_id"]
            # restaurant["fields"]["business_id"] = val["business_id"]
            restaurant["fields"]["business_name"] = val["inspection_business_name"]
            restaurant["fields"]["address"] = val["address"]
            restaurant["fields"]["city"] = val["city"]
            restaurant["fields"]["zip_code"] = val["zip_code"]
            restaurant["fields"]["longitude"] = val["longitude"]
            restaurant["fields"]["latitude"] = val["latitude"]

            #add the results to the restaurant dict
            rests.append(restaurant)


            #parse the JSON into a dict of keys called inspection
            inspection = {}
            inspection["pk"] = val["inspection_serial_num"]
            inspection["model"] = "safe_eats_app.InspectionReport"
            inspection["fields"] = {}
            inspection["fields"]["inspection_business_name"] = val["inspection_business_name"]
            inspection["fields"]["restaurant"] = val["business_id"]
            inspection["fields"]["inspection_date"] = val["inspection_date"][0:10]

            #add the results to the inspection dict
            inspect_report.append(inspection)

            #parse the JSON into a dict of keys called violation
            violation = {}
            if val["violation_points"] == "0":
                count += 1
            violation["violation_record_id"] = val.get("violation_record_id", count)
            violation["fields"] = {}
            violation["model"] = "safe_eats_app.InspectionResult"
            violation["fields"]["inspection"] = val["inspection_serial_num"]
            try:
                violation["fields"]["inspection_score"] = val["inspection_score"]
            except KeyError:
                violation["fields"]["inspection_score"] = ""
            
            violation["fields"]["inspection_type"] = val["inspection_type"]
            violation["fields"]["inspection_result"] = val["inspection_result"]
            try:
                violation["fields"]["violation_description"] = val["violation_description"]
            except KeyError:
                violation["fields"]["violation_description"] = ""

            violation["fields"]["violation_points"] = val["violation_points"]
            violation["pk"] = pk
            pk += 1
        except KeyError:
            pass

        #add the results to the violation dict
        inspect_results.append(violation)

    #The restaurant file will contain the restaurant name and location.
    with open('restaurants.json', "w") as f:
        json.dump(rests, f, indent=2)

    #The Inspection report file will contain the restaurant info attached to the inpection report.
    with open('inspection_results.json', "w") as f:
        json.dump(inspect_results, f, indent=2)

    #The Inspection results will contain the results from each inspection. More than one result is possible for each report.
    with open('inspection_reports.json', "w") as f:
        json.dump(inspect_report, f, indent=2)


if __name__ == '__main__':
    get_restaurant_info()