# 函数封装
import xlrd
import os
from PyModule.student_info import StudentInfo

#读取数据转成list封装成函数
def read_excel_save_list(excel_path):
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_name('Sheet1')  # 注意区分大小写
    students_info = []
    for i in range(1, sheet.nrows):
        student_info = []
        for j in range(sheet.ncols):
            if sheet.cell_type(i, j) == 2 and sheet.cell_value(i, j) % 1 == 0:  # 解决xlrd自动将数字转成浮点型问题
                cell_value = int(sheet.cell_value(i, j))
            else:
                cell_value = sheet.cell_value(i, j)
            student_info.append(cell_value)
        students_info.append(student_info)
    return students_info

#读取数据转成对象封装成函数
def read_excel_save_list_obj(excel_path):
    workbook = xlrd.open_workbook(excel_path)
    sheet = workbook.sheet_by_index(0)  # 注意区分大小写
    stus_info = []  # 列表存放对象
    for i in range(1, sheet.nrows):
        student = StudentInfo(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2),
                              sheet.cell_value(i, 3), sheet.cell_value(i, 4))
        stus_info.append(student)
    return stus_info


#测试函数功能
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../PyFile/studentsinfo.xlsx')

stusInfo = read_excel_save_list(excel_path)
for i in range(len(stusInfo)):
    print(stusInfo[i])

stusinfo_obj = read_excel_save_list_obj(excel_path)
for i in range(len(stusinfo_obj)):
    print(stusinfo_obj[i].stu_name)

