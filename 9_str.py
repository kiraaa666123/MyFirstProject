# 当要赋值给变量的字符串太长的时候，可以用反斜杠\来换行，但实际赋值的字符串是没有换行的
name = "heellllelelelel\
shfhfhfhfhfhffh" + \
    str(33) + \
    "hhhhh"
print(name)

str_1 = "susu"
num_1 = 123
num_2 = 23.123233

message = f"""
哈哈哈哈哈
嘿嘿嘿嘿嘿
{str_1}
45678
{num_1}
{num_2:.2f}    
"""

# {num_2:.2f}表示保留两位小数

print(message)

