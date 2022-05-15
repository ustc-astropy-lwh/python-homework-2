import torchvision.models as models
from torchinfo import summary
import torch.nn as nn

resnet_change_out_f = models.resnet18(pretrained=False)
resnet_change_out_f.fc = nn.Sequential(nn.Linear(in_features=512,out_features=200))
summary(resnet_change_out_f, (1, 3, 64, 64)) # 1：batch_size 3:RGB 224: width height

# models.resnet18().fc = nn.Sequential(nn.Linear(in_features=512,out_features=200))

# print(resnet_change_out_f)


