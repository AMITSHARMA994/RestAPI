from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    dsg = models.CharField(max_length=30)
    salary = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)


    def __str__(self):
        return str(self.id)+" "+self.name