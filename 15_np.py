# 该文件用于学习numpy数组

import numpy as np

import numpy as np
# print(np.__version__)

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x))
# plt.show()


# import time
# from tqdm import tqdm
#
# print("开始处理数据，请稍候...")
#
# # 模拟一个处理 100 个任务的循环
# for i in tqdm(range(100), desc="处理进度"):
#     # 这里假装在做一些耗时的工作（比如计算、读取数据）
#     time.sleep(0.05)  # 暂停 0.05 秒
#
# print("任务全部完成！🎉")


arr1 = np.array([1,2,3])
print(arr1)

arr2 = arr1.astype(float)
print(arr2)

print(arr1+0.0)
print(arr1*1.0)

print(arr1/1)   # 不管除的是整型还是浮点型，arr1都转化为浮点型，结果也都为浮点型

arr1 = np.ones(3)    # 一维数组
arr2 = np.ones((2,3))    # 二维数组，两行三列

print(arr1)
print(arr2)

arr1 = np.ones(10)
arr2 = arr1.reshape((2,5))    # 一维数组转二维
print(arr2)

arr2 = np.ones((5,3))
arr1 = arr2.reshape(15)    # 二维数组转一维数组
print(arr1)

'''创建指定数组'''
arr2 = np.array([[1,2,3]])    # 一行三列矩阵
arr2 = np.array([[1],[2],[3]])    # 三行一列矩阵

arr2 = np.array([[1,2,3],[2,3,4],[3,4,5]])

'''创建递增数组'''
# 整数
#arange生成的都是一维数组，要生成二维的就要用reshape
arr1 = np.arange(10)    # 0到9
arr2 = np.arange(0,11,2)    # 0到10中，步长为2
arr2 = np.arange(-1,-9,-1)
# 浮点数
arr1 = np.arange(10.0)    # 0到9
arr2 = np.arange(0,11,2.0)    # 0到10中，步长为2

'''创建同值数组（创建出来都是浮点型的）'''
arr1 = np.zeros(10)    # 十个零的一维数组
arr2 = np.ones((1,3))    # 全为一的一行三列二维数组
arr2 = 3.14*np.ones((2,3))    # 全为3.14的二行三列二维数组

'''创建随机数组（浮点数）'''
arr1 = np.random.random(10)    # 10个随机的0-1之间的数
#如果想输入60到100之间的随机数
arr2 = (100-60)*np.random.random((2,3)) + 60
#如果要整数型的
arr2 = (100-60)*np.random.random((2,3)) + 60
arr2 = arr2.astype(int)
#服从正太分布的随机数组
arr2 = np.random.normal(0,1,(2,3))   # 参数分别为均值和标准差

'''索引'''
arr1 = np.array([1,2,3])
print(arr1[1])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2[1,1])

'''修改'''
arr2[1,1] = 100.9    # 将浮点型放到整形数组中，会被截断

'''花式索引'''
arr1 = np.array([1,2,3])
print(arr1[[0,2]])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2[[0,2],[1,2]])    # 花式索引输出的是向量
arr2[[0,2],[1,2]] = 100    # 批量修改
print(arr2)

'''向量的切片'''
print(arr1[1:3])   # 数组的切片还是数组
print(arr1[::2])   # 步长为2

'''矩阵的切片'''
arr2 = np.arange(1,21).reshape(4,5)
print(arr2)
print(arr2[1:3,1:-1])
print(arr2[::3,::2])

'''提取某一行'''
print(arr2[2,:])
'''提取某一列'''
print(arr2[:,2])    # 输出的仍然是个向量（原本是个四行一列的矩阵的，但为了节省空间）
print((arr2[:,2]).reshape((-1,1)))

'''数组的切片仅是视图，并不会创建新的变量，仅仅是在原数组上进行切片'''
arr1 = np.arange(0,10)
cut = arr1[:2]
cut[1] = 100
print(arr1)

