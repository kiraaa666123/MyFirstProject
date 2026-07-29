try:
    weight = int(input("身高："))
    height = int(input("体重："))
    f = open("sfsdf")
    ans = weight/height
    print(ans)
except ZeroDivisionError:
    print("除零错误")
except:
    print("有错误")
else:
    print(ans)
finally:
    print("程序结束")


print("hhh")



class MyCounter:
    def __init__(self,a,b):
        '''a与b就相当于add函数和sub函数的公共变量，解决了一个函数内的局部变量无法在另一个函数内使用的情况'''
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

class MyCounter2(MyCounter):
    def __init__(self,a,b):
        super().__init__(a,b)
        '''一个类只能继承一个父类，如果要使用多个类的方法，可以在init里创建其他类的对象，然后通过对象调用方法'''
        self.test = MyCounter(a,b)

    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
test_2 = MyCounter2(1,2)
print(test_2.test.add())