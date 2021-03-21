# 读取.ini配置文件
import os
import configparser

current_path = os.path.dirname(__file__)
print('current_path:', current_path)
ini_path = os.path.join(current_path, '../Config/config.ini')
print('ini_path', ini_path)

conf = configparser.ConfigParser() # 创建对象
conf.read(ini_path, encoding= 'utf-8')
print('全部的组名：', conf.sections())
print('default组下的内容（键值对）：', conf.items())
print('某个组下所有的key', conf.options('default'))
print('组中的参数值：', conf.get('default', 'excel_path'))
