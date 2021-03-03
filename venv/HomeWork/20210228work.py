'''
作业：
1、用自己的理解方式编码举例LEGB规则
'''
l = '10'
print(f'当前l为全局变量(L),l={l}')
def legbRule():
    l = '20'
    print(f'当前l为嵌套变量(E)，l={l}')
    def fun01():
        l = '30'
        print(f'当前l为局部变量(G)，l={l}')
        print(f'\'__name__\'未被定义，当前{__name__}为内置变量（B）')
    fun01()
legbRule()

'''
2、用函数递归的方式求 4！
'''

def factorial(i):
    fac = 0
    if i == 0:
        fac = 1#0!=1
    else:
        fac = i * factorial(i-1)
    return fac
n = int(input('请输入一个大于0数：'))
if n >= 0:
    print(f'{n}的阶乘为{factorial(n)}')
else:
    print('负数没有阶乘！！！')


'''
3、编写一个匿名函数，能求出3个数的最大值
'''
maxValue = lambda a, b, c: max(a, b, c)
print(maxValue(3, 4, 6))
'''
4、python模块的导入方式有哪几种？（问答）
import 模块名
from 包 import 模块名
from 包.模块名 import 方法名
from 包.模块名 import *

5、用包和不用包的区别在哪里？
用包为了方便模块管理
不用包模块之间相互调用更加方便

6、编写用户登陆系统
需求：
1.系统里面有多个用户，用户的信息目前保存在列表里面
   users = ['root','westos']
   passwd = ['123','456']
2.用户登陆(判断用户登陆是否成功）
   1).判断用户是否存在
   2).如果存在
       1).判断用户密码是否正确
       如果正确，登陆成功，退出循环
       如果密码不正确，重新登陆，总共有三次机会登陆
   3).如果用户不存在
   重新登陆，总共有三次机会
'''
'''
def login(user,password):
    users = ['root', 'westos']
    passwd = ['123', '456']
    islogin = False
    if user in users:
        i = users.index(user)
        if password == passwd[i]:
            print('登录成功！！')
            islogin = True
        else:
            print(' 您输入的密码不正确！')
            islogin = False
    else:
        print('您输入的用户不存在！')
        islogin = 'false'
    return islogin

count = 0
while True:
    if count < 3:
        user = input('请输入用户名：')
        password = input('请输入密码：')
        if login(user, password) == True:
            break
        else:
            count += 1
            if count < 3:
                print('请重新输入')
    else:
        print('您输入的账号密码错误超过3次，退出系统！')
        break
'''
users = ['root', 'westos']
passwd = ['123', '456']
count = 0
while count < 3:
    user = input('请输入用户名：')
    password = input('请输入密码：')
    count += 1
    if user in users:#判断用户是否存在
        index = users.index(user)#获取用户名下标
        if password == passwd[index]:
            print(f'用户{user}登录成功')
            break
        else:
            print(f'用户{user}登录失败，密码不正确')
    else:
        print(f'用户{user}不存在')
else:
    print('已超过3次机会')