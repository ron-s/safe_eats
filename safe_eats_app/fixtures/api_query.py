import requests
import json




rests = []
inspect_report = []
inspect_results = []




def get_restaurant_info():

	url = "https://data.kingcounty.gov/resource/gkhn-e8mn.json?$where=inspection_date%20between%20%272015-01-01T12:00:00%27%20and%20%272016-03-25T14:00:00%27&inspection_closed_business=false&"

	r = requests.get(url
#		url, headers={"X-App-Token":"[ ]"}
	)

	data = r.json()


#need to scrub data 
#add conditional if no lat/long then don't add to database
	count = 0

	for val in data:
		try:
			restaurant = {}
			restaurant["fields"] = {}
			restaurant["model"] = "safe_eats_app.restaurantinfo"
			restaurant["business_id"] = val["business_id"]
			restaurant["fields"]["business_name"] = val["inspection_business_name"]
			restaurant["fields"]["address"] = val["address"]
			restaurant["fields"]["city"] = val["city"]
			restaurant["fields"]["zip_code"] = val["zip_code"]
			restaurant["fields"]["longitude"] = val["longitude"]
			restaurant["fields"]["latitude"] = val["latitude"]


			# latitude  = val["latitude"]
			# longitude = val["longitude"]

			# api_response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=50&type=restaurant&key={2}'.format(latitude,longitude,api_key))

			

			# if api_response.status_code == 200:
			# 	api_response_dict = api_response.json()
			# 	#print(api_response_dict)


			# 	results_list = api_response_dict['results']
			# 	for each_dict in results_list:
			# 		print(longitude)
			# 		if (each_dict["geometry"]["location"]["lat"] == latitude) and (each_dict["geometry"]["location"]["lng"] == longitude):
			# 			placeID = each_dict["place_id"]


			# 			#restaurant["fields"]["google_restaurant_id"] = api_response_dict[placeId]

			# 			break


			#restaurant["fields"]["yelp_restaurant_id"] = val[""]

			rests.append(restaurant)




			inspection = {}
			inspection["inspection_serial_num"] = val["inspection_serial_num"]
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
			violation["fields"]["violation_description"] = val.get("violation_description", '')
			violation["fields"]["violation_points"] = val["violation_points"]
			

			inspect_results.append(violation)
		
		except:
			print("Boooooo")




	with open('restaurants.json', "w") as f:
		json.dump(rests, f, indent=2)


	with open('inspection_results.json', "w") as f:
		json.dump(inspect_results, f, indent=2)

	with open('inspection_reports.json', "w") as f:
		json.dump(inspect_report, f, indent=2)


if __name__ == '__main__':
	get_restaurant_info()