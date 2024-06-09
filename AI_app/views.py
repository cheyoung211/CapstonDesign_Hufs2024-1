from django.shortcuts import render
from django.views.generic import TemplateView
import json
from .forms import UploadFileForm
from django.http import JsonResponse
from django.views import View
from .ai_model import load_model
import numpy as np
import torch
import io
from torchvision import transforms
from PIL import Image
import pickle
import torch
from timm import create_model
import torch.nn as nn

# Create your views here.
class aiimport(TemplateView):
    template_name = 'AI_app.html'

# class WoundPredictionView(View):
#     def post(self, request):

#         '''분류할 사진을 input으로 받아와 사진에 해당하는 상처 종류 반환'''

#         try:
#             #upload된 파일 가져오기
#             img_file = request.FILES['wound_image']
#             image = Image.open(img_file)
#             image = image.resize((224,224))
#             image_array = np.array(image).reshape(1,-1)

#             #train된 모델 import
#             model = jobbib.load('model.plk')

#             #예측
#             predict = model.predict(image_array)
#             prediction_result = prediction[0]

#             #상처 분류 결과
#             return JsonResponse({'result': prediction_result})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status = 500})

class ViTClassifier(nn.Module):
    def __init__(self, num_classes):
        super(ViTClassifier, self).__init__()
        self.vit = create_model('vit_base_patch16_224', pretrained = True)
        self.vit.head = nn.Linear(self.vit.head.in_features, num_classes)

    def forward(self, x):
        return self.vit(x)

def load_model():
    model_path = 'C:/Users/MATH-1/python_file/WoundCLF_0609124600.pkl'
    model = pickle.load(open(model_path,'rb'))
    return model

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def classify_image(image_path):
    
    model = load_model().to(device)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485,0.456,0.406], std = [0.229,0.224,0.225])
    ])

    image = Image.open(image_path)
    image_tensor = transform(image).unsqueeze(0).to(device)


    model.eval()
    with torch.no_grad():
        outputs = model(image_tensor)
        _,predicted = torch.max(outputs,1)

    clf_result = predicted.item()
    wound_dict = {0 : '찰과상',
                  1 : '멍',
                  2 : '화상',
                  3 : '베임',
                  4 : '내성장손발톱',
                  5 : '열상',
                  6 : '자상'}
    return wound_dict[clf_result]

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = settings.ROOT/file.name ####이 부분 확인 바랍니다.
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                result = classify_image(file_path)
                return render(request, 'ai_app/result.html', {'result':result})
    else:
        form = UploadFileForm()
    return render(request, 'ai_app/upload.html', {'form':form})