from django.db import models
from django.utils import timezone
# Create your models here.
class  Visitors(models.Model):
    name = models.CharField(max_length = 150)
    temperature = models.DecimalField(max_digits = 3, decimal_places = 1)
    company = models.CharField(max_length = 150)
    id_number = models.CharField(max_length=150, blank = True)
    telephone_number = models.IntegerField()
    # date = models.DateField('date captured')
    date = models.DateField(default=timezone.now)

def __str__(self):
    return self.name

# class Register(models.Model):
#     visitor = models.ForeignKey(Visitors,on_delete=models.CASCADE)
#     temperature = models.IntegerField()
#     date = models.DateTimeField(auto_now=True)

