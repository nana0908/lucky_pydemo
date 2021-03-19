'''
模拟简单的计算器，要求如下：
定义名为Number的类
其中有两个整型数据成员n1和n2
应声明为私有。编写构造方法：赋予n1和n2初始值
再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有成员方法
分别对两个成员变量执行加、减、乘、除的运算。
创建Number类的对象，调用各个方法，并显示计算结果。
'''
# class Number:
#     def __init__(self,n1,n2):
#         self.__n1 = n1
#         self.__n2 = n2
#     def addition(self):
#         print(f'{self.__n1} + {self.__n2} = {self.__n1 + self.__n2}')
#     def subtration(self):
#         print(f'{self.__n1} - {self.__n2} = {self.__n1 - self.__n2}')
#     def multiplication(self):
#         print(f'{self.__n1} * {self.__n2} = {self.__n1 * self.__n2}')
#     def division(self):
#         print(f'{self.__n1} / {self.__n2} = {self.__n1 / self.__n2}')
# try:
#     n1 = int(input('请输入数字一：'))
#     n2 = int(input('请输入数字二：'))
# except ValueError as e:
#     print('请输入int型数字')
# except Exception as e:
#     print(e)
# else:
#     value = Number(n1,n2)
#     value.addition()
#     value.subtration()
#     value.multiplication()
#     value.division()


'''
定义名为MyTime的类：
其中应有三个整型成员：时（hour）、分（minute）、秒（second）
1）为了保证数据的安全性，这三个成员变量应声明为私有。
2）为MyTime类定义构造方法，以方便创建对象时初始化成员变量。
3）再定义diaplay方法，用于将时间信息打印出来。
4）为MyTime类添加以下方法addSecond(int sec) addMinute(int min) addHour(int hou) subSecond(int sec)
subMinute(int min) subHour(int hou) 分别对时、分、秒进行加减运算。
5）定义封装的get和set方法，方便另外一个类对三个私有变量进行使用，并写成另外类如何调用该方法
'''
class MyTime:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def display(self):
        print(f'时间为：{self.__hour}时{self.__minute}分{self.__second}秒')
    def addSecond(self,sec):
        if self.__second + sec > 60:
            print(f'{sec}秒之后秒数为：{self.__second + sec - 60}秒')
        else:
            print(f'{sec}秒之后秒数为：{self.__second + sec}秒')
    def addMinute(self,min):
        if self.__minute + min > 60:
            print(f'{min}分钟之后分钟数为：{self.__minute + min - 60}分')
        else:
            print(f'{min}分钟之后分钟数为：{self.__minute + min}分')
    def addHour(self,hou):
        if self.__hour + hou > 24:
            print(f'{hou}小时之后小时数为：{self.__hour + hou - 24}时')
        else:
            print(f'{hou}小时之后小时数为：{self.__hour + hou}时')
    def subSecond(self,sec):
        if self.__second - sec < 0:
            print(f'{sec}秒之后秒数为：{self.__second - sec + 60}秒')
        else:
            print(f'{sec}秒之后秒数为：{self.__second - sec}秒')
    def subMinute(self,min):
        if self.__minute - min < 0:
            print(f'{min}分钟之后分钟数为：{self.__minute - min + 60}分')
        else:
            print(f'{min}分钟之后分钟数为：{self.__minute - min}分')
    def subHour(self, hou):
        if self.__hour - hou < 0:
            print(f'{hou}小时之后小时数为：{self.__hour - hou + 24}时')
        else:
            print(f'{hou}小时之后小时数为：{self.__hour - hou}时')
    def getSecond(self):
        return self.__second
    def setSecond(self,sec):
        self.__second = sec
        return self.__second
    def getMinute(self):
        return self.__minute
    def setMinute(self,min):
        self.__minute= min
        return self.__minute
    def getHour(self):
        return self.__hour
    def setHour(self,hou):
        self.__hour = hou
        return self.__hour

# time = MyTime(10,36,40)
# time.addSecond(70)
# time.addSecond(10)
# time.subHour(10)
# time.subHour(20)
class GetTime:
    def __init__(self,Time):
        self.time = Time
    def get_time(self):
        print(f'{self.time.getHour()}时{self.time.getMinute()}分{self.time.getSecond()}秒')
    def set_time(self,hou,min,sec):
        print(f'修改后时间为：{self.time.setHour(hou)}时{self.time.setMinute(min)}分{self.time.setSecond(sec)}秒')

# set_time = GetTime(time)
# set_time.get_time()
# set_time.set_time(12,10,34)
'''
设计一个交通工具类vehicle，
其中的属性包括速度speed、种类kind、颜色color；方法包括：设置颜色setColor，取得颜色getColor。
再设计一个子类Car，增加属性passenger表示可容纳旅客人数，添加方法取得最大速度getMaxSpeed()。
对两个类都进行初始化构造
创建Car的对象，输出Car的所有属性
'''
class Vehicle:
    def __init__(self,speed,kind,color):
        self.speed = speed
        self.kind = kind
        self.color = color
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color

class Car:
    def __init__(self,Vehicle,passenger):
        self.vehicle = Vehicle
        self.passenger = passenger
    def getMaxSpeed(self):
        print(f'最大速度为：{self.vehicle.speed}')
# veh = Vehicle('1000m/s','宝马','白色')
# car = Car(veh,4)
# print(car.vehicle.speed)
# print(car.vehicle.kind)
# print(car.vehicle.color)
# print(car.passenger)
# car.getMaxSpeed()


'''

创建一个父类Animal类
属性：姓名、动物种类、年龄、性别
方法：吃
在父类的基础上创建两个子类 Dog cat ，新有尾巴、奔跑速度属性
新有方法：跑  叫
要求，新建对象时所有的属性都能进行初始化
'''
class Animal:
    def __init__(self,name,kind,age,sex):
        self.name = name
        self.kind = kind
        self.age = age
        self.sex = sex
    def eat(self):
        print('我要吃东西啦')
class Dog(Animal):
    def __init__(self,name,kind,age,sex,tail,speed):
        super().__init__(name,kind,age,sex)
        self.tail = tail
        self.speed = speed
    def run(self):
        print('狗跑')
    def call(self):
        print('汪汪汪')
class Cat(Animal):
    def __init__(self,name,kind,age,sex,tail,speed):
        super().__init__(name,kind,age,sex)
        self.tail = tail
        self.speed = speed
    def run(self):
        print('猫跑')
    def call(self):
        print('喵喵喵喵~')
wangcai = Dog('wangcai','茶杯犬',3,'男','小短尾巴','10m/s')
tom = Cat('Tom','布偶',2,'女','毛茸茸的尾巴','5m/s')
wangcai.call()
tom.run()
'''
1、在异常处理中这些try、except、else、finally、raise有什么含义
执行try中的语句都会判断是否出现异常，如果出现异常则会跳到except判断异常
except 判断异常
else 如未引发异常才能执行else中的语句，否则跳过不执行
finally 不管是否发生异常都会执行
raise 自定义异常，触发异常
'''
'''
2、创建一个用户自定义异常UsernameInputError,如果用户用户名输入错误，能通过捕获错误并提示用户名***输入错误
'''
class UsernameInputError(Exception):#自定义异常需继承Exception
    # def __str__(self):
    #     return '用户名不正确'
    pass

user_names = ['admin','nana']
user_name = input('请输入用户名：')
if user_name not in user_names:
    try:
        raise UsernameInputError(f'{user_name}用户不正确')
    except UsernameInputError as e:
        print(e)
else:
    print('用户名正确')
'''
3、调研完成python读取 .ini文件
'''
