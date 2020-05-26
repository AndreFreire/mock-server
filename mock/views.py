from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from time import sleep
import requests


@csrf_exempt
def index1(request, *argparams, **kwparams):
    return index(request)


def index(request):
    #import ipdb;ipdb.set_trace()
    with open('data.json') as json_file:
        data = json.load(json_file)
        service_config = data.get(request.path.split("/")[1])
        sleep(service_config.get("wait"))
        path = request.build_absolute_uri().split(request.path.split("/")[1])[1]

        if type(service_config.get("status")) == int:
            return HttpResponse(status=service_config.get("status"))

        if service_config.get("status") == "custom":
            for i in service_config.get("custom"):
                if path.startswith(i.get("path")):
                    return HttpResponse(str(i.get("response")).replace("'","\""), status=i.get("status"), content_type="application/json")

        headers = {}
        for i in request.headers:
            if i.lower() in data.get("headers"):
                headers[i] = request.headers[i]
        
        url = service_config.get("url") + path
        
        if request.method == 'GET':
            response = requests.get(url, headers=headers)
        if request.method == 'POST':
            response = requests.post(url, data=request.body, headers=headers)
        if request.method == 'PUT':
            response = requests.put(url, data=request.body, headers=headers)
        if request.method == 'DELETE':
            response = requests.delete(url, data=request.body, headers=headers)

        return HttpResponse(response.text, status=response.status_code, content_type="application/json")
            
    return HttpResponse(status=599)

@csrf_exempt
def update(request):
    #with open('data.txt') as json_file:
    #    data = json.load(json_file)
    #    import ipdb;ipdb.set_trace()
    with open('data.json', 'w') as outfile:        
        json.dump(json.loads(request.body), outfile)
    return HttpResponse(status=200)
