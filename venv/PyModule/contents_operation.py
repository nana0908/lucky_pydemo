'''
目录操作
os.mkdir():创建目录
os.makedirs():可建多级目录
os.chdir():切换目录
os.rmdir():删除空目录
os.getcwd():获取当前目录
os.path.isdir(''):判断目录是否存在
shutil.rmtree():删除非空目录

'''
import os
import shutil
#os.mkdir('')#
#shutil.rmtree()#删除非空目录
print( os.getcwd() )#获取当前目录
print( os.path.isdir('D:/PycharmProjects/lucky_pydemo/venv/PyModule') )#判断目录是否存在

if not os.path.isdir('D:/PycharmProjects/lucky_pydemo/venv/PyModule'):
    os.mkdir('D:/PycharmProjects/lucky_pydemo/venv/PyModule')
    #os.makedirs('')#可建多级目录
else:
    print('目录已经存在')