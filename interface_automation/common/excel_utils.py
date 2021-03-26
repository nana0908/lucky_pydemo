# excel文件处理类
import os
import xlrd
class ExcelUtil:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # python支持在构造方法中调用类方法

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    def get_merge_cell_value(self, row_index, col_index):  # 设置合并单元格的值
        merged = self.sheet.merged_cells  # 获取表格内所有合并单元格的位置信息
        # 处理单元格数据
        for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中合并单元格的位置信息
            if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
                if (col_index >= clow and col_index < chigh):  # 列坐标判断
                    cell_value = self.sheet.cell_value(rlow, clow)
                    break  # 防止循环的进行判断，出现值覆盖的情况
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)  # 非单元格取单元格本身的值
            else:
                cell_value = self.sheet.cell_value(row_index, col_index)  # 非单元格取单元格本身的值
        return cell_value
    #取excel数据并以列表字典的形式返回
    def get_sheet_value_by_list(self):
        all_data_list = []
        first_row = self.sheet.row(0)
        for i in range(1, self.sheet.nrows):
            row_dict = {}
            for j in range(self.sheet.ncols):#第一行数据作为dict的key
                row_dict[first_row[j].value] = self.get_merge_cell_value(i, j)
            all_data_list.append(row_dict)
        return all_data_list


# 测试类
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../test_case/test_data.xlsx')
    excel_data = ExcelUtil(excel_path, 'Sheet1')
    print(excel_data.get_row_count())
    print(excel_data.get_merge_cell_value(3, 0))
    all_data = excel_data.get_sheet_value_by_list()
    for i in all_data:
        print(i)