
print("hello world,data-type 数据类型")
'''
python中创建变量不需要首先定义变量类型
整型：int example：-10
长整型：long  100000000000000L
浮点型：float 2.50
字符串：string IlovePython
列表：list ["python",12,2.3,9.7]
元组：tuple ("python",12,2.3,9.7)
字典： Dictionary {"name":"libai","company":"baidu","grade":"T7"}
集合：set {1,2,3}
布尔型：bool True，False
'''
a = 100
b = 12.745
c = 'hello world'
d = True
e = ["a",1,2]
f = ("tuple",3,2)#元组
g = (("name","lisa"),("sex","male"))#嵌套元组

print(type(a))#type(x) 查看变量数据类型
print(type(b))
print(type(c))
print(type(d))
print(type(e))


'''
不同类型变量可以相互转换
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
'''

print(float(a))#整数转成字符串
print(str(b))# 浮点型转成字符串 (输出字符串时不会看到引号哟)
print(bool(c))# 字符串转成布尔型 (有内容的字符串都会变成True)
print(int(d))# 布尔型转成整数 (True会转成1，False会转成0)
print(chr(97))# 将整数变成对应的字符 (97刚好对应字符表中的字母a)
print(ord('a'))# 将字符转成整数 (Python中字符和字符串表示法相同)
print(tuple(e))#list和元组互转
print(dict(g))#嵌套元组转换为字典
print(type(dict(g)))
print(int(b))#浮点型转整型，取整数，不做四舍五入
print(round(b,0))#round(x,y)用于数字的四舍五入,y后面表示保留几位小数

'''
不同进制相互转换
2进制转换：bin(int(x,8))
8进制转换：oct(int(x,10))
10进制转换：int(x,2)
16进制转换：hex(int(x,2))
'''
x = '10'
print(bin(int(x,16)))#16进制的x转成2进制
print(oct(int(x,2)))#2进制的x转成8进制
print(int(x,8))#8进制的x转成2进制
print(hex(int(x,10)))#10进制的x转成16进制