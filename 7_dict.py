dict_1 = {"xiaoming":23,"xiaohong":18}
# dict,字典,就是键值对，也是可变的，可以增加和移除

print(dict_1["xiaoming"])    #通过键来寻找值

# 列表不能作为键，因为列表是可变的，键必须是不可变的

# tuple叫做元组，可以放任意个元素，和列表的区别是元组不可变，不能用append和remove
tuple_1 = ("zhangwei",25)
tuple_2 = ("zhangwei",23)
tuple_3 = ("zhangwei",28)
len(tuple_1)

dict_2 = {tuple_1:"1234567",
          tuple_2:"6666666",
          tuple_3:"0000000"}
#这样就可以区分同名字的键的情况，如同名字都叫张伟但年龄不一样
print(dict_2[("zhangwei",25)])
print(dict_2[tuple_1])

#增加字典名
dict_1["xiaofang"] = 20

#删除字典名
del dict_1["xiaoming"]

#看键是否存在
print("xiaoming" in dict_1)

if "xiaoming" in dict_1:
    print("存在")

len(dict_1)

nothing = {}    #一个空的大括号默认是空字典而不是空集合，因为python中字典使用的概率远高于集合


dict_3 = {
    0:"hhh",
    1:222,
    2:True,
    3:(6,6,6)
}
print(dict_3)
#  字典的值可以是任意类型，但字典的键只能是字符串或数字
#  一般用到字典的时候，索引一般都是字符串




