'''
函数定义：
def 函数名(行参):
    语句块
函数调用：
函数名(实参)
'''

def fun1():
    print('无参函数')

def fun2(a,b):
    print('有参函数，其中a，b为形参')
    return a + b

fun2( 3, 4 )#函数调用，其中3，4为实参，与函数形参意义对应

'''
参数传递：
参数是不可变数据类型，传递的是实参的值(如：fun2()函数)
参数是可变数据类型时，传递的是实参的地址，引用传递(如fun3()函数)
'''
def fun3(list01):
    list01.append([ 1, 2, 3])
    print(list01)

list0 = [ 1, 2, 3]
print(list0)
fun3(list0)
print(list0)

'''
变量作用域：作用域是相对的，局部优先
内置作用域（B）：python自带变量，以'__'开头，通过print(var())可查看内置变量
全局作用域（G）：函数外部定义
嵌套作用域（E）：函数内嵌套函数外部定义
局部作用域（L）：函数内部定义
LEGB法则：搜索变量优先级：局部 > 嵌套 > 局部 > 内置
'''
print( vars() )#打印内置变量
__file__ = '全局作用域'#__file__为内置函数
def fun4():
    __file__ = '嵌套作用域'
    #global __file__ #强制使用全局变量
    #__file__ = '强制全局变量'
    print( '当前作用域为{}'.format(__file__) )
    def fun5():
        a1 = '局部变量域'#局部优先
        print( '当前作用域为{}'.format(__file__) )
        print( '当前作用域为内置变量域:{}'.format(__name__) )#__name__内置变量
    fun5()
fun4()
print( __file__ )#使用global强制使用全局变量后，a1的值已经变为强制后的值

'''
函数的参数：
必备参数:参数列表顺序不可以改变
关键字参数：参数列表顺序是可以改变
缺省参数：未传参时，参数必须要有默认值
任意个数参数：* 表示将没有匹配的值都放到同一个元组中，** 代表将没有匹配的值都放到同一个字典中
'''
def pri(name, *test_tuple):
    print(name)
    print(test_tuple, type(test_tuple))
pri('zhangsan', 20, 'it', 'changsha', 50)

def pri(name, **test_dict):#多余的参数必须是键值对类型
    print(name)
    print(test_dict, type(test_dict))
pri('zhangsan', age = 20, sex = 'male', address = 'changsha')

