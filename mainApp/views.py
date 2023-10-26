from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import io
def homePage(Request):
    return render(Request,'index.html')
@csrf_exempt
def createRecord(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    empSerilalizer = EmployeeSerializer(data=pythonData)
    if(empSerilalizer.is_valid()):
        empSerilalizer.save()
        msg = {"result":"done","message":"Record is Create!!!"}
    else:
        msg = {"result":"Fail","message":"Invalid Record!!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")
def getRecord(Request):
    data = Employee.objects.all()
    dataserializer = EmployeeSerializer(data,many=True)
    return HttpResponse(JSONRenderer().render(dataserializer.data),content_type="applicate/json")

def getSingleRecord(Request,id ):
    try:
       data = Employee.objects.get(id=id)
       dataSerializer = EmployeeSerializer(data)
       return HttpResponse(JSONRenderer().render(dataSerializer.data),content_type="applicate/json")
    except:
        msg = {"result":"Done","message":"id not valid!!!"}
        return HttpResponse(JSONRenderer().render(msg),content_type="application/json")

def searchRecord(Request,search):
    data = Employee.objects.filter(Q(name__contains=search)|Q(dsg__contains=search)|Q(city__contains=search)|Q(state__contains=search))
    dataSerializer = EmployeeSerializer(data,many=True)
    return HttpResponse(JSONRenderer().render(dataSerializer.data),content_type="applicate/json")
@csrf_exempt
def updateRecord(Request,id):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    try:
        emp = Employee.objects.get(id=id) 
        empSerilalizer = EmployeeSerializer(emp,data=pythonData,partial=True)
        if(empSerilalizer.is_valid()):
            empSerilalizer.save()
            msg = {"result":"Done","message":"Record is Updated!!!"}
        else:
            msg = {"result":"fail","message":"invalid Record!!!"}
    except:
        msg = {"result":"Fail","message":"Invalid id!!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")

def deleteRecord(Request,id):
    try:
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {"result":"Done","message":"Record is Delete!!!"}
    except:
        msg = {"result":"Done","message":"id not valid!!!"}
    return HttpResponse(JSONRenderer().render(msg),content_type="application/json")