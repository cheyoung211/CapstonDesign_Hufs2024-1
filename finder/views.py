from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q, Count, Case, When, IntegerField
from .models import *


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


class HeadSearch(ListView):
    model = Disease
    template_name = 'head.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        # 사용자 입력 받기
        symptoms = self.request.GET.getlist('symptoms')
        if not symptoms:
            return Disease.objects.none()
        # 각 증상별로 모든 Symptom 필드 검색
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}__icontains': symptom}) for i in range(1, 18)]
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query  # OR 연산으로 모든 Symptom 필드에 대해 쿼리           
            # 일치하는 질병 찾기
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        # 일치 횟수에 따라 질병 정렬 후 상위 3개 반환
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:3]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head_symptoms'] = HeadSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context