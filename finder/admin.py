from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(HeadSymptoms)
admin.site.register(UpperbodySymptoms)
admin.site.register(BellySymptoms)
admin.site.register(PelvisSymptoms)
admin.site.register(OnlyArmSymptoms)
admin.site.register(HandSymptoms)
admin.site.register(OnlyLegSymptoms)
admin.site.register(FootSymptoms)