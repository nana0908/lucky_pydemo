print("函数和模块")

from random import randint #from...import...语法：从模块中直接导入需要使用的函数
#定义函数 def 求阶乘
def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input("m = "))
n = int(input("n = "))

print(fac(m))
print(fac(m) // fac(n) // fac(m-n))

#参数的默认值
'''
CRAPS赌博游戏
'''
#定义骰子的函数，n表示骰子的个数，默认值为2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

#如果没有定义骰子的个数，则使用默认值
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))

'''
可变参数
'''
def add(*args):
    total1 = 0
    for var in args:
        total1 += var
    return total1

print(add())
print(add(1))
print(add(1,2))

'''
标准库中的模块和函数
'''
print(abs(-1.31))#返回一个数的绝对值
print(chr(8364))#Unicode编码转字符
print(ord('@'))#字符转unicode编码
print(len("1234556"))#获取字符串或列表长度
print(max(12,23,33))
print(min(12,23,33))
print(pow(2,0.5))#求幂运算
