import os
import shutil
import torch
from models import VIT_Encoder
from tensorload import dataloader
import pytorch_lightning as pl
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from augmentation import data_augmentation

dataset_path = 'Your data path'
root_path = 'Path for new data'

#data를 train, test용으로 나눌 폴더 만들기
os.makedirs(root_path+'data/', exist_ok=True)
os.makedirs(root_path+'data/train/', exist_ok=True)
os.makedirs(root_path+'data/val/', exist_ok=True)

labels = os.listdir(dataset_path)

for l in labels:
    os.makedirs(root_path+'data/train/'+l, exist_ok=True)
    os.makedirs(root_path+'data/val/'+l, exist_ok=True)

labels_cnt_list = []

for l in labels:
    labels_cnt_list.append(len(os.listdir(dataset_path+'/'+l)))

train_img_list = []
train_label_list = []
test_img_list = []
test_label_list = []

#데이터 나눠서 폴더에 넣기
for idx, l in enumerate(labels):
    num_train = int(labels_cnt_list[idx] * 0.85)
    tmp_image_name_list = os.listdir(dataset_path+'/'+l)
    for cnt, fname in enumerate(tmp_image_name_list):
        if cnt <= num_train:
          dst_path = os.path.join(root_path, 'data/train/', l, fname)
          shutil.copy(dataset_path+'/'+l+'/'+fname, dst_path)
          train_img_list.append(dst_path)
          train_label_list.append(idx)
        else:
          dst_path = os.path.join(root_path, 'data/val/', l, fname)
          shutil.copy(os.path.join(dataset_path, l, fname), dst_path)
          test_img_list.append(dst_path)
          test_label_list.append(idx)

train_data_path = 'C:/Users/MATH-1/python_file/data_file/data/train'
data_augmentation(train_data_path, augcount = 5) #데이터 증강

early_stop_callback = EarlyStopping(monitor='val_loss', mode ='min', patience=5)

#모델 선언
model = VIT_Encoder()
trainer = pl.Trainer(max_epochs=2, devices=1, accelerator="gpu",val_check_interval = 0, callbacks=[early_stop_callback])
train_dataloader = dataloader(train_label_list, test_label_list)  #dataloader
trainer.fit(model, train_dataloaders = train_dataloader)



