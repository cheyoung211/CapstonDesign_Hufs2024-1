import os
import shutil
from augmentation import data_augmentation
import pickle

def save_list(list_name, file_name):
    with open(file_name,'wb') as f:
        pickle.dump(list_name,f)
        

def data_prepare(dataset_path, root_path):

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

    #증강된 이미지를 list에 넣기
    for idx, l in enumerate(labels):
        tmp_image_name_list = os.listdir(dataset_path+'/'+l)
        for cnt, fname in enumerate(tmp_image_name_list):
            if 'aug' in fname:
                dst_path = os.path.join(root_path, 'data/train/', l, fname)
                #shutil.copy(dataset_path+'/'+l+'/'+fname, dst_path)
                train_img_list.append(dst_path)
                train_label_list.append(idx)
    
    save_list(train_img_list,'train_img_list.pkl')
    save_list(train_label_list, 'train_label_list.pkl')
    save_list(test_img_list, 'test_img_list.pkl')
    save_list(test_label_list, 'test_label_list.pkl')

    return train_img_list, train_label_list, test_img_list, test_label_list
