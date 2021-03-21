# 日志模块
import logging, os
'''
python中日志等级
    DEBUG：程序调试bug时使用
    INFO：程序正常运行时使用
    WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
    ERROR：程序出错误时使用，如:IO操作失败
    CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用
五种日志级别按从低到高排序：
DEBUG < INFO < WARNING < ERROR < CRITICAL
'''
logger = logging.getLogger('python实战日志')# 创建日志对象

# 设置日志级别DEBUG < INFO < WARNING < ERROR < CRITICAL
logger.setLevel(level=logging.INFO)
# 在控制台打印对象
console = logging.StreamHandler() # 控制台输出对象
# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelno)s - %(levelname)s - %(lineno)d - %(message)s')
console.setFormatter(formatter) # 使用日志格式
console.setLevel(level=logging.ERROR) #console单独设置日志级别（局部优先）
logger.addHandler(console) # 设置日志在控制台打印
logger.info('我是日志模块打印的！！！')
logger.error('我是 ERROR 日志，设置console日志级别后，只有比达到设置的日志级别才会打印')
'''
日志格式：
名称	             说明
    %(levelno)s	打印日志级别的数值
    %(levelname)s	打印日志级别名称
    %(pathname)s	打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s	打印当前执行程序名
    %(funcName)s	打印日志的当前函数
    %(lineno)d	打印日志的当前行号
    %(asctime)s	打印日志的记录时间
    %(thread)d	打印线程ID
    %(threadName)s	打印线程的名称
    %(process)d	打印进程的ID
    %(message)s	打印日志的信息
————————————————
'''
# 将日志写入到日志文件中
current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../Log/python.log')

file_log = logging.FileHandler(log_path, encoding= 'utf-8')#创建文件类型的日志对象
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelno)s - %(levelname)s - %(lineno)d - %(message)s')
file_log.setFormatter(formatter)

# 将日志写入到文件中
logger.addHandler(file_log)
logger.info('info级别的日志写入到文件中')
logger.error('error级别的日志写入到文件')

