'''
日期、时间操作
在python中常用time和datetime模块处理时间
time模块一般用用4中方式显示时间
    时间元组：即用一个元组组装起来的9组数字处理时间
        t = (2021,2,26,17,31,33,0,0,0):(年，月，日，时，分，秒，一周的第几日，一年的第几日，夏令时)
    时间戳:time.mktime(t)
    格式化显示：time.strftime('时间格式',时间元组)/time.strftime('str',’时间格式‘),,即字符串，时间元组相互转换
    英文显示：time.asctime(t)
'''
import time
t = (2021,2,26,17,31,33,0,0,0)#(年，月，日，时，分，秒，一周的第几日，一年的第几日，夏令时)
now = time.time() #获取当前时间戳
now_trple = time.localtime(now) #时间戳转元组
t_str = time.strftime('%Y-%m-%d %H-%M-%S %p',t) #格式化元组时间
print( int(now) )
print( time.mktime(t) )#给定时间的时间戳
print( now_trple )#转换时间戳为元组
print( t_str )
print( time.strftime('%Y-%m-%d %p') )
print( time.asctime( now_trple ) )#英文显示

'''
datatime模块 
    date:处理年月日
    time：处理时分秒、微秒
    datetime：处理年月日、时分秒、微秒
'''
import datetime

# 时间元组表示
dt = datetime.datetime(2021,3,3,17,31,33,0)#(年、月、日、时、分、秒、微秒)
print('元组表示时间打印时自动格式化：',dt)
print( '截取dt部分时间--获取年',dt.year )#截取时间元组中的部分
print( '截取dt部分时间--获取月',dt.month )#截取时间元组中的部分
print( '截取dt部分时间--获取日',dt.day )#截取时间元组中的部分
print( '截取dt部分时间--获取日期',dt.date() )#获取日期
print( '截取dt部分时间--获取时间',dt.time())#获取时间
print( '截取dt部分时间--获取星期',dt.weekday())#获取星期,从0开始，周一为0（0-6）
print( '截取dt部分时间--获取星期',dt.isoweekday())#正常计算星期（从1开始）（1-7）
#获取当前时间
nowdt = datetime.datetime.today()#获取当前系统时间
nowdt01 = datetime.datetime.now()
print( '当前时间：',nowdt )
print( '当前时间：',nowdt01 )
#获取时间戳
dt_str = dt.timestamp()#时间转时间戳
print( '当前时间时间戳',dt.timestamp() )
print( '时间戳转时间',datetime.datetime.fromtimestamp(dt_str) )#时间戳转时间
print( '时间戳转时间,先将时间转成时间戳，再转时间',dt.fromtimestamp(dt_str) )#时间戳转时间

#按自定义格式返回字符串
print( '时间格式化：',dt.strftime('%Y-%m-%d') )
print( '当前时间格式化：',dt.strftime('%Y-%m-%d %H:%M:%S %p'))#大小写意义不一样
#英文显示
print( dt.ctime() )

