import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../test_case/test_data.xlsx')
print(excel_path)

wb = xlrd.open_workbook(excel_path) # 创建工作簿对象
sheet = wb.sheet_by_index(0) # 创建表格对象
print(sheet.cell_value(1, 0)) # 对于合并的左上角首个单元格会返回真实值

# 合并的单元格都能获取到值，merged_cells属性获取文档中合并单元格的信息
print( sheet.merged_cells ) # 返回一个列表（合并单元格的起始行，结束行，起始列，结束列）

# 逻辑：凡是在merged_cells属性范围内的单元格，都要等于合并的左上角首个单元格的真实值
# 处理合并单元格的数据
def get_merge_cell_values(row_index, col_index):  # 设置合并单元格的值
    merged = sheet.merged_cells  # 获取表格内所有合并单元格的位置信息
    cell_value = None
    # 处理单元格数据
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中合并单元格的位置信息
        if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
            if (col_index >= clow and col_index < chigh):  # 列坐标判断
                cell_value = sheet.cell_value(rlow, clow)
                break  # 防止循环的进行判断，出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)  # 非单元格取单元格本身的值
        else:
            cell_value = sheet.cell_value(row_index, col_index)  # 非单元格取单元格本身的值
    return cell_value
print(get_merge_cell_values(2, 0))

def get_cell_value(row_index, col_index):
    merged = sheet.merged_cells  # 获取表格内所有合并单元格的位置信息

# 获取数据并转成字典列表
sheet_list = []
for i in range(1, sheet.nrows):
    row_dict = {}
    row_dict['事件'] = get_merge_cell_values(i, 0)
    row_dict['步骤序号'] = get_merge_cell_values(i, 1)
    row_dict['步骤操作'] = get_merge_cell_values(i, 2)
    row_dict['完成情况'] = get_merge_cell_values(i, 3)
    sheet_list.append(row_dict)

# for i in sheet_list:
#     print(i)
#
all_data_list = []
first_row = sheet.row(0)#把表头（第一行）取出来，为一个列表
print(first_row)
for i in range(1, sheet.nrows):#从第二行开始遍历
    row_dict = {}
    for j in range(sheet.ncols):#第一行的每一列数据作为dict的key
        row_dict[first_row[j].value] = get_merge_cell_values(i, j)
    all_data_list.append(row_dict)

print(all_data_list)
for i in all_data_list:
    print(i)

# for i in all_data_list:
#     case_list = {}
#     case_list.setdefault(i[])
a = {'one': 1, 'two': 2}
a.setdefault('one', 2) # 设置默认值，如果该key在dict中存在，不会修改dict中key的值
a.setdefault('three', 3) # 如果该key不存在，则新增该键值对
print(a)