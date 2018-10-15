from django.shortcuts import render
import requests


def home(requests):
    respons = requests.get('http://freegeoip.net/json/')
    geodata = respons.json()
    return render(request, 'core/home.html',{
        'ip': geodata['ip'],
        'country': geodata['country_names']
    })