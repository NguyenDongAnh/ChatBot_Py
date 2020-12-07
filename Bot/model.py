import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.m = nn.Dropout(p=0.5)
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.tanh = nn.Tanh()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.tanh(out)
        out = self.m(self.l2(out))
        out = self.tanh(out)
        out = self.m(self.l3(out))
        # no activation and no softmax at the end
        return out