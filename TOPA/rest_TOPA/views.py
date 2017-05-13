from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Airline, Flight
from .serializers import AirlineSerializer, FlightSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST','GET'])
def ejemplo(request):
	if request.method == 'POST':
		data=request.data
		flights = Flight.objects.filter(flightCode=data['flightCode'])
		serializer = FlightSerializer(flights, many=True)
		return Response(serializer.data)
	elif request.method == 'GET':
		flights = Flight.objects.all()
		serializer = FlightSerializer(flights, many=True)
		return Response(serializer.data)


