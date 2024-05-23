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
#from pl.loggers import TensorBoardLogger

dataset_path = 'C:/Users/MATH-1/python_file/data_file/Wound_dataset'
root_path = 'C:/Users/MATH-1/python_file/data_file/'

train_img_list, train_label_list, test_img_list, test_label_list = data_prepare(dataset_path, root_path)

#early_stop_callback = EarlyStopping(monitor='val_loss', mode ='min', patience=5)
#logger = TensorBoardLogger('tb_logs', name = 'ViT')

#모델 선언
model = VIT_Encoder()
trainer = pl.Trainer(max_epochs=50, log_every_n_steps = 20, devices=1, accelerator="gpu")#,val_check_interval = 0, callbacks=[early_stop_callback])
train_dataloader, test_dataloader = dataloader(train_label_list, test_label_list, train_img_list, test_img_list)  #dataloader
trainer.fit(model, train_dataloaders = train_dataloader)
print('model train is finished')

trainer.test(dataloaders=test_dataloader)
print('model test is finished')


