def add(a,b,c,d):
    print(f"四者相加为：{a + b + c + d}")
    print("四者相加为：" + str(a + b + c + d))
    return a + b + c + d    # 没有return的时候默认return None


add(10,20,30,40)


def my_counter(a,b):
    '''加法器和乘法器'''
    return a+b,a*b
x,y=my_counter(10,20)
print(x,y)

def menu(*args):
    '''可以传入任意多个参数,返回元组'''
    return args
print(menu(1,2,3,4,5))

def hobbies(name,*hobby):
    return name,hobby
name,hobby = hobbies("cxk",'dance','sing','rap','basketball')
print(f"{name}喜欢{hobby}")


def evaluate(num1,num2,**kwargs):
    '''**kwargs自动创建了一个字典'''
    kwargs['xiaoming'] = num1
    kwargs['xiaozhang'] = num2
    return kwargs
list = evaluate(100,90)
print(list)
list = evaluate(100,90,xiaohong = 80,xiaolan = 70)
print(list)

def school(name,level = 1):    # 函数定义形参的时候可以设置默认值，然后如果传参的时候没传该参数，则使用默认值
    return f"{name}是{level}级"      
