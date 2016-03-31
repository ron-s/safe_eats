import requests
import json

rests = []
inspect_report = []
inspect_results = []


def get_restaurant_info():
    url = "https://data.kingcounty.gov/resource/gkhn-e8mn.json?&inspection_business_name=Subway&$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-22T14:00:00%27"
    r = requests.get(url)

    data = r.json()
    # print(type(data))


    count = 0
    pk = 0

    for val in data:
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

        rests.append(restaurant)

        inspection = {}
        inspection["pk"] = val["inspection_serial_num"]
        inspection["model"] = "safe_eats_app.InspectionReport"
        inspection["fields"] = {}
        inspection["fields"]["inspection_business_name"] = val["inspection_business_name"]
        inspection["fields"]["restaurant"] = val["business_id"]
        inspection["fields"]["inspection_date"] = val["inspection_date"][0:10]

        inspect_report.append(inspection)

        violation = {}
        if val["violation_points"] == "0":
            count += 1
        violation["violation_record_id"] = val.get("violation_record_id", count)
        violation["fields"] = {}
        violation["model"] = "safe_eats_app.InspectionResult"
        violation["fields"]["inspection"] = val["inspection_serial_num"]
        violation["fields"]["inspection_score"] = val["inspection_score"]
        violation["fields"]["inspection_type"] = val["inspection_type"]
        violation["fields"]["inspection_result"] = val["inspection_result"]
        try:
            violation["fields"]["violation_description"] = val["violation_description"]
        except KeyError:
            violation["fields"]["violation_description"] = ""

        violation["fields"]["violation_points"] = val["violation_points"]
        violation["pk"] = pk
        pk += 1

        inspect_results.append(violation)

    with open('restaurants.json', "w") as f:
        json.dump(rests, f, indent=2)

    with open('inspection_results.json', "w") as f:
        json.dump(inspect_results, f, indent=2)

    with open('inspection_reports.json', "w") as f:
        json.dump(inspect_report, f, indent=2)


if __name__ == '__main__':
    get_restaurant_info()