import math
print('结构分支--if语句的使用')

'''
在Python中，要构造分支结构可以使用if、elif和else关键字。所谓关键字就是有特殊含义的单词，像if和else就是专门用于构造分支结构的关键字
Python中没有用花括号来构造代码块而是使用了缩进的方式来表示代码的层次结构，
如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。
'''

#例1：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
grade = int(input('please input grade:'))
if grade >= 90:
    print('A')
elif grade >= 80 and grade < 90:
    print('B')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 60 and grade < 70:
    print('D')
else:
    print('E')

#例2：输入三条边长，如果能构成三角形就计算周长和面积。
'''
根据海伦公式求：

已知三角形du的三边分别是a、b、c，求zhi面积dao。

先算出周长的一半h=1/2(a+b+c)，然后根据公式S=(h*(h-a)(h-b)(h-c))**0.5，代入数值即可。
'''
a = float(input('please input side chief one:'))
b = float(input('please input side chief two:'))
c = float(input('please input side chief three:'))
if a+b>c or a+c>b or b+c>a:
    C = a+b+c
    h1 = C/2
    S = (h1*(h1-a)*(h1-b)*(h1-c))**0.5     #数据计算
    S1 = math.sqrt(h1*(h1-a)*(h1-b)*(h1-c))#引入函数sqrt(x)--返回数字x的平方根
    print(f'{S}')
    print(f'{S1}')
    print('周长：%.2f，面积：%.2f' % (C,S1))
else:
    print('不能构成三角形')