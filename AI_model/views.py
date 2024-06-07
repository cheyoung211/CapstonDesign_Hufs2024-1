from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from PIL import Image
import pickle

class homeimport(TemplateView):
    template_name = 'home.html'

class WoundPredictionView(View):
    def post(self, request):
        
        '''분류할 사진을 input으로 받아와 사진에 해당하는 상처 종류 반환'''

        try:
            #upload된 파일 가져오기
            img_file = request.FILES['wound_image']
            image = Image.open(img_file).convert('RGB')
            
            #train된 모델 import
            load_model = pickle.load(open('model.plk','rb'))

            #prediction_dict
            prediction_dict = [{'찰과상':'url',
                                '멍':'url',
                                '화상':'url',
                                '배':'url',
                                '내성발톱':'url',
                                '열상':'url',
                                '자상':'url'}]
            
            #예측
            prediction = load_model.predict(image)
            pretictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
                'prediction_url' : prediction_dict[prediction]
                }
            

        except Exception as e:
            predictions = {
                'error' : '1',
                'message' : str(e)
                }

        return Response(predictions)
            
