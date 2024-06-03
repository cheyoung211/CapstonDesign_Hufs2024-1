from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import *


# Create your views here.

class finderimport(TemplateView):
    template_name = 'finder.html'

class Mapimport(TemplateView):
    template_name = 'map.html'

#머리
class HeadImport(TemplateView):
    template_name = 'head.html'

#상체
class UpperBodyImport(TemplateView):
    template_name = 'upperbody.html'
    
#머리+상체
class HeadUpperImport(TemplateView):
    template_name = 'headupper.html'

#배
class BellyImport(TemplateView):
    template_name = 'belly.html'

#골반
class PelvisImport(TemplateView):
    template_name = 'pelvis.html'

#배+골반
class BellyPelvisImport(TemplateView):
    template_name = 'bellypelvis.html'

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

# 이하 세부 부위별 Search
class HeadSearch(ListView):
    model = Disease
    template_name = 'head.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head_symptoms'] = HeadSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class UpperBodySearch(ListView):
    model = Disease
    template_name = 'upperbody.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upper_body_symptoms'] = UpperbodySymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class HeadUpperSearch(ListView):
    model = Disease
    template_name = 'headupper.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['head_upper_symptoms'] = HeadUpperSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class BellySearch(ListView):
    model = Disease
    template_name = 'belly.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['belly_symptoms'] = BellySymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class PelvisSearch(ListView):
    model = Disease
    template_name = 'pelvis.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pelvis_symptoms'] = PelvisSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class BellyPelvisSearch(ListView):
    model = Disease
    template_name = 'bellypelvis.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['belly_pelvis_symptoms'] = BellyPelvisSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context


class ArmSearch(ListView):
    model = Disease
    template_name = 'arm.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['only_arm_symptoms'] = OnlyArmSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context

class LegSearch(ListView):
    model = Disease
    template_name = 'leg.html'
    context_object_name = 'diseases'
    def get_queryset(self):
        symptoms = self.request.GET.getlist('symptoms') # 사용자 입력
        if not symptoms:
            return Disease.objects.none()
        symptom_matches = {}
        for symptom in symptoms:
            queries = [Q(**{f'Symptom_{i}': symptom}) for i in range(1, 18)] # Symptom 필드 검색
            combined_query = queries.pop(0)
            for query in queries:
                combined_query |= query         
            matching_diseases = Disease.objects.filter(combined_query)
            for disease in matching_diseases:
                if disease in symptom_matches:
                    symptom_matches[disease] += 1
                else:
                    symptom_matches[disease] = 1
        sorted_diseases = sorted(symptom_matches.items(), key=lambda x: x[1], reverse=True)
        top_diseases = [disease for disease, _ in sorted_diseases[:1]]
        return top_diseases
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['only_leg_symptoms'] = OnlyLegSymptoms.objects.all()
        context['selected_symptoms'] = self.request.GET.getlist('symptoms')
        return context
