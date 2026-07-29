greeting = "hello what's up bro"

str_1 = "hello" + "world"

print(greeting + "张三")

#python变量命名的规定：字母全部小写，不同单词之间用下划线分割


#注释用#，多行注释用***
"""
这
是
多
行
注释
"""

num = 111

print(num)

print(f"hello {num}")


name = "lili"
len(name)    #len求变量长度,只能用在字符串上
print(len(name))

name[2]    #字符串后面跟[]可以当做类似于数组用
print(name[1])
print(name[0])

b1 = True
b2 = False
print(b1)
print(b2)


n = None   # 空指类型


print(type(n))
print(type(b1))
print(type(name))
print(type(1.5))
print(type(1))


x = "悲"
print(f"""
空
{x}
切
""")


a,b,c = 1,2,3  # 元组赋值法
b,a = a,b  # 快速交换变量的值
values = 1,2,3,4,5,6  # 这是把括号省略了的元组
print(values)
a,b,*rest = values  # a获得1，b获得2，rest获得一个3，4，5，6的列表
print(rest)
tuple_x = (1,"b",True,(1,2,3),[1,2,"hhh"])  # 元组可以是任意元素相互组成

x_2 = f"{x}tianminren"
print(x_2)
