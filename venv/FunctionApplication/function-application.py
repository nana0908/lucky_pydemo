# 函数应用
'''
函数参数介绍：形参，实参
'''
def add(num1, num2):#num1和num2为形参。 必备参数
    return num1 + num2

print(add(3,4))#3,4为实参，，与形参一一对应。必备参数

'''
python函数参数类型：
必备参数：以正确的顺序传入函数，也叫位置参数，即参数是通过位置进行匹配的，从左到右，依次进行匹配
关键字参数：体现在实参的写法
缺省参数：体现在形参，形参有默认值
任意个数参数（收集参数）：又称不定长参数，表示能接受0到多个参数
'''
def add1(num1, num2):
    print(f'{num1}+{num2}={num1+num2}')

add1(num1=2,num2=3)#形参名称赋值的方式，关键字参数

def add2(num1, num2=20):#缺省参数，形参num2有默认值，注：如果有多个参数，缺省参数放置在最后
    print(f'{num1}+{num2}={num1+num2}')

add2(2)

def add3(*num):# 收集参数：*号代表元组
    print( type(num) , num )

add3()
add3(3)
add3(1,2,3,4)

def add4(**num):# 收集参数：**号代表字典
    print( type(num) , num )

add4()
add4(a=1,b=2)#注意传参格式

def multiplication_table():#九九乘法表
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end='\t')
        print('\n')
multiplication_table()

'''
python函数的参数传递:
不可变类型：整数、字符串、元组---传递的只是值的本身
可变类型：列表，字典--- 会影响对象的值
'''
def s_add(num):
    num = num + 10
    print(id(num),num)

def l_add(list01):
    list01.append(20)
    print(id(list01),list01)
a = 10
list_a = [1,2,3,4]
print(id(a),a)
s_add(a)#不可变类型传的是值，不会改变对象的值
print(id(list_a),list_a)
l_add(list_a)#可变类型传的是地址，会改变对象的值

# is 判断两个标识符（变量）是不是引用自同一个对象，用id方法求得地址一样得话为true
a = 10
print(a is 10)
b = a
print(a is b)
c = 11
print(a is c)

# 函数的嵌套：即在一个函数内部存在调用其他函数的情况,或者在函数内部再定义一个函数
def fun1():
    print('函数1')
    s_add(10)#数内部存在调用其他函数
    def fun2():
        print('函数2')#函数内部再定义一个函数
    fun2()#作用域：函数内部定义的函数只能再函数内部调用
fun1()

'''
变量的作用域。
作用域是象对的 LEGB == > 
如果LEG都存在，则L（局部作用域）优先，其次E（嵌套作用域），再之后是G（全局作用域），最后是B（内置作用域）
'''
a = 10
print( a )

a = 10
def fun1():
    a = 20
    print(a)
fun1()

b = 10 # 全局作用域  G
def fun2():
    b = 20 # 嵌套作用域 E
    def fun3():
        b = 30 # 局部作用域 L
        print( b )
    fun3()
fun2()

#__file__ = 10 #全局作用域 G
def fun4():
    #__file__ = 20 # 嵌套作用域 E
    def fun5():
        #__file__ = 30 # 局部作用域 L
        print( __file__ )#__file__ 内置变量，内置变量，以__开头，当LEG都没有的时候，=内置变量的值，如该内置变量不存在，则报错
    fun5()
fun4()

'''
递归：
'''
#递归实现累加.
def _add(num):
    if num > 0:
        print(f'{num} + {num-1}')
        return num + _add(num-1)
    else:
        return 0
print(_add(3))#1+2+3


