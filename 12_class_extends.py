class Mammal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def eat(self):
        print(f"{self.name}会吃饭")
    def poop(self):
        print(f"{self.name}会拉屎")

class Man(Mammal):
    def __init__(self,name,age,sex,height,weight):
        super().__init__(name,age,sex)
        self.height = height
        self.weight = weight
    def play(self):
        print(f"{self.name}会玩游戏")

xiaoming = Man("xiaoming",18,"男",180,75)
xiaoming.eat()
xiaoming.poop()
xiaoming.play()
