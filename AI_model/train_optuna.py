import torch
import torch.nn as nn
import torch.optim as optim
from timm import create_model
from tensorload import dataloader
import pickle
import os
import optuna

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
torch.set_float32_matmul_precision('medium')

class ViTClassifier(nn.Module):
    def __init__(self, num_classes):
        super(ViTClassifier, self).__init__()
        self.vit = create_model('vit_base_patch16_224', pretrained = True)
        self.vit.head = nn.Linear(self.vit.head.in_features, num_classes)

    def forward(self, x):
        return self.vit(x)
    
def get_list(file_name):
    with open(file_name, 'rb') as f:
        path_list = pickle.load(f)
    return path_list

train_img_list = get_list('train_img_list.pkl')
train_label_list = get_list('train_label_list.pkl')
test_img_list = get_list('test_img_list.pkl')
test_label_list = get_list('test_label_list.pkl')

def objective(trial):

    #HYPERPARAMETER
    BATCH_SIZE = trial.suggest_int('batch_size', 8, 32)
    NUM_EPOCHS = trial.suggest_int('epochs', 5, 20)
    LR = trial.suggest_loguniform('lr', 1e-5, 1e-1)
    NUM_CLASSES = 7

    train_dataloader, test_dataloader = dataloader(train_label_list, test_label_list, train_img_list, test_img_list, batch_size = BATCH_SIZE)  #dataloader

    model = ViTClassifier(NUM_CLASSES).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr = LR)

    for epoch in range(NUM_CLASSES):
        print(f'Epoch #{epoch} starting')
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

    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_dataloader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data,1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100*correct/total
    return accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)

print(f'Best trial: {study.best_trial.value}')
print(f'Best params: {study.best_trial.params}')
