import os
import xlrd
from PyPractice.students_base_info import StudentsBaseInfo
# excel_dir = os.path.dirname(os.getcwd())#os.path.dirname(os.getcwd()) 获取上级目录
# excel_path = file_dir.replace('\\','/')  + '/PyFile/test01.xlsx'
# print(file_path)
# excel = xlrd.open_workbook(file_path)#打开excel

current_path = os.path.dirname(__file__)#获取当前文件目录
excel_path = current_path.replace('\\','/') + '/../PyFile/studentsinfo.xlsx'#/../返回上级目录之后再做拼接
#excel_path = os.path.join(current_path,'../PyFile/studentsinfo.xlsx').replace('\\','/')#方法2：os.path.join 拼接
#print(excel_path)
def get_stu_info(file_path):
    workbook = xlrd.open_workbook(excel_path)#打开文件
    sheet = workbook.sheet_by_index(0)#根据下标获取对应的sheet表（表示第一个工作表）
    print(sheet.nrows,sheet.cell(1,0).value)
    students_infos = []
    for i in range(1,sheet.nrows):
        student_info = StudentsBaseInfo(sheet.cell(i,0).value,sheet.cell(i,1).value,sheet.cell(i,2).value,
                                        sheet.cell(i,3).value,sheet.cell(i,4).value)#创建学生信息对象（调用之前创建的学生信息类）
        #print(student_info.stu_name)
        students_infos.append(student_info)
    return students_infos

#测试方法
stus = get_stu_info(excel_path)
print(stus[1].stu_name)