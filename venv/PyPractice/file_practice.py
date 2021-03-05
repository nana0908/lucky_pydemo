#文件操作
'''
在PyFile目录下创建50个内容一样的文件

import os
os.chdir('D:/PycharmProjects/lucky_pydemo/venv/PyFile') #切换目录
for i in range(1,51):
    file = open('./%02d.txt' % i,'w')
    file.write('newdream')
    file.flush()
    file.close()
'''

#打开文件calc.txt文件(文件内容为：['3+5=\n', '4+6=\n', '7-2=\n', '8-3=\n', '22-8='])，取出来做计算
'''
思路：读取数据--尝试算出一行数据的结果（切片，取两个加数，做成一个字符串等式）
循环（把所有的等式放入一个列表）
writelines将list写入
'''
'''
file = open('D:/PycharmProjects/lucky_pydemo/venv/PyFile/calc.txt')
#print(file.readlines())
calc_list = []
for calc_str in file.readlines():
    lista = []
    if calc_str.__contains__('+'):
        lista = calc_str.split('+')#通过‘+’号拆分，如'3+5=\n' 拆为3 和 5=\n
        value = int(lista[0]) + int(lista[1][:lista[1].index('=')])#列表切片式中list[start, end], 返回的数据是索引为start到索引为end的所有值
    else:
        lista = calc_str.split('-')
        value = int(lista[0]) - int(lista[1][:lista[1].index('=')])
    calc_list.append(calc_str[:calc_str.index('=')+1] + str(value) + '\n')
print(calc_list)
file.close()
file = open('D:/PycharmProjects/lucky_pydemo/venv/PyFile/calc.txt','w')
file.writelines(calc_list)
file.flush()
file.close()
# str = '3+5=\n'
# list = str.split('+')
# print(list)
'''
#python读取excel文件
#思路：文件路径--支持软件（第三方库xlrd）--操作（写代码）== > 读第三方库操作方式
#pip install xlrd
import os
import xlrd
file_dir = os.path.dirname(os.getcwd())#os.path.dirname(os.getcwd()) 获取上级目录
file_path = file_dir.replace('\\','/')  + '/PyFile/test01.xlsx'
print(file_path)
excel = xlrd.open_workbook(file_path)#打开excel
#excel.sheet_names()#获取excel里面的工作表的sheet名称数组
sheet = excel.sheet_by_index(0)#根据下标获取对应的sheet表（表示第一个工作表）

nrows = sheet.nrows #获取sheet的最大行数
ncols = sheet.ncols #获取sheet的最大列数
print(f'sheet的最大行数：{nrows},\nsheet的最大列数为：{ncols}')

value = sheet.cell(0,0).value#获取第0行0列单元格的值
print(value)

for i in range(0,nrows):
    print(sheet.cell(i,0).value)#获取第i行第0列的值