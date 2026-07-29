import matplotlib.pyplot as plt
import torch
from _18_2_DNN import DNN
import numpy as np
from torch import nn

new_model = torch.load('DNN.pth')
tensor_x = torch.Tensor([[1,0.2,0.3]]).to('cuda:0')
print(tensor_x.shape)
ans = new_model(tensor_x)
print(ans)

Fig1 = plt.figure()
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y)
plt.show()

Fig1.savefig('test_photo.svg')





