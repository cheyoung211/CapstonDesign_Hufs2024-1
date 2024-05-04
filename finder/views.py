from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class finderimport(TemplateView):
    template_name = 'finder.html'

#머리
class HeadImport(TemplateView):
    template_name = 'head.html'

#상체
class UpperBodyImport(TemplateView):
    template_name = 'upperbody.html'

#배
class BellyImport(TemplateView):
    template_name = 'belly.html'

#골반
class PelvisImport(TemplateView):
    template_name = 'pelvis.html'

#팔
class ArmImport(TemplateView):
    template_name = 'arm.html'
    
class OnlyArmImport(TemplateView):
    template_name = 'onlyarm.html'
    
class HandImport(TemplateView):
    template_name = 'hand.html'

#다리
class LegImport(TemplateView):
    template_name = 'leg.html'

class OnlyLegImport(TemplateView):
    template_name = 'onlyleg.html'

class FootImport(TemplateView):
    template_name = 'foot.html'


# 머리, 상체, 복부, 골반, 팔, 다리
# 팔->팔과 손
# 다리->다리와 발
# 배->상중하
# 상체->목 어깨 가슴