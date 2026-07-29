f = open("D:\\code\\python\\第一个项目\\file_data.txt","r",encoding="utf-8")

print(f.read(12))

print(f.readline())

lines = f.readlines()
for line in lines:
    print(line)

f.close()

with open("D:\\code\\python\\第一个项目\\file_data.txt","r",encoding="utf-8") as f:
    print(f.read())



with open("D:\\code\\python\\第一个项目\\file_data.txt","w",encoding="utf-8") as f:    #写操作的时候，没法调用read
    f.write("hhh")    #"w"模式下，write操作会覆盖之前文件中的所有内容。
    #写的操作下，如果没有这个文件，会自动生成该路径的一个文件

with open("D:\\code\\python\\第一个项目\\file_data.txt","a",encoding="utf-8") as f:
    f.write("hhh")    #"a"模式下，write操作就不会覆盖之前文件中的所有内容。

#如果想即读又写，可以用"r+"模式
with open("D:\\code\\python\\第一个项目\\file_data.txt","r+",encoding="utf-8") as f:
    f.write("aaa\n")
    print(f.read())


with open("poem.txt","w",encoding = "utf-8") as f:   #在同一个目录下的文件，可以直接用文件名来查找，省去前面的路径
    f.write("我欲乘风归去\n又恐琼楼玉宇\n高处不胜寒\n")