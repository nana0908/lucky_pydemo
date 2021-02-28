'''
1、根据用户输入的玫瑰花的朵数输出其代表的意义：在古代希腊神话中，玫瑰花集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，
但是不同的朵数带表的含义是不同的。
1朵表是：你是我的唯一。3朵表是：我爱你。10朵表示：十全十美。99朵表示：天长地久。108朵表示：求婚！
'''

def rose_case(value):
    rose = {
        1:"你是我的唯一",
        3:"我爱你",
        10:"十全十美",
        99:"天长地久",
        108:"求婚！"
    }
    return rose.get(value,'您输入的数字没有代表意义哦~~')#字典中get()方法取值 dict.get(key, default=None) key -- 字典中要查找的键。default -- 如果指定键的值不存在时，返回该默认值。
i1 = int(input('请输入玫瑰花朵数（1，3，10，99，108）：'))
print(rose_case(i1))

'''
2、国家对酒驾的规定是：车辆驾驶人员血液中的酒精含量小于20mg/100ml不构成饮酒驾驶行为。
含量大于或者等于20mg/100ml,小于80mg/100ml为饮酒驾车，酒精含量大于或者等于80mg/100ml酒醉驾车。
现写一段代码判断输入的血液酒精含量是否为酒驾。
'''

abv = int(input('请输入车辆驾驶员血液酒精含量（单位：mg/100ml）:'))
if 20 <= abv < 80:
    print('该驾驶员为饮酒驾车。')
elif abv > 80:
    print('该驾驶员为酒醉驾车')
else:
    print('该驾驶员未酒驾')

'''
3、小明身高1.75m，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

def bmi_calc(bmi):
    if bmi < 18.5:
        print('过轻')
    elif 18.5 <= bmi < 25:
        print('正常')
    elif 25 <= bmi < 28:
        print('过重')
    elif 18 <= bmi < 32:
        print('肥胖')
    elif bmi >= 32:
        print('严重肥胖')
    else:
        print('输入错误')
bmi1 = 80.5/(1.75*1.75)
print(bmi1)
bmi_calc(bmi1)
'''

4、使用循环语句计算从1到100，一共有多少个尾数为7或者7的倍数这样的数，请输出这样的数。
'''
sum = 0
for i in range(1, 101):#产生0-100范围的整数，取不到101
    if i % 10 == 7 or i % 7 == 0:
        print(f'{i}为尾数为7或者7的倍数')
        sum += 1
    else:
        continue
print(f'1-100中有{sum}个尾数为7或者7的倍数')

'''
5、模拟支付宝的蚂蚁森林通过日常的走步--20g，生活缴费--50g，线下支付--100g，网络购票--80g，
共享单车--200g等低碳，环保行为可以积攒能量，当能量达到一定数量后，可以种一棵真正的树--500g。
   由用户输入环保行为，来积累能量；查询能量请输入能量来源！退出程序请输入0；
'''

init = 0
print('能量输入来源：\n日常的走步--20g，生活缴费--50g，线下支付--100g，网络购票--80g，共享单车--200g')
while True:
    action = input('查询能量请输入能量来源,退出程序请输入0：')
    if action == '日常的走步':
        init += 20
        print(f'增加20g能量，当前能量为{init}')
    elif action == '生活缴费':
        init += 50
        print(f'增加50g能量，当前能量为{init}')
    elif action == '线下支付':
        init += 100
        print(f'增加100g能量，当前能量为{init}')
    elif action == '网络购票':
        init += 80
        print(f'增加80g能量，当前能量为{init}')
    elif action == '共享单车':
        init += 200
        print(f'增加200g能量，当前能量为{init}')
    elif action == '0':
        print('退出能量计算程序')
        break
    else:
        print('输入错误，请重新输入')
        continue
plantTrees = input(f'您当前可种植{init // 500}棵树，请选择是否需要种树，选择 Y/N')
if plantTrees == 'Y':
    if init < 500:
        print('种树能量不够')
    elif init >= 500:
        init -= 500
        print(f'恭喜您成功种下一棵树,剩余能量为{init}')
elif plantTrees == 'N':
        print(f'取消种树，剩余能量{init}')

'''
6、猜数字游戏，随机生成一个1到10之间的数(包括1和10)的数字作为基准数，
玩家每次通过键盘输入一个数字，如果输入的数字和基准数字相同，则过关，否则重新输入。
如果玩家输入-1，则表示退出游戏。
'''

import random
base = random.randint(1, 10)#随机生成一个1-10范围内的随机数
#print(base)
while True:
    num = int(input('请输入一个[1,10]范围内的数字(输入-1，则表示退出游戏):'))
    if num == -1:
        print('退出游戏')
        break
    else:
        if num == base:
            print('过关，游戏结束')
            break
        elif num != base:
            print('输入不正确，请重新输入')
'''

7、编写程序，设置您的余额，流量和剩余通话时间。模拟10086自助查询系统的功能：输入1，显示您当前的余额；
输入2，显示您当前剩余的流量，单位为G；输入3，您当前的剩余通话，单位为分钟；输入0，退出自助查询系统。
'''

balance = input('请设置用户当前余额（单位元）：')
flow = input('请设置剩余流量（单位G）：')
calls = input('请设置剩余通话（单位：分钟）：')
def query10086(i):
    query = {
        1: f'您当前的余额为：{balance}元',
        2: f'您当前剩余的流量为：{flow}G',
        3: f'您当前剩余通话为：{calls}分钟',
        0: '退出自助查询系统'
    }
    return query.get(i, '输入错误！')
while True:
    i = int(input('请输入数字（1：查询余额，2：查询流量，3：查询剩余通过，0：退出）'))
    list1 = [0,1,2,3]
    if i in list1:
        if i == 0:
            print(query10086(i))
            break
        else:
            print(query10086(i))
    else:
        print('输入错误！')

'''
8、几个好朋友一起玩逢七拍腿的游戏，即从1开始依次数数，当数到尾数为7的数或7的倍数时，则不报出该数，而是拍一下腿。
现在编写程序，从1数99，假设每个人都没有出错，计算共要拍多少次腿。
'''

num1 = 0
'''
for i in range(1, 100):#产生0-100范围的整数，取不到101
    if i % 10 == 7 or i % 7 == 0 :
        num1 += 1
    else:
        continue
print(num1)
'''
for i in range(1, 100):#产生0-100范围的整数，取不到101
    if i % 7 == 0:
        num1 += 1
    else:
        string = str(i)
        if string.endswith('7'): #endswith()函数：判断最后一位数字是不是7
            num1 += 1
print(num1)

'''
9、输出2000-2020年之间的润年。(非整百年能被4整除的为闰年,能被400整除的是闰年)
'''

is_leap = []
for year in range(2000, 2021):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        is_leap.append(year)
    else:
        continue
print(f'2000-2020年中间的闰年有{is_leap}')


'''
10、由用户输入三个整数，判断这三个数是否可以构成三角形。
如果可以构成三角形的话，则进一步显示三角形的类型(等边，等腰，一般三角形)。
如果不构成三角形的话，则给出提示信息。
'''
a, b, c = input("请输入三个整数：").split(',')
if int(a)+int(b) > int(c) and int(a)+int(c) > int(b) and int(b)+int(c) > int(a):
    print('可以构成三角形')
    if a == b == c :
        print('该三角形为等边三角形')
    elif a == b or a == c or b == c:
        print('该三角形为等腰三角形')
    elif a != b and b != c and a != c:
        print('该三角形为普通三角形')
else:
    print('无法构成三角形')
