from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import python_weather
import asyncio


# Create your views here.

async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("indianapolis")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getweather())
class  weatherApi(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello, World!'}) 