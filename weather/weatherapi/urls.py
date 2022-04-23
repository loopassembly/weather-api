from django.urls import path,include
from django.contrib import admin
from weatherapi import views



urlpatterns = [
    # path('', include(router.urls)),
    path('weather', views.weatherApi.as_view()),
]