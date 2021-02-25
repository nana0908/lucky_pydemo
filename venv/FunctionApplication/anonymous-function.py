'''
匿名函数：Lambda:用lambda关键字可以创建小型匿名函数，能接受任何数量的参数但只能返回一个表达式的值
要点：
1，lambda 函数不能包含命令，
2，包含的表达式不能超过一个。
'''
sum1 = lambda num1,num2:num1+num2#函数名 = lambda 形参：表达式

def sum1(num1,num2):#与lambda函数意义一致
    return num1 + num2

'''
内置函数：系统自带的函数
'''
list01 = [2, 34, 4, 88, -9, 99]
print(min(list01))
print(max(list01))
