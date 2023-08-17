from django.db import models
from django.templatetags.static import static
from django import forms

# Create your models here.
class FreqList(models.Model):
    city_val = models.CharField(max_length=300)
    freq_val = models.FloatField(default=0.0)
    rf_pred = models.FloatField(default=0.0)

    def __str__(self):
      return self.city_val

# for future when users may want to add a city to a FreqList    
class City(models.Model):
	cityname = models.ForeignKey(FreqList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
	  return self.text