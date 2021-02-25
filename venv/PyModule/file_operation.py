'''
python文件操作：python提供了必要的函数和方法进行默认情况下的文件操作，可以用file对象做大部分的文件基本操作
open函数：打开一个文件，创建一个file对象
    语法：file object = open（file_name,access_mode,buffring）
    #file_name :你想要访问的文件名称
    #access_mode:打开文件的模式：只读（r），写入（w），追加（a），默认只读
    #buffing：0：不会有寄存，1：访问文件寄存行，>1:寄存取缓冲大小，<0:取系统默认缓冲大小
'''
import os

print( os.getcwd() )#显示文件的当前位置（相对）
print( os.path.abspath(__file__) )#显示文件的绝对位置
print( os.path.dirname(__file__) )#显示文件的目录名
#open()
file01 = open('D:/PycharmProjects/lucky_pydemo/venv/PyFile/demo_01.txt')
content01 = file01.read(3)#read(3):读取当前位置的3个字符

print('当前文件位置',file01.tell())#tell()函数，获取文件指针当前位置

#seek()函数，更改文件指针位置，语法：seek(offset,from),offset:偏移量，from：0（起始位置，1（当前位置），2（文件末尾），其中1和2只能在带b模式下）
# 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常
file01.seek(5,0)#从起始位置开始偏移5位开始读取
print('当前文件位置',file01.tell())#偏移文件指针之后获取当前文件位置，位置变为5

content02 = file01.read()#read()：读取整个文件，会让文件指针移位，从第三个位置开始读取
print(content01)
print(content02)

print( 'file01文件是否关闭',file01.closed )#判断文件是否关闭
file01.close()
print( 'file01文件是否关闭',file01.closed )#判断文件是否关闭
print( 'file01文件编码',file01.encoding )#文件编码
print( 'file01文件名称',file01.name )#文件名称
print( 'file01文件模式',file01.mode )#文件模式

file02 = open('D:/PycharmProjects/lucky_pydemo/venv/PyFile/demo_02.txt','rb')
line01 = file02.readline()#readline() 读取一行，和read函数一样，指针移位
print('当前文件位置',file02.tell())#偏移文件指针之后获取当前文件位置，位置变为5
file02.seek(5,1)#从起始位置开始偏移5位开始读取
print('当前文件位置',file02.tell())#偏移文件指针之后获取当前文件位置，位置变为5
line02 = file02.readline(2)#readline() 读取一行中的2个字符
lines = file02.readlines()#读取所有行
print('line01:',line01)
print('line02:',line02)
print('lines:',lines)

file03 = open('D:/PycharmProjects/lucky_pydemo/venv/PyFile/demo_03.txt','w',encoding='utf-8')#以写的方式打开文件，没有存在文件就新建
print( file03.writable() ) #判断文件是否可写
file03.write('012345678\n') # 写的时候，之前的文件内容会被覆盖
file03.writelines(['china\n','中国\n','000\n'])
file03.flush()#刷新文件内部缓冲

#rename()方法重命名 rename('旧文件名','新文件名')
os.rename('','')
#remove(filename) 删除文件

