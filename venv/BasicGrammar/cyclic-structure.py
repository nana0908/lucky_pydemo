print("循环结构--for-in循环，while循环")
import random
'''
for-in 循环
如果明确知道循环的次数，推荐使用for-in循环
'''
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
s1 = int(input("please input a number"))
end = int(s1 ** 0.5)
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

