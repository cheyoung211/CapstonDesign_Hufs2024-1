from django.db import models

# Create your models here.

class Disease(models.Model):
    Disease = models.CharField(max_length=100)
    Symptom_1 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_2= models.CharField(max_length=100, null=True, blank=True)
    Symptom_3 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_4 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_5 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_6 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_7 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_8 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_9 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_10 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_11 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_12 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_13 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_14 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_15 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_16 = models.CharField(max_length=100, null=True, blank=True)
    Symptom_17 = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.Disease