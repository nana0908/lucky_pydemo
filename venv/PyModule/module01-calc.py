'''
模块：对于一个复杂的功能，为了编写课维护的代码，会把函数分组放入不同的文件中，这样每个文件包含的代码象对较少
在python中，一个.py文件就是一个模块（即一个文件被看做一个独立的模块）
内置模块：如：sys，os，subprocess，time，json等，使用print(help('module'))
自定义模块：自定义模块需注意命名，尽量不要和python自带模块冲突
开源模块：公开的第三方模块，如：https://pypi.python.org/pypi，可以使用pip install安装
'''
#print(help('modules'))
'''
import导入模块，按照标准库模块，python三方模块，定义模块的顺序从上至下排开
通过sys.path.append(path)函数导入自定义模块所在的目录
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
import os,time,sys # 标准库模块
print( os.getcwd() )
print( sys.path )
#import appium,selenium # 第三方模块
#sys.path.append('D:/PycharmProjects/lucky_pydemo/venv/BasicGrammar/')#windows系统导入自定义模块所在的目录
sys.path.append('/Users/nana/PycharmProjects/lucky_pydemo/venv/BasicGrammar/')#导入自定义模块所在的目录
for i in sys.path:
    print(i)#打印环境变量
#import example # 自定义模块
from BasicGrammar import example#导入自定义模块
#from BasicGrammar.example import craps

from random import randint #from...import 模块导入，导入模块内单个方法
from random import *#会加载模块所有方法，不推荐使用
#from example import craps as c #给方法起别名，模块内只能使用别名调用


if __name__ == '__mian__':#判断执行的name是不是自己本身，可以防止重复调用
    print('')


example.craps()
