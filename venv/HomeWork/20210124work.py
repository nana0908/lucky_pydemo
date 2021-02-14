"""
1.给定一个非空正整数的列表，按照列表内数字重复出现次数，从高到低排序
"""

list1 = [1,2,3,5,3,3,3,1,3,2,7,8,7,7,3,1,1,1]
d = {}
for i in list1 :
    d[i] = list1.count(i) #count() 方法用于统计字符串里某个字符出现的次数
print(d,type(d))
'''
items()方法将字典的元素转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
（如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。
lambda x:y中x表示输出参数，y表示lambda函数的返回值），所以采用这种方法可以对字典的value进行排序
'''
print(sorted(d.items(),key=lambda item : item[1],reverse=True))#sort() 对给出的对象进行排序。d.items()实际上是将d转换为可迭代对象

list2 = [1,3,5,6,3,2,3,1,7,2,2,2,3,6]
set01 = set(list2)
print(set01)
dict01 = {}
for i in set01:
    dict01[i] = list2.count(i)
print(dict01)
list3 = sorted(dict01,key=dict01.get,reverse= True)#sort() 对给出的对象进行排序,dict01.get获取字典的value
print(list3)
'''
月份缩写：如果有 
months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，
编写一个程序，用户输入一个月份的数字，输出月份的缩写。
'''
month = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."
monthlist = list(filter(None,month.split('.')))#去除list的空字符串和None
print(monthlist,type(monthlist))
i = int(input("请输入月份数字（1-12）："))
if i >0 and i < 13 :
    print("您输入的月份为：", monthlist[i - 1])
else:
    print("您输入的月份数字不正确！")


'''
3、定义列表：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
a.请分别取出['Apple', 'Google', 'Microsoft’]、’Ruby’,[‘Adam’,’Bart’]
b.计算列表长度并输出
c.列表中追加元素"seven"，并输出添加后的列表
d.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
e.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0])
print(L[1][2])
print(L[2][:2])#:切片，取值是顾头不顾尾，注：切片的步长默认为1，不可为0
print(len(L))#len() 计算长度
L.append(['seven'])#append()追加单个元素
print(L)
L.extend([['hello'],['linda']])#extend() 追加多个元素
print(L)
L.insert(0,['Tony'])#insert()插入元素
print(L)
L[1] = ['Kelly']# 修改元素
print(L)





