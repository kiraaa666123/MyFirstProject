import pandas as pd
import numpy as np
'''pandas为标签库，类似字典，创建的叫做对象（类比numpy创建的叫做数组）'''

'''对象的创建'''

#先定义键和值
v=[0,0.25,0.5,0.75,1]
v=np.array(v) #用列表或数组都可以
k=['a','b','c','d','e']
k=np.array(k)
sr=pd.Series(v,k)
print(sr)

# sr=pd.Series(v) #如果没有定义键，默认0，1，2...
# print(sr)

#输出values属性与index属性，都是以数组来输出的，所以pandas库是建立在numpy库基础上的
print(sr.values)
print(sr.index)

'''创建值对应多项的对象'''
v=[[90,'数学'],[100,'语文'],[95,'英语']]
k=['a','b','c'] #每一行的标签
c=['成绩','科目'] #columns,即每一列的标签
df=pd.DataFrame(v,k,c)
print(df)
print(df.values) #单独访问values时，输出一个数组，pandas就退化为了numpy

arr = df.values[:,0].astype(int)
print(arr)


'''对象的索引'''
#访问元素
sr.loc['a'] #按键来显式访问
sr.iloc[1] #隐式访问第二个元素
sr.loc['a']=10

#切片
sr.loc['a':'c'] #这个是左闭右闭

print(df.loc[['a','b','c'],['科目','成绩']])


print(pd.read_csv('data.csv'))
print(pd.read_csv('data.csv').describe())
