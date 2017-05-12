import requests
import json
import time
# from testing import open_json

rests = []
rest_ids = set()
inspect_report = []
inspect_results = []


def get_restaurant_info():
    """Contact the King county API to obtain a JSON list of objects containing restaurant health inspection info that will be saved to 3 separate JSON files. """
    

    offset = 0

    while offset < 60000:


        #url to all king county restaurant health inspections since Jan 1, 2016 ordered by socrata ID
        url = 'http://data.kingcounty.gov/resource/gkhn-e8mn.json?$limit=50000&$order=:id&$where=inspection_date%20between%20%272016-01-01T12:00:00%27%20and%20%272017-05-01T12:00:00%27'

        # url = 'http://data.kingcounty.gov/resource/gkhn-e8mn.json?$limit=10&$order=:id&$where=inspection_date%20between%20%272016-01-01T12:00:00%27%20and%20%272017-05-01T12:00:00%27'

        r = requests.get(url)

        # data = open_json()
        data = r.json()

        for val in data:
            
            #parse the JSON into a dict of keys called restaurant

            restaurant = {}
            restaurant["fields"] = {}
            restaurant["model"] = "safe_eats_app.restaurantinfo"

            pk = val.get("business_id", "")
            if pk not in rest_ids:
                restaurant["pk"] = val.get("business_id", "")
                restaurant["fields"]["business_name"] = val.get("inspection_business_name", val.get("name", ""))
                restaurant["fields"]["address"] = val.get("address", "")
                restaurant["fields"]["city"] = val.get("city", "")
                restaurant["fields"]["zip_code"] = val.get("zip_code", "")
                restaurant["fields"]["longitude"] = val.get("longitude","")
                restaurant["fields"]["latitude"] = val.get("latitude", "")

                #add the restaurant results to the rests dict
                rests.append(restaurant)
                #add the unique pk to the rest_ids
                rest_ids.add(pk)


            #parse the JSON into a dict of keys called inspection
            inspection = {}

            if "inspection_serial_num" in val:

                inspection["pk"] = val["inspection_serial_num"]
                inspection["model"] = "safe_eats_app.InspectionReport"
                inspection["fields"] = {}
                inspection["fields"]["inspection_business_name"] = val.get("inspection_business_name", "")
                inspection["fields"]["restaurant"] = val.get("business_id", "")

                inspect_date = val.get("inspection_date", "")
                if len(inspect_date) > 10:
                    inspect_date = inspect_date[0:10]
                inspection["fields"]["inspection_date"] = inspect_date

                inspect_report.append(inspection)


            #parse the JSON into a dict of keys called violation
            violation = {}

            if "violation_record_id" in val:

                violation["violation_record_id"] = int(val.get("inspection_score", 0))

                violation["fields"] = {}
                violation["model"] = "safe_eats_app.InspectionResult"
                violation["fields"]["inspection"] = val.get("inspection_serial_num", "")
                violation["fields"]["inspection_score"] = int(val.get("inspection_score", 0))
                violation["fields"]["inspection_type"] = val.get("inspection_type", "")
                violation["fields"]["inspection_result"] = val.get("inspection_result", "")
                violation["fields"]["violation_description"] = val.get("violation_description", "")
                violation["fields"]["violation_points"] = val.get("violation_points", "")
                
                #add the results to the violation dict
                inspect_results.append(violation)


        offset += 50000
        time.sleep(2)
        print("number of restaurants in list: {}".format(len(rests)))



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