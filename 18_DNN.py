import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

#生成数据集
X1=torch.rand(100000,1)#输入特征1
print(X1)
X2=torch.rand(100000,1)#输入特征2
X3=torch.rand(100000,1)#输入特征3
Y1=( (X1+X2+X3)<1).float()#输出特征1
Y2=( (1<(X1+X2+X3))&((X1+X2+X3)<2) ).float()#输出特征2
Y3=( (X1+X2+X3)>2).float()#输出特征3
Data=torch.cat([X1,X2,X3,Y1,Y2,Y3],1)#整合数据集
Data=Data.to('cuda:0')#把数据集搬到GPU上
print(Data.shape)

#划分训练集与测试集
train_size=int(len(Data)*0.9)#训练集的样本数量
test_size=len(Data)-train_size#测试集的样本数量
Data = Data[torch.randperm(Data.size(0)),:]#打乱样本的顺序
train_Data=Data[:train_size,:]#训练集样本
test_Data=Data[train_size:,:]#测试集样本

class DNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 5),nn.ReLU(),
            nn.Linear(5, 5),nn.ReLU(),
            nn.Linear(5, 5),nn.ReLU(),
            nn.Linear(5, 3)
        )

    def forward(self, x):
        return self.net(x)

model=DNN().to('cuda:0')#创建子类的实例，并搬到GPU上

#损失函数的选择
loss_fn=nn.MSELoss()

#优化算法的选择
learning_rate=0.01#设置学习率
optimizer=torch.optim.SGD(model.parameters(), learning_rate)


#训练网络
epochs=100000
losses=[]#记录损失函数变化的列表
#给训练集划分输入与输出
X=train_Data[:, :3]#前3列为输入特征
Y=train_Data[:,-3:]#后3列为输出特征
for i in range(epochs):
    Pred=model(X)#一次前向传播（批量）
    loss=loss_fn(Pred, Y)#计算损失函数
    losses.append(loss.item())#记录损失函数的变化
    optimizer.zero_grad()#清理上一轮滞留的梯度
    loss.backward()#一次反向传播
    optimizer.step()#优化内部参数


Fig=plt.figure()
plt.plot(range(epochs), losses)
plt.ylabel('loss'),plt.xlabel('epoch')
plt.show()


# 测试网络
# 提取测试集的输入与输出
X_test = test_Data[:, :3]   # 前3列为输入特征
Y_test = test_Data[:, -3:]  # 后3列为输出特征（One-Hot标签）

# 不计算梯度，节省显存并加速
with torch.no_grad():
    Pred_test = model(X_test)                     # 前向传播，得到 (N, 3) 的分数
    pred_indices = torch.argmax(Pred_test, 1) # 预测类别索引 (N,)
    true_indices = torch.argmax(Y_test, 1)    # 真实类别索引 (N,)
    correct = (pred_indices == true_indices).sum().item()  # 正确预测的样本数
    total = Y_test.size(0)                         # 总样本数
    accuracy = 100 * correct / total

print(f'测试集准确率: {accuracy:.2f}%')

torch.save(model, 'DNN.pth')