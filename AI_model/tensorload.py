import torch
from torchvision import transforms
from PIL import Image
from torch.utils.data import TensorDataset
from torch import nn
from torch.utils.data import DataLoader

def load_images_as_tensors(image_list):
    tensors = []
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # 이미지 크기를 조정합니다. 필요에 따라 조절하세요.
        transforms.ToTensor()  # 이미지를 텐서로 변환합니다.
    ])
    for image_path in image_list:
        # 이미지 파일을 읽어옵니다.
        image = Image.open(image_path)
        # 이미지를 텐서로 변환합니다.
        tensor = transform(image)
        tensors.append(tensor)
    return torch.stack(tensors)


def dataloader(train_label_list, test_label_list, train_img_list, test_img_list, batch_size = 10):

    train_label_list = torch.LongTensor(train_label_list)
    test_label_list = torch.LongTensor(test_label_list)

    train_data = load_images_as_tensors(train_img_list)
    test_data = load_images_as_tensors(test_img_list)

    train_dataset = TensorDataset(train_data, train_label_list)
    test_dataset = TensorDataset(test_data, test_label_list)

    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle = True,)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size)

    return train_dataloader, test_dataloader


#project = nn.Conv2d(3, 192, kernel_size= 8, stride=8)

