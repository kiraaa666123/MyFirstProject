
list_a = ["键盘","鼠标"]
list_a.append("显示器")
list_a.remove("鼠标")
print(list_a)

list_b = ["苹果",123,66.6,True,None]    #list可以放不同数据类型的数据
print(list_b)

len(list_b)    # list也可以使用len，返回的是列表里元素的个数

list_b[1] = 666    #list也可以用下标来访问第几个元素，从零开始
print(list_b)

list_c = []
list_c.append("你")
list_c.append("我")
print(list_c)
print(list_c[1])


price = [100,200,1024,666]
print(max(price))
print(min(price))
price_sorted = sorted(price)
print(price_sorted)


list_d = [1,2,3,4,5]
print(list_d[-1],list_d[-2],list_d[-3])  # 列表的-1项为倒数第一项，-2项为倒数第二项


#  切片
print(list_d[1:4])  # 从索引[1]开始，切到索引[4]之前
print(list_d[1:])
print(list_d[:4])
cut_d = list_d[1:]  # 切片也可以赋值个一个新的变量

print(list_d[::2])  # 每两个元素采样一次
print(list_d[1:-1:2])  # 从索引[1]开始，切到索引[-1]之前，每两个元素采样一次

print(list_d+[6])
list_d = list_d+[6]
print(list_d)


list_d = [1,2,3,4,5]
cut = list_d[:4]
cut[1] = 666
print(list_d)
print(cut)    # list切片是与list相互独立的，这点与数组不同

