# 使用xlrd模块，第三方的工具包可以读取xlsx，xls的文件，写入是用xlwt
import xlrd
import os
from PyModule.student_info import StudentInfo

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'../PyFile/studentsinfo.xlsx')
#创建工作簿对象
workbook = xlrd.open_workbook(excel_path)
#创建表格对象
sheet = workbook.sheet_by_name('Sheet1')#注意区分大小写
print('总行数：', sheet.nrows)#获取总行数
print('总列数：', sheet.ncols)#获取总列数
print('第一行的数据：', sheet.row(0))#获取单行的数据，注意行和列的下标均从0开始
print('单元格数据：', sheet.cell_value(2, 1))#获取单元格数据，行 列

'''
excel中的数据类型对应关系：
    空（empty）       0
    字符串（string）    1
    数字（number）     2
    日期（date）     3
    布尔（boolean）     4
    error   5
'''
print('单元格数据类型：', sheet.cell_type(2, 1))

#读取excel并保存数据为列表
# “//”，在python中，这个叫“地板除”，3//2=1
# “%”，这个是取模操作，也就是区余数，4%2=0，5%2=1
students_info = []
for i in range(1, sheet.nrows):
    student_info = []
    for j in range(sheet.ncols):
        if sheet.cell_type(i, j) == 2 and sheet.cell_value(i, j) % 1 == 0:#解决xlrd自动将数字转成浮点型问题
            cell_value = int(sheet.cell_value(i, j))
        else:
            cell_value = sheet.cell_value(i, j)
        student_info.append(cell_value)
    students_info.append(student_info)
print(students_info)

# 读取数据保存为对象

stus_info = [] #列表存放对象
for i in range(1, sheet.nrows):
    student = StudentInfo(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2),
                          sheet.cell_value(i, 3), sheet.cell_value(i, 4))
    stus_info.append(student)

for i in range(len(stus_info)):
    print(stus_info[i].stu_name)