from django.http import HttpResponse
from .models import Latlan

def gps(request):
    if request.method == 'GET':

        lat = request.GET['Lat']
        lan = request.GET['Lan']
        print float(lat), float(lan)
        latlan = Latlan(lat=float(lat), lan=float(lan))
        latlan.save()
        return HttpResponse(lat)


    return HttpResponse('hello')

def data(request):
    if request.method == 'GET':
        return HttpResponse(Latlan.objects.all())
