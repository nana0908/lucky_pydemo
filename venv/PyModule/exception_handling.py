#异常处理
'''
    异常处理一般用来处理软件或信息系统中出现的异常状况（即超出程序正常执行流程的某些特殊条件），如：文件找不到，
网络连接失败，非法参数等。
    当python发生异常时需要捕获处理它，否则程序会终止执行
    在python中，异常也是对象，所有的异常都是基类Exception的成员，所有异常都从基类Exception继承，而且都在exception
模块中定义。python自动将所有异常名称放在内建命名空间类，所以程序不需要导入即可使用异常
    捕捉异常可以使用try/except语句.try语句块中的错误
    try:
        block
    except [exception,[data...]]:
        block
    else：
        block
    finally:
        block
    - 执行try下面的语句，如果引发异常，则执行过程会跳到第一个except语句
    - 如果第一个except中定义的异常与引发的异常匹配，则执行该except众点饿语句
    - 如果引发的异常不匹配第一个except，则会搜索第二个except，允许编写的except数量没有限制
    - 如果所有的except都不匹配，则异常会传递大下一个调用本代码的最高层try代码中（Exception）
    - 如果没有发生异常，则执行else块代码
    - 不管是否发生异常均会执行finally块代码，语法需放在else之后
异常分为两类：
    1. 系统异常 数组越界，文件找不到，值错误等
    2. 业务异常 用户名密码错误等（自定义异常）
触发异常：python中的raise关键字引发一个异常
    raise [Exception [,args[,traceback]]]#语句中Exception是异常类型，参数是一个异常参数值，该参数可选，如不提供，则是None

'''
try:
    num = int(input('please input 0--4：'))
    lista = [1, 3, 4, 8, 9]
    print(lista[num])
except IndexError as e:#处理异常，出错后的处理 except 按照先后顺序匹配错误
    print('IndexError下标越界')
except ValueError as e:
    print('ValueError 输入的非正整数 ')
except Exception as e:#Exception 一般加到最后
    print('报错了，但我不知道原因')
else:#try中语句块正常执行时会执行else
    print('ending')
finally:#不管是否发生异常均会执行
    print('我一直执行')

#触发异常
# raise IndexError('raise 下标越界')
try:
    raise IndexError('raise IndexError')#创建一个对象并赋予一个参数
except IndexError as e:#e代表目前的一个异常对象
    print(e)

#自定义异常
class OnlyInput04Eeeor(Exception):
    def __str__(self):#内置方法__str__():自定义实例输出方法
        return '输入了不在范围内[1，4]的数字'
# def check_num(num):
#     if num < 0 or num > 4:
#         raise OnlyInput04Eeeor('输入的数字错误')

try:
    num = int(input('please input 0--4：'))
    if num < 0 or num > 4:#自定义异常，一般跟着条件语句
        raise OnlyInput04Eeeor()
except OnlyInput04Eeeor as e:
    print(e)
except Exception as e:
    print(e)