
user_age = input("What is your age:")    #input接收到的东西赋值给变量的时候一律为字符串类型
print("你的年龄是：" + user_age)

print("你的年龄是" + str(8) + "岁")    #数字不能和字符串一起输出，必须要将数字先转化为字符串才行
print("你的年龄是",8,"岁")

#同理，input接收到的都是字符串类型，如果要转化为数字，可以用int(str)

num = int(user_age) + 2
print(num)

num2 = int(input("What is your favorite number?"))   #可以直接把int()加在input外边，直接转化为整形数字

# 只有数字是可以进行运算的，字符串不能进行运算



# 实例，计算BMI

user_weight = int(input("请输入你的体重："))
user_height = float(input("请输入你的身高："))
user_BMI = user_weight / (user_height ** 2)
print(user_BMI)
print("用户的BMI是：" + str(user_BMI))