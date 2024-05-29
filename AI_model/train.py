import os
import shutil
import torch
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
torch.set_float32_matmul_precision('medium')
from models import VIT_Encoder
from tensorload import dataloader
from data_preprocessing import data_prepare
import pytorch_lightning as pl
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
import pickle
import time
#from pl.loggers import TensorBoardLogger

dataset_path = 'Your data path'
root_path = 'Path for new data'

#처음 학습시킬때만 아래 코드를 실행해서 파일을 저장
#train_img_list, train_label_list, test_img_list, test_label_list = data_prepare(dataset_path, root_path)

def get_list(file_name):
    with open(file_name, 'rb') as f:
        path_list = pickle.load(f)
    return path_list

train_img_list = get_list('train_img_list.pkl')
train_label_list = get_list('train_label_list.pkl')
test_img_list = get_list('test_img_list.pkl')
test_label_list = get_list('test_label_list.pkl')

#early_stop_callback = EarlyStopping(monitor='val_loss', mode ='min', patience=5)
#logger = TensorBoardLogger('tb_logs', name = 'ViT')

#모델 선언 & 훈련
model = VIT_Encoder()
trainer = pl.Trainer(max_epochs=2, log_every_n_steps = 20, devices=1, accelerator="gpu")#,val_check_interval = 0, callbacks=[early_stop_callback])
train_dataloader, test_dataloader = dataloader(train_label_list, test_label_list, train_img_list, test_img_list)  #dataloader
trainer.fit(model, train_dataloaders = train_dataloader)
print('model train is finished')

#test
trainer.test(dataloaders=test_dataloader)
print('model test is finished')

#모델 저장
timestamp = time.time()
lt = time.localtime(timestamp)
model_name = time.strftime('WoundCLF_%m%d%H%M%S.pkl', lt)
with open(model_name, 'wb') as fw:
    pickle.dump(model, fw)
