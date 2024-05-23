import torch
import numpy as np
from torch import nn
from torch.utils.data import DataLoader, random_split
from torch.utils.data import TensorDataset
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor, Lambda
import torchmetrics
import pytorch_lightning as pl

class EmbeddingLayer(nn.Module):
    def __init__(self,in_chan, img_size, patch_size, batch_size=10):
        super().__init__()
        self.num_patches = int(img_size / pow(patch_size, 2)) # 784
        self.emb_size = in_chan * patch_size * patch_size # 192
        self.project = nn.Conv2d(in_chan, self.emb_size, kernel_size= patch_size, stride=patch_size)
        self.cls_token = nn.Parameter(torch.randn(1,1,self.emb_size))
        self.positions = nn.Parameter(torch.randn(self.num_patches+ 1, self.emb_size)) # [785,192]


    def forward(self, x):
        x = self.project(x)
        x = x.view(-1, 784, 192) # [batch_size, 49, 16]
        repeat_cls = self.cls_token.repeat(x.size()[0],1,1) #[batch_size, 1 , 16]
        x = torch.cat((repeat_cls, x), dim=1)
        x += self.positions
        return x

class Multihead(nn.Module):
    def __init__(self, emb_size, num_heads):
        super().__init__()
        self.multiheadattention = nn.MultiheadAttention(emb_size, num_heads, batch_first = True, dropout=0.2)
        self.query = nn.Linear(emb_size, emb_size)
        self.key = nn.Linear(emb_size, emb_size)
        self.value = nn.Linear(emb_size, emb_size)

    def forward(self, x):
        query = self.query(x)
        key = self.key(x)
        value = self.value(x)
        attn_output, attention = self.multiheadattention(query, key, value)
        return attn_output, attention

class FeedForwardBlock(nn.Sequential):
    def __init__(self, emb_size, expansion = 4, drop_p = 0.2):
        super().__init__(
            nn.Linear(emb_size, expansion * emb_size),
            nn.GELU(),
            nn.Dropout(drop_p),
            nn.Linear(expansion * emb_size, emb_size)
        )

class VIT(nn.Module):
    def __init__(self,emb_size = 192):
        super().__init__()
        self.embedding_layer = EmbeddingLayer(3, 224*224, 8)
        self.Multihead = Multihead(emb_size, 8)
        self.FFB = FeedForwardBlock(emb_size)
        self.norm = nn.LayerNorm(emb_size)

    def forward(self, x):
        x = self.embedding_layer(x)

        norm_x = self.norm(x)
        multihead_output, attention = self.Multihead(norm_x)

        #residual Function
        output = multihead_output + x

        norm_output = self.norm(output)
        FFB = self.FFB(norm_output)

        final_out = FFB + output

        return final_out, attention

class TransformerEncoder(nn.Module):
    def __init__(self, n_layers: 5, ):
        super().__init__()
        self.layers = nn.ModuleList([VIT() for _ in range(n_layers)])

    def forward(self, x):
        for layer in self.layers:
            final_out, attention = layer(x)

        return final_out

ac = torchmetrics.Accuracy(task="multiclass", num_classes = 7).to('cuda')

class VIT_Encoder(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.loss = []
        self.Encoder = nn.Sequential(
            TransformerEncoder(n_layers = 5),
            #Reduce('b n e -> b e', reduction='mean')
        )
        self.final_layer = nn.Linear(192, 7)
        self.val_loss = []
        self.acc = []
        self.test_acc =[]

    def forward(self, x):
        x = self.Encoder(x)
        cls_token_final = x[:,0]
        #(cls_token_final.shape)
        cls_token_final = self.final_layer(cls_token_final)
        return cls_token_final

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = nn.CrossEntropyLoss()(logits,y)
        preds = torch.argmax(logits, dim = 1)
        acc = torch.mean((preds == y).float())
        self.log('train_loss', loss, on_step = True, on_epoch = True, prog_bar = True, logger = True)
        self.log('train_acc', acc, on_step = True, on_epoch = True, prog_bar = True, logger = True)

        #self.loss.append(loss.item())
        return loss

    def on_train_epoch_end(self):
        mean_loss = sum(self.loss) / 37
        print(f'traing_loss :{mean_loss}')
        self.loss = []
        self.acc = []

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = nn.CrossEntropyLoss()(logits,y)
        self.val_loss.append(loss.item())
        acc = ac(logits, y)
        self.acc.append(acc)
        return loss

    def on_validation_epoch_end(self):
        mean_loss = sum(self.val_loss) / 40
        mean_acc = sum(self.acc)/ 40
        print(f'val loss :{mean_loss}, val_acc : {mean_acc}')

        self.val_loss = []
        self.acc = []
        self.log("val_loss", mean_loss)

    #def test_dataloader(self):
    #    return test_dataloader


    def test_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        acc = ac(logits, y)
        self.test_acc.append(acc)

    def on_test_epoch_end(self):
        mean_acc = sum(self.test_acc)/10
        print('mean_acc:',mean_acc)


    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)