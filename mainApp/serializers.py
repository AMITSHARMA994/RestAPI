from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    dsg = serializers.CharField(max_length=30)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)

    def create(self,validatedData):
        return Employee.objects.create(**validatedData)

    def update(self,instance,validatedData):
        if("name" in validatedData and validatedData["name"]!=""):
            instance.name = validatedData['name']
        if("dsg" in validatedData and validatedData["dsg"]!=""):
            instance.dsg = validatedData['dsg']
        if("salary" in validatedData and validatedData["salary"]!=""):
            instance.salary = validatedData['salary']
        if("city" in validatedData and validatedData["city"]!=""):
            instance.city = validatedData['city']
        if("state" in validatedData and validatedData["state"]!=""):
            instance.state = validatedData['state']
        instance.save()
        return instance
    