'''arr1 = arr2 后，str1与str2也不是相互独立的（类似于c语言中将=传递地址）'''
arr2 = arr1
arr2[2] = 666
print(arr1)


'''数组的翻转'''
#向量
arr1 = np.arange(10)
arr1 = np.flipud(arr1)
print(arr1)

#矩阵
arr2 = np.arange(20).reshape(4,5)
print(np.fliplr(arr2)) #左右翻转
print(np.flipud(arr2)) #上下翻转


'''数组的拼接'''
arr11 = np.array([1,2,3])
arr12 = np.array([4,5,6])
arr = np.concatenate([arr11,arr12])
print(arr)

arr21 = np.array([[1,2,3],[4,5,6]])
arr22 = np.array([[7,8,9],[10,11,12]])
arr = np.concatenate([arr21,arr22]) #axis默认值为0，对行进行操作，为竖着拼接
print(arr)

arr = np.concatenate([arr21,arr22],1) #axis值为1，为横着拼接
print(arr)

'''矩阵的分裂'''
#向量
arr = np.arange(10)
arr1,arr2,arr3 = np.split(arr,[2,5])
print(arr1,arr2,arr3)
#矩阵
arr = np.arange(12).reshape(3,4)
arr1,arr2,arr3 = np.split(arr,[1,3],1)
print(arr1,'\n',arr2,'\n',arr3)


'''向量的广播（行矩阵广播），列矩阵广播同理'''
arr1 = np.array([100,0,-100])
arr2 = np.random.random((10,3))
print(arr1*arr2)


'''矩阵相乘'''
arr1 = np.arange(10).reshape(2,5)
arr2 = np.arange(15).reshape(5,3)
print(np.dot(arr1,arr2))

'''数学函数'''
arr = np.array([1,2,-3])
print(np.abs(arr)) #绝对值

theta = np.arange(3)*np.pi/2 #这块仍然是一个数组
sin_v = np.sin(theta)
cos_v = np.cos(theta)
tan_v = np.tan(theta)

x = np.arange(1,5)
np.exp(x) #指数函数
np.log(x) #对数ln
#对于以其他为底的对数,用换底公式
#比如
np.log(x)/np.log(2)

'''聚合函数'''
arr = np.random.random((2,3))
np.max(arr,0) #比较行的最大，最后得到一行
np.min(arr,1)  #比较列的最小，最后得到一列
np.max(arr) #如果没有参数，会找到整体中的一个最大值

'''求和函数与求积函数'''
np.sum(arr,0) #按行求和，最后得到一行
np.sum(arr,1) #按列求和，最后得到一列
np.sum(arr) #整体求和，最后得到一个数
#求积同理，为prod

'''均值函数与标准差函数'''
np.mean(arr,0) #按行求均值，最后得到一行
np.mean(arr,1) #按列求均值，最后得到一列
np.mean(arr) #整体求均值
#求标准差为std


'''构造布尔数组'''
arr = np.arange(1,7).reshape(2,3)
print(arr>=4)

arr1 = np.arange(1,6)
arr2 = np.flipud(arr1)
print(arr1>arr2)

#多个条件
print((arr<2)|(arr>4))

'''统计数组中的true'''
#sum
arr = np.random.normal(0,1,10000)
num = np.sum(np.abs(arr)<1)
print(num) #概率应该接近于0.6827

#any
arr1 = np.arange(1,10)
arr2 = np.flipud(arr1)
print(np.any(arr1==arr2)) #只要有一个相等的，就输出true

#all
arr = np.arange(1,10)
print(np.all(arr>5))

'''布尔数组的掩码作用'''
arr1 = np.arange(1,10)
arr2 = np.flipud(arr1)
print(arr1[arr1>arr2])

'''找到数组中的元素的位置'''
arr = np.random.normal(500,60,1000)
#np.where输出的是一个元组，第一个元素是数据，第二个元素是数据类型，不想输出数据类型的就加个[0]就好了
print(np.where(arr>650)[0])
print(np.where(arr==np.max(arr))[0])
#打印出来的都是索引
