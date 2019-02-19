import torch.nn as nn
import pretrainedmodels
from termcolor import colored


class ViewerFC(nn.Module):
    def forward(self, x):
        return x.view(x.size(0), -1)


class ResNet(nn.Module):
    def __init__(self, se, dw, layers, drop, ncls):
        super(ResNet, self).__init__()
        if layers == 18:
            model = pretrainedmodels.__dict__['resnet18'](num_classes=1000, pretrained='imagenet')
            print(colored('====> ', 'green') + 'Pre-trained resnet18 is used as backbone')
        elif layers == 34:
            model = pretrainedmodels.__dict__['resnet34'](num_classes=1000, pretrained='imagenet')
            print(colored('====> ', 'green') + 'Pre-trained resnet34 is used as backbone')
        elif layers == 50:
            if not se and not dw:
                bb_name = 'resnet50'
            elif se and not dw:
                bb_name = 'se_resnet50'
            else:
                bb_name = 'se_resnext50_32x4d'

            model = pretrainedmodels.__dict__[bb_name](num_classes=1000, pretrained='imagenet')
            print(colored('====> ', 'green') + f'Pre-trained {bb_name} is used as backbone')
        elif layers == 101:
            model = pretrainedmodels.__dict__['se_resnet101'](num_classes=1000, pretrained='imagenet')
            print(colored('====> ', 'green') + 'Pre-trained se-resnet101 is used as backbone')
        elif layers == 152:
            model = pretrainedmodels.__dict__['se_resnet152'](num_classes=1000, pretrained='imagenet')
            print(colored('====> ', 'green') + 'Pre-trained se-resnet152 is used as backbone')
        else:
            raise NotImplementedError

        self.encoder = list(model.children())[:-2]

        self.encoder.append(nn.AdaptiveAvgPool2d(1))
        self.encoder = nn.Sequential(*self.encoder)

        if drop > 0:
            self.classifier = nn.Sequential(ViewerFC(),
                                            nn.Dropout(drop),
                                            nn.Linear(model.last_linear.in_features, ncls))
        else:
            self.classifier = nn.Sequential(
                ViewerFC(),
                nn.Linear(model.last_linear.in_features, ncls)
            )

    def forward(self, x):
        x = self.encoder(x)
        x = self.classifier(x)
        return x
