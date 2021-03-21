#类封装
import xlrd
import os
from PyModule.student_info import StudentInfo
from Utils.log_utils import log_obj # 直接导入日志对象
class ReadExcel:
    def __init__(self,excel_path):
        self.excel_path = excel_path

    def read_excel_save_list(self):
        try:#异常处理
            workbook = xlrd.open_workbook(self.excel_path)
            log_obj.info('创建工作簿workbook对象成功')
        except FileNotFoundError as e:
            log_obj.error('文件路径不存在，系统将使用默认路径') # 打印日志至文件中
            print('文件路径不存在，系统将使用默认路径')
            current_path = os.path.dirname(__file__)
            excel_path = os.path.join(current_path, '../PyFile/studentsinfo.xlsx')
            workbook = xlrd.open_workbook(excel_path)
        except Exception as e:
            print(e)
            log_obj.error('系统异常')
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

    # 读取数据转成对象封装成函数
    def read_excel_save_list_obj(self):
        try:  # 异常处理
            workbook = xlrd.open_workbook(self.excel_path)
        except FileNotFoundError as e:
            log_obj.error(f'文件路径不存在{e}')
            print('文件路径不存在，系统将使用默认路径!!')
            current_path = os.path.dirname(__file__)
            excel_path = os.path.join(current_path, '../PyFile/studentsinfo.xlsx')
            workbook = xlrd.open_workbook(excel_path)
        except Exception as e:
            print(e)
            log_obj.error(f'系统异常{e}')
        sheet = workbook.sheet_by_index(0)  # 注意区分大小写
        stus_info = []  # 列表存放对象
        for i in range(1, sheet.nrows):
            student = StudentInfo(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2),
                                  sheet.cell_value(i, 3), sheet.cell_value(i, 4))
            stus_info.append(student)
        return stus_info

# 测试类功能
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../PyFile--/studentsinfo.xlsx')
    test_students = ReadExcel(excel_path)
    log_obj.debug(f'{excel_path}文件读取成功')
    stus_info = test_students.read_excel_save_list()
    for i in range(len(stus_info)):
        print(stus_info[i])
    students_obj = test_students.read_excel_save_list_obj()
    for i in range(len(students_obj)):
        print(students_obj[i].stu_name)
