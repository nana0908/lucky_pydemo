print("循环结构--for-in循环，while循环")
import random
'''
for-in 循环
如果明确知道循环的次数，推荐使用for-in循环
'''
list01 = list(x for x in range(10))#使用for ... in .... 可构造一个数字列表
print(list01)

print("用for循环实现1-100求和")
total = 0
for x in range(1,101):#range(1, 101)可以用来构造一个从1到100的范围
    total += x
print(total)

'''
range(101) 产生0-100范围的整数，取不到101
range(1,101) 产生[1,101)范围的整数
range(1,101,2) 产生1-100的奇数，其中2是步长
range(100,0,-2) 产生100到1的偶数，其中-2是步长
'''

print("用for循环实现1-100之间的偶数求和")
total1 = 0
for i in range(2,101,2):
    total1 += i
print(total1)

total2 = 0
for j in range(101,1,-2):
    total2 += j
print(total1)
'''
for ... in ... 遍历str/list/dict
'''
str01 = 'hello'
list02 = ['zhangsan', 'lisi', 'wangwu']
dict01 = {'x':1, 'y':2, 'z':3}
#遍历字符串str01
for i in str01:
    print(i)
#遍历list02
for i in list02:#方法1，通过值遍历
    print(i)

for i in range(0,len(list02)):#方法2，通过下标遍历
    print(list02[i])
# 要求输出列表的元素及下标
print(list(enumerate(list02,start=1)))#enumerate()函数，取出列表的序号，start= 改变初始下标，默认为0
#遍历字典dict
#方法一：字典的函数get(),通过键获取值
for key in dict01:
    print(key,dict01.get(key))
#方法二：：直接输出key和value，items()方法将字典的元素转化为了元组，然后取出
for key,value in dict01.items():
    print(key,value)
'''
while循环
'''
#计算出一个1-100之间的随机数，玩家输入数字，计算机给出提示，如果猜中则退出，计算玩家一共猜了多少个字
s = random.randint(1,100)#随机生成一个1-100范围内的随机数
print(s)
count = 0
while True:
    count += 1
    num = int(input("please input a number:"))
    if s > num:
        print("smaller one")
    elif s < num:
        print("a little bigger")
    else:
        print("Congratulations,right!")
        break
print("你总共猜了%d次" % count)

#打印乘法口诀表
for i1 in range(1,10):
    for j1 in range(1,i1+1):
        print(f'{i1}*{j1} = {i1*j1}',end='\t')#print函数中的end='\t'代表tab键（制表符）
    print()

#输入一个正整数判断是不是素数（素数及只能被1和自身整除的大于1的整数）
'''
判断一个正整数m是否为素数，只要判断m可否被2~根号m之中的任何一个正整数整除，
如果m不能被此范围中任何一个正整数整除，m即为素数，否则m为合数。
'''
s1 = int(input("please input a number"))
end = int(s1 ** 0.5)#开根号
is_prime = True
for x1 in range(2,end + 1):
    print(s1,end,x1)
    if s1 % x1 == 0:
        print(f'{s1}不是素数')
        is_prime = False
        break
    elif is_prime and s1 != 1:
        print(f'{s1}是素数')
    else:
        print(f'{s1}不是素数')

'''
str.formart() 输出
'''
name = '张三'
age = 24
print('my name is %s,age is %d yearsold' % (name,age))
print('my name is {},age is {} yearsold'.format(name,age))
print('my name is {name},age is {age} yearsold'.format(name='lisi',age=25))

'''
例：购物车功能要求：要求用户输入总资产，例如：2000，显示商品列表，让用户根据序号选择商品，加入购物车购买，
如果商品总额大于总资产，提示用户余额不足，否则，购买成功
'''
money = float(input('请输入总资产：'))
goods = [{'name':'电脑','price':1999},
         {'name':'鼠标','price':10},
         {'name':'游艇模型','price':10000},
         {'name':'键盘','price':998}]
print('序号\t商品名称\t商品价格\t')
for i in goods:
    print(goods.index(i)+1, end='\t\t')
    for key in i:
        print(i.get(key),end='\t\t')
    print('\n')
while True:
    chose = int(input('请根据序号选择商品，请输入序号：'))
    if chose in range(1,len(goods)+1):
        buycount = int(input('请输入商品数量：'))
        allprice = goods[chose-1].get('price') * buycount
        if allprice <= money:
            money -= allprice
            print(f'购买成功，您得总资产剩余：{money}')
        else:
            ichose = input('购买失败，账户余额不足,请选择是否需要继续购买（Y/N）：')
            if ichose == 'Y':
                continue
            else:
                print('结束购物！')
                break
    else:
        print('无该商品序号，请重新输入！')

