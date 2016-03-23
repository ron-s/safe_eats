import requests
import json


def get_restaurant_data():

	url = "https://data.kingcounty.gov/resource/gkhn-e8mn.json?$where=starts_with(description,%27Mobile%20Food%20Unit%27)&inspection_date=2016-03-18T00:00:00.000)"
	r = requests.get(
	    url, headers={"X-App-Token":"[]"}
	)

	data = r.json()

	for val in data.values():

		restaurant["fields"] = {}
		restaurant["fields"]["business_id"] = val["business_id"]
		restaurant["fields"]["business_name"] = val["inspection_business_name"]
		restaurant["fields"]["address"] = val["address"]
		restaurant["fields"]["city"] = val["city"]
		restaurant["fields"]["zip_code"] = val["zip_code"]
		
		restaurant["fields"]["latitude"] = val["latitude"]
		restaurant["fields"]["longitude"] = val["longitude"]

		restaurant["fields"]["inspection_date"] = val["inspection_date"]
		restaurant["fields"]["inspection_result"] = val["inspection_result"]
		restaurant["fields"]["inspection_score"] = val["inspection_score"]
		restaurant["fields"]["inspection_type"] = val["inspection_type"]
		restaurant["fields"]["inspection_serial_num"] = val["inspection_serial_num"]
		restaurant["fields"]["violation_points"] = val["violation_points"]
		restaurant["fields"]["violation_description"] = val["violation_description"]
		restaurant["fields"]["violation_record_id"] = val["violation_record_id"]

		output.append(restaurant)








if __name__ == '__main__':
	get_restaurant_data()