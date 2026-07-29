from multiprocessing import managers


class CuteCat:
    def __init__(self ,age ,owner):    #一个类有什么属性是在初始方法里定义的
        self.name = "shisan"
        self.age = age
        self.owner = owner

    def speak(self):
        print("喵" * self.age)    #字符串*数字等于输出数字次该字符串

shisan = CuteCat(3,"susu")
print(shisan.name + str(shisan.age) + shisan.owner)
print(f"{shisan.name} {shisan.age} {shisan.owner}")

shisan.speak()


class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {"语文":0,"数学":0,"英语":0}
    # def set_grade(self,course,grade):
    #     if course in self.grades:
    #         self.grades[course] = grade
    def set_grade(self):
        for course in self.grades:
            self.grades[course] = int(input(f"{course}成绩为："))

    def output_grades(self):
        print(f"学生{self.name}的成绩为：")
        for course,grade in self.grades.items():
            print(f"{course}:{grade}")

xiaoming = Student("xiaoming",15)
xiaoming.output_grades()
xiaoming.set_grade()
# xiaoming.set_grade("化学",59)
# xiaoming.set_grade("语文",59)
# xiaoming.set_grade("数学",100)
xiaoming.output_grades()



class MyCounter:
    def __init__(self,a,b):
        '''a与b就相当于add函数和sub函数的公共变量，解决了一个函数内的局部变量无法在另一个函数内使用的情况'''
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b


class Man:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        '''属性sex有个默认值'''
        self.sex = "man"
cxk = Man("cxk",18)
cxk.sex = "balabala"
print(cxk.sex)

