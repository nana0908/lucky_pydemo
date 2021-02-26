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
dt = datetime.datetime(2021,2,26,17,31,33,0)#(年、月、日、时、分、秒、微秒)
print( dt.year )#截取时间元组中的部分
#获取当前时间
nowdt = datetime.datetime.today()
nowdt01 = datetime.datetime.now()
print( '当前时间：',nowdt )
print( '当前时间：',nowdt01 )
#获取时间戳
dt_str = dt.timestamp()
print( '当前时间时间戳',dt.timestamp() )
print( datetime.datetime.fromtimestamp(int(dt_str)) )#时间戳转时间
#按自定义格式返回字符串
print( '时间格式化：',dt.strftime('%Y-%m-%d') )
#英文显示
print( dt.ctime() )

