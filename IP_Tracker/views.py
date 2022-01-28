import os
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from urllib.request import urlopen
from json import dumps
# Create your views here.
import socket


def Home(request):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("Your Computer IP Address is:" + ip)
    api_key = 'at_MZxV86uJWy8Bzr0Pe0ydfi7sEzzw3'
    api_url = 'https://geo.ipify.org/api/v1?'
    url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
    result = urlopen(url).read().decode('utf8')
    json_obj = json.loads(result)
    region = json_obj['location']['region']
    country = json_obj['location']['country']
    latitude = json_obj['location']['lat']
    longitude = json_obj['location']['lng']
    postalCode = json_obj['location']['postalCode']
    time_zone = json_obj['location']['timezone']
    isp = json_obj['isp']
    return render(request, "index.html",
                  {'ip': ip, 'country': country, 'postalCode': postalCode, 'time_zone': time_zone,
                   'isp': isp})


def show_ip_result(request):
    ip = request.GET["ip"]
    api_key = 'at_MZxV86uJWy8Bzr0Pe0ydfi7sEzzw3'
    api_url = 'https://geo.ipify.org/api/v1?'
    url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
    result = urlopen(url).read().decode('utf8')
    json_obj = json.loads(result)
    region = json_obj['location']['region']
    country = json_obj['location']['country']
    latitude = json_obj['location']['lat']
    longitude = json_obj['location']['lng']
    postalCode = json_obj['location']['postalCode']
    time_zone = json_obj['location']['timezone']
    isp = json_obj['isp']
    print(longitude)
    print(latitude)
    return render(request, 'index.html',
                  {'ip': ip, 'region': region, 'country': country, 'postalCode': postalCode, 'time_zone': time_zone,
                   'isp': isp, 'latitude': latitude, 'longitude': longitude})
    # return HttpResponse(result)
