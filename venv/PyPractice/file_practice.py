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