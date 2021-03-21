'''
函数嵌套
1、在函数内部调用其他函数
2、在函数内部再定义一个函数（不常见）
'''

'''
函数递归：直接或间接的调用了函数本身
'''
#手动输入一个数字N，循环打印N次helloworld，使用递归方式实现
def pri(num):
    if num > 0:
        print('hello world!!!')
        pri(num - 1)
    else:
        return 0
N = int(input('请输入一个数字：'))
pri(N)

'''
匿名函数：lambda函数，创建小型函数，能接受任何数量的参数但只能返回一个表达式的值
    语法：函数名称 = lambda 参数列表：返回的表达式
'''
sum = lambda a, b: a+b
print(sum(3, 4))

sum01 = lambda a, b: print(a + b)#老版本不能调用print函数，经过几次版本更新，目前可以
sum01(1, 2)

'''
内置函数：python自带函数
'''

'''
python模块：在python中，一个.py文件就是一个独立的模块
    内置模块：如：sys，os，subprocess，time，json等，使用print(help('module'))
    自定义模块：自定义模块需注意命名，尽量不要和python自带模块冲突
    开源模块：公开的第三方模块，如：https://pypi.python.org/pypi，可以使用pip install安装
导入模块
    import 模块名称--都是导入内置模块或者第三方模块的时候，常用
    from 包名 import 模块名 导入整个模块
    from 包名.模块名 import 方法名 常用，导入单个方法，当两个函数中有同名函数时，以最后导入的为准
    from 包名.模块名 import * 导入模块所有的方法，不推荐使用
    from 包名.模块名 import 方法名 as 别名 给导入的方法取别名，通过这种方式导入，使用时只能用别名调用   
导入模块的编写顺序：
    内置模块
    第三方模块
    自定义模块
'''
import time
from random import randint
time.sleep(4)#调用模块中的方法，模块.模块方法
import sys


