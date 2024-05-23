import cv2
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow.keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def data_augmentation(train_data_path, augcount):
    '''
    데이터 증강을 해주는 함수
    train_data_path : train data가 있는 경로
    augcount : 증강된 이미지 수
    '''

    datagen = ImageDataGenerator(
        rotation_range=60,
        width_shift_range=0.4,
        height_shift_range=0.4,
        shear_range=0.4,
        zoom_range=0.4,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    for folder in os.listdir(train_data_path):
        folder_path = os.path.join(train_data_path, folder)
        if os.path.isdir(folder_path):
            # 폴더 내 모든 이미지 파일 순회
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                    img_path = os.path.join(folder_path, filename)
                    img = cv2.imread(img_path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = img.reshape((1,) + img.shape)  # 모델의 입력 형태로 이미지를 변환 (batch_size=1)

                    # 이미지 증강 및 저장
                    i = 0
                    for batch in datagen.flow(img, batch_size=1, save_to_dir=folder_path, save_prefix='aug', save_format='jpg'):
                        i += 1
                        if i >= augcount:  # 증강된 이미지의 수 (원하는 수로 조절 가능)
                            break  # 무한 루프를 방지하기 위해 종료