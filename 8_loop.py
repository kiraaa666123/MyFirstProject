t_list = [1,2,3,4,5]
for t in t_list:
    if t % 2 == 0:
        print("偶数")

t_dict = {"a":1,"b":2,"c":3,"d":4}
for keys,values in t_dict.items():
    if values % 2 == 0:
        print(keys)

for i in range(1,101):    # 从1遍历到100，    #只放一个值的时候，range默认起始值为0
    print(i)
range(1,101,2)    # 步长为2

j = 0
while j < len(t_list):
    print(t_list[j])
    j += 1



# 练习

user_grade = input("请输入你的成绩（输入-1结束）")
total = 0
count = 0
while user_grade != "-1":
    total += int(user_grade)
    count += 1
    user_grade = input("请输入你的成绩（输入-1结束）")
if count == 0:
    print(0)
else:
    print("成绩平均值为：" + str(total / count))




