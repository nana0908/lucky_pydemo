print("函数与字符串的应用")
# 例1：设计一个生成指定长度验证码的函数,验证码由数字和英文大小字母构成

import random
import string
ALL_CHARS = '0123456789abcdefghigklmopqrsturwxyzABCDEFGHIJKLMNOPQRSTURWXYZ'
# 可以利用Python标准库中的string 模块来获得数字和英文字母的字面常量
ALL_CHARS1 = string.digits + string.ascii_letters
print(ALL_CHARS1)
def generate_code(gen_len = 4):
    code = ''
    for _ in range(gen_len):
        index = random.randrange(0,len(ALL_CHARS))# randrange() 方法返回指定递增基数集合中的一个随机数,基数缺省值为1
        code += ALL_CHARS[index]
    return code

# 例2：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename):
    pos = filename.rfind('.') # 从字符串中逆向查找.出现的位置
    return filename[pos + 1:]
print(generate_code(5))
print(get_suffix('123.txt'))
