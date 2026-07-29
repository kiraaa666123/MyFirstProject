num = int(input("指数："))
if num >=60 :
    print("及格")
else :
    print("不及格")

if num >=60:
    if num < 85:
        print("良好")
    else :
        print("优秀")
else :
    print("真菜")



if num >=85 :
    print("优秀")
elif num >=60 :
    print("良好")
else :
    print("不及格")

if 60 < num < 85:    #python中允许直接这么判断
    print("良好")


# 也可以用and、or和not来进行更多条件的判断，优先级：not>and>or