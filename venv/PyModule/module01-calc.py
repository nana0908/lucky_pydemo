'''
模块：对于一个复杂的功能，为了编写课维护的代码，会把函数分组放入不同的文件中，这样每个文件包含的代码象对较少
在python中，一个.py文件就是一个模块（即一个文件被看错一个独立的模块）
内置模块：如：sys，os，subprocess，time，json等，使用print(help('module'))
自定义模块：自定义模块需注意命名，尽量不要和python自带模块冲突
开源模块：公开的第三方模块，如：https://pypi.python.org/pypi，可以使用pip install安装
'''
#print(help('modules'))
'''
import导入模块，按照标准库模块，python三方模块，定义模块的顺序从上至下排开
from...import 模糊导入
通过sys.path.append(path)函数导入自定义模块所在的目录
'''
import os,time,sys # 标准库模块
#import appium,selenium # 第三方模块
sys.path.append('D:/PycharmProjects/lucky_pydemo/venv/BasicGrammar/')#导入自定义模块所在的目录
#import example # 自定义模块
from BasicGrammar import example#导入自定义模块

from random import randint #from...import 模块导入，导入模块内单个方法
from random import *#会加载模块所有方法，不推荐使用
#from example import craps as c #给方法起别名，模块内只能使用别名调用

example.craps()
