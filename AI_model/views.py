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
            image = Image.open(img_file)
            image = image.resize((224,224))
            image_array = np.array(image).reshape(1,-1)
            
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
            predict = load_model.predict(image_array)
            prediction_result = prediction[0]


            #상처 분류 결과
            return JsonResponse({'result': prediction_result})
            

        except Exception as e:
            return JsonResponse({'error': str(e)}, status = 500})
            
