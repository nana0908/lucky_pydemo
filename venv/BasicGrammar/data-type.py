import keyword
print(keyword.kwlist)# 关键字不能作为命名。建议变量名全部小写，类名首字母大写

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
print(int(x,8))#8进制的x转成10进制
print(hex(int(x,10)))#10进制的x转成16进制

'''
转义字符与原始字符串
'''
s1 = '\'hello,world\''
s2 = '\\hello,world!\\'#python中，用\反斜杠表示转义。\n 换行，\t 制表符，字符串本身包含‘、“，\等特殊字符，需转义
s3 = '\time up \now'
s4 = r'\time uo \now'#python中，字符串以r活着R开头，代表原始字符串，即：每个字符都是原本的含义，没有所谓的转义字符
print(f's1={s1}')
print(f's2={s2}')
print(f's3={s3}')
print(f's4={s4}')

'''
字符串之比较运算/成员运算
'''
s5 = 'hello world'
s6 = 'hello world'
s7 = s6
print(s5 == s6,s6 == s7) # '=='比较字符串中的内容
print(s5 is s7,s6 is s7) # 'is'比较字符串的内存地址

s8 = 'he'
s9 = 'sh'
print(s8 in s5)
print(s9 not in s5)# 'in''not in'判断一个字符串中是否存在另一个字符活字符串
print(s8+s9)#字符串拼接，注意：同一数据类型才能进行拼接
print(s8*8)#字符串重复
print(len(s7)) # 获取字符串长度
print(len("goodbye,world"))

s = 'abc123456'
N = len(s)
print(s[0],s[-N]) # 获取第一个字符，s[0] 索引运算， s[-N] 负向索引
print(s[2:5:2],s[-2:-8:-1]) # 正向切片，运算符是[i:j:k]，其中i是开始索引,是结束索引，k是步长，默认值为1

s = 'hello,world'
print(s.capitalize()) #  使用capitalize方法获得字符串首字母大写后的字符串
print(s.title()) # 使用title方法获得字符串每个单词首字母大写后的字符串
print(s.upper()) # 使用upper方法获得字符串大写后的字符串
s1 = s.upper()
print(s1.lower()) # 使用lower方法获得字符串小写后的字符串

print(s.find('h'),s.find('s')) # ind方法从字符串中查找另一个字符串所在的位置,找到返回索引，未找到返回-1
print(s.index('l')) # index方法与find方法类似，找到返回索引，未找到引发异常

print(s.startswith('he')) # startswith、endswith来判断字符串是否以某个字符串开头和结尾
print(s.endswith('he'))
print(s.isalpha()) # is开头的方法判断字符串的特征 如isalpha方法检查字符串是否以字母构成返回布尔值
print(s.isalnum()) # isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s.isdigit()) # isdigit方法检查字符串是否由数字构成返回布尔值

# 字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理
print(s.center(20,'*')) # center方法以宽度20将字符串居中并在两侧填充*
print(s.rjust(20)) # 右对齐，宽度20，左侧填充空格
print(s.ljust(20,'~')) # 左对齐，宽度20，右侧填充~

s1 = '  nana@123.com\t'
print(s1.strip()) # strip方法获得字符串修剪左右两侧空格之后的字符串
print(s1.lstrip())
print(s1.rstrip())

# list，：列表。list是可变的有序列表，可以随时添加或删除其中的元素
list1 = [3,3,3]
list2 = [1,2,3,5,8,7,8,3,2,1]
list3 = [['linda'],['lisa','jim'],3,4,6,9]
print(list2[0])#通过索引获取元素
print(list1+list2)#加号+ 拼接符
print(list1*4) # 乘号* 重复符
print(len(list1))# 获取列表长度
list1.append(5)# 列表末尾追加单个元素
print(list1)
list1.extend([2,3,4])# 列表末尾追加多个元素，追加list
print(list1)
list1.insert(0,3)# 指定位置插入元素
print(list1)
list1.pop(0)#删除列表指定索引处元素，默认删除列表末尾元素
print(list1)
list1.remove(3)# 删除第一次出现的该元素
print(list1)
print(list1.count(3))# 统计该元素在列表中出现的个数
print(list1.index(3))# 该元素第一次出现的位置，无则抛异常
list2.sort()
print(list2)#排序,默认升序
list2.sort(reverse=True) #排序后升序
print(list2)
list2.reverse()
print(list2)#反转

#list的复制，如：L1=L,只是给L取了一个名为L1的别名，他们的内存地址是一致的
#L1=L[:]，L1为L的克隆，即另一个拷贝，是把L中的所有值给L
list4 = list1 #传址 -- 地址传递，改变其中一个列表，另一个列表也会发生改变
print(id(list1))
print(id(list4))
list5 = list1[:]#传值 -- 数值传递，改变其中一个列表，另一个列表不会发生改变
print(id(list5))

# tuple  元组，不可变可重复列表（只读的列表），使用()进行定义。类似于list的一个数据类型
tuple01 = (1,2,3,2,3)
tuple02 = (2,4,5,6)
print(tuple01[0])#元组的切片和索引与列表一致
print(tuple01+tuple02)#元组可以进行重复和拼接
print(tuple01*2)
#元组可使用的函数有count(),index()
print(tuple01.count(1))
print(tuple01.index(1))

# set 集合，用{}定义,或者用set()函数创建集合，是一个无序，元素不可重复的序列。
set01 = {'aa','bb','cc','aa'}
print(set01)
set02 = {'dd','aa','ee','ff'}
#set不能进行拼接/重复，切片/索引等操作，但可以用来运算
print(set01 - set02)#差集，只返回第一个集合中存在第二个集合中不存在的
print(set01 & set02)#交集，返回两个集合中共同存在的元素
print(set01 | set02)#并集，返回两个集合中拥有的元素（去重）
print(set01 ^ set02)#交集的补集
print('aa' in set01)#用in判断元素是否存在于集合中，存在返回True，不存在返回False
#注意：创建一个空集合必须用set()而不是{},因为{}是用来创建一个空字典的

#字典 dict 和集合一样用{}定义---存储方式：键值对的方式存储：key:value
dict01 = {'name':'lisa','tel':'1667347588','age':23}
dict02 = dict(name='linda',tel='13462727731',age=25)#dict()函数定义字典
dict03 = dict((['name','nana'],['tel','15678838929'],['age',30]))
tuple03 = [1,2,3]
dict04 = dict.fromkeys(tuple03,'zhangsan')#使用内建函数formkeys(S [,v])定义字典
print(dict04)
dict01['name'] = 'jim' #改变字典中的值，key存在，则修改该key对应的值
dict01['score'] = 66   #如果字典中key不存在，则直接新增
print(dict01)

print(dict01.get('name')) # 通过get()函数获取元素,若元素不存在，则返回None
print(dict01.keys())#获取所有的key值
print(dict01.values())#获取所有的value值
del dict02['tel']#删除字典中对应的值
print(dict02)
print(dict01.pop('tel'))#删除字典中存在的key对应的值并返回
print(dict01)
dict01.update(dict02)#更新字典，key有则更新，无则不更新
print(dict01)
dict03.clear()#清除字典中的所有元素
print(dict03)

# 数据类型的转换
#数字类型自动转换











