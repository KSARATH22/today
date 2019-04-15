from django.db import models
class EmpData(models.Model):
    id=models.IntegerField()
    emp_name=models.CharField(max_length=60)
    loction=models.CharField(max_length=60)
    salary=models.IntegerField()
    def __str__(self):
        return self.emp_name
