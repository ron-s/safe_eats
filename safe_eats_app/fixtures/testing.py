# import requests
import json
import time

rests = []

def open_json():

	with open('rests.json', "r") as f:
		d = json.load(f)

	return d





def get_restaurant_info():
	"""Contact the King county API to obtain a JSON list of objects containing restaurant health inspection info that will be saved to 3 separate JSON files. """
	#url to all king county restaurant health inspections since 2006


	# url = "http://data.kingcounty.gov/resource/gkhn-e8mn.json"

	r = requests.get(url)

	data = r.json()

	with open('rests.json', "w") as f:
		json.dump(rests, f, indent=2)