from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def safe_eats_index(request):
	#print("test")
	#return an httpresponse of object using the render function
	return render(request, 'safe_eats/safe_eats.html')