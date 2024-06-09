import torch
import torch.nn as nn
import torch.optim as optim
from timm import create_model
from tensorload import dataloader
import pickle
import os
import time

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
torch.set_float32_matmul_precision('medium')

# 최적의 하이퍼파라미터로 모델 학습
BATCH_SIZE = 23
NUM_EPOCHS = 18
LR = 2.4829065579754252e-05
NUM_CLASSES = 7

def get_list(file_name):
    with open(file_name, 'rb') as f:
        path_list = pickle.load(f)
    return path_list

#저장된 데이터 path 가져오기
train_img_list = get_list('train_img_list.pkl')
train_label_list = get_list('train_label_list.pkl')
test_img_list = get_list('test_img_list.pkl')
test_label_list = get_list('test_label_list.pkl')

# 데이터 로더 생성
train_dataloader, test_dataloader = dataloader(train_label_list, test_label_list, train_img_list, test_img_list, batch_size=BATCH_SIZE)

class ViTClassifier(nn.Module):
    def __init__(self, num_classes):
        super(ViTClassifier, self).__init__()
        self.vit = create_model('vit_base_patch16_224', pretrained = True)
        self.vit.head = nn.Linear(self.vit.head.in_features, num_classes)

    def forward(self, x):
        return self.vit(x)

# 모델, 손실 함수 및 옵티마이저 설정
model = ViTClassifier(NUM_CLASSES).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# 모델 학습
for epoch in range(NUM_EPOCHS):
    model.train()
    running_loss = 0.0
    for images, labels in train_dataloader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f'Epoch {epoch+1}/{NUM_EPOCHS}, Loss: {running_loss/len(train_dataloader)}')


# 모델 평가
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_dataloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy: {100 * correct / total}%')

timestamp = time.time()
lt = time.localtime(timestamp)
model_name = time.strftime('WoundCLF_%m%d%H%M%S.pkl', lt)
with open(model_name, 'wb') as fw:
    pickle.dump(model, fw)
