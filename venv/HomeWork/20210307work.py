'''
1、模拟简单的计算器，要求如下：
定义名为Number的类
其中有两个整型数据成员n1和n2
应声明为私有。编写构造方法：赋予n1和n2初始值
再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有成员方法
分别对两个成员变量执行加、减、乘、除的运算。
创建Number类的对象，调用各个方法，并显示计算结果。
'''

class Number:
    def __init__(self,n1,n2):
        self.__n1 = n1
        self.__n2 = n2
    def addition(self):
        return (self.__n1 + self.__n2)
    def subtration(self):
        return (self.__n1 - self.__n2)
    def multiplication(self):
        return (self.__n1 * self.__n2)
    def division(self):
        return (self.__n1 / self.__n2)
num1 = int(input('please input number1：'))
num2 = int(input('please input number1：'))
value = Number(num1,num2)
print(f'{num1}+{num2}={value.addition()}')
print(f'{num1}-{num2}={value.subtration()}')
print(f'{num1}*{num2}={value.multiplication()}')
print(f'{num1}/{num2}={value.division()}')



'''
2、创建一个学生类：
属性：姓名，年龄，学号 方法：答到，展示学生信息
类属性：名称

创建一个班级类：
属性：学生，班级名 方法：添加学生，删除学生，点名
'''
'''
class Student:
    studentname = ['xiaoming','zhangsan','lisi']
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def answer(self):
        if self.name in Student.studentname:
            print(f'我是{self.name},我到了')
        else:
            print('学生不存在')
    def studentInfo(self):
        print(f'{self.name},{self.age},{self.id}')

class SClass(Student):
    def __init__(self,name,age,id,classname):
        super().__init__(name,age,id)
        self.classname = classname
    def addstudent(self,sname):
        if sname in Student.studentname:
            print('学生已存在')
        else:
            Student.studentname.append(sname)
            print('添加成功')

    def delstudent(self,sname):
        if sname in Student.studentname:
            Student.studentname.remove(sname)
            print('删除成功')
        else:
            print('学生不存在')
    def rollcall(self):
        for i in Student.studentname:
            print('点名：',i)

sevenclss = SClass('xiaoming',24,'001','7班')
sevenclss.answer()
sevenclss.studentInfo()
sevenclss.addstudent('libai')
sevenclss.delstudent('lisi')
sevenclss.rollcall()
'''
class Student:
    name01 = None
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def replied(self):#答到方法
        print(f'我叫{self.name},今年{self.age}岁了，学号是{self.id}')

class SClass():
    students = []#存类对象
    def __init__(self,Student,classname):#Student为类对象
        self.students.append(Student)
        self.classname = classname
    def addstudent(self,name,age,id):
        self.students.append(Student(name,age,id))

    def delstudent(self,name):
        names = []
        for i in range(len(self.students)):
            names.append(self.students[i].name)
        if name in names:
            for j in range(len(self.students)):
                if name == self.students[j].name:
                    self.students.remove(self.students[j])#删除学生
                    break
        else:
            print(f'{name}不存在')
    def rollcall(self,name):
        names = []
        for i in range(len(self.students)):
            names.append(self.students[i].name)
        if name in names:
            for j in range(len(self.students)):
                if name == self.students[j].name:
                    self.students[j].replied()#点名
        else:
            print(f'{name}不存在')

zhangsan = Student('zhangsan',23,'001')
sevenclass = SClass(zhangsan,'7class')
sevenclass.rollcall('zhangsan')
sevenclass.addstudent('lisi',24,'002')
sevenclass.rollcall('lisi')
sevenclass.delstudent('lisi')#删除lisi
sevenclass.rollcall('lisi')

'''
3、设计一个车类，属性：车的类型、车的速度、
分别再建立两个子类：小汽车类、电动汽车类 去继承车类
为了实现汽车增加能源的方式，在父类中添加 一个增加能源方法 increased_energy() 做出抽象方法
实现小汽车类加 油  电动汽车充电的不同实现
'''

from abc import ABCMeta,abstractmethod
class Car(metaclass=ABCMeta):
    def __init__(self,type,speed):
        self.type = type
        self.speed = speed
    @abstractmethod
    def increased_energy(self):
        pass

class SmallCar(Car):
    def __init__(self,type,speed):
        super().__init__(type,speed)
    def increased_energy(self):
        print('小汽车加油')

class ElectricCar(Car):
    def __init__(self,type,speed):
        super().__init__(type,speed)
    def increased_energy(self):
        print('电动汽车充电')

scar = SmallCar('小汽车','100m/s')
scar.increased_energy()
ecar = ElectricCar('电动汽车','110m/s')
ecar.increased_energy()

'''
4、设计一个数据类型类 DataType ,包含一个抽象方法 length 方法，
并建立多个子类（Dict、List、String、Tuple）对length 方法进行实现：
如Dict子类 实现length方法功能，输出显示“字典形式的数据，包含3个项”，依次类推
创建一个get_length方法，能实现传入不同的子类对象，输出不同的求长度的结果
'''

from abc import ABCMeta,abstractmethod
class DataType(metaclass=ABCMeta):
    def __init__(self,data):
        self.data = data
    @abstractmethod
    def length(self):
        pass
class Dict(DataType):
    def __init__(self,data):
        super().__init__(data)
    def length(self):
        print(f'字典形式的数据，长度为{len(self.data)}')
class List(DataType):
    def __init__(self,data):
        super().__init__(data)
    def length(self):
        print(f'列表形式的数据，长度为{len(self.data)}')
class String(DataType):
    def __init__(self,data):
        super().__init__(data)
    def length(self):
        print(f'字符串形式的数据，长度为{len(self.data)}')
class Tuple(DataType):
    def __init__(self,data):
        super().__init__(data)
    def length(self):
        print(f'元组形式的数据，长度为{len(self.data)}')

dict01 = Dict({'name':'lisa','tel':'1667347588','age':23})
list01 = List([1,2,3,4,5])
string = String('helloworld')
tuple01 = Tuple((1,2,3,2,3))

def get_length(object):
    object.length()

get_length(dict01)
get_length(list01)
get_length(string)
get_length(tuple01)
#print(type(dict01))
# def get_length(object):
#     if isinstance(object,dict):#isinstance(o,type)判断对象类型
#         dict_01 = Dict()
#         dict_01.length(object)
#     elif isinstance(object,list):
#         list_01 = List()
#         list_01.length(object)
#     elif isinstance(object,str):
#         string = String()
#         string.length(object)
#     elif isinstance(object,tuple):
#         tuple_01 = Tuple()
#         tuple_01.length(object)
# get_length(dict01)
# get_length(list01)
# get_length(string)
# get_length(tuple01)

'''
5、 写一个传奇游戏中的猪类，类中有属性：颜色、个头、攻击力、准确度。有一个展示猪信息的方法。
再写一个测试类，生成一个猪的对象，将此猪的颜色值为“白色”，个头为5厘米，攻击力为50点血，准确度为0.8。
要求输出此猪的信息格式为：一只白色的猪，个头5厘米，攻击为为50点血，准确度为0.8，我好怕怕呀
'''
class Pig:
    def __init__(self,color,size,aggressivity,accuracy):
        self.color = color
        self.size = size
        self.aggressivity = aggressivity
        self.accuracy = accuracy
whitePig = Pig('白色','5厘米','50点血','0.8')
print(f'一只{whitePig.color}的猪，个头{whitePig.size}，攻击为为{whitePig.aggressivity}，准确度为{whitePig.accuracy}，我好怕怕呀')

'''
6、 写一个牌的类，类中有属性：花色、值。有一个展示牌信息的方法。
要求写一个测试类，生成一张牌，将此牌的花色设为“梅花”，将此牌的值设为5。
最后显示此牌的信息，要求格式为:梅花5
'''
class Brand:
    def __init__(self,colortype,value):
        self.colortype = colortype
        self.value = value
plum_blossom5 = Brand('梅花','5')
print(f'{plum_blossom5.colortype}{plum_blossom5.value}')
'''
7、 写一个猪类，类中的属性：品种，颜色，攻击力。类中有方法：
     无返回值的方法：
    （一）猪走路的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪走来走去”。
    （二）猪打人的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪打人了，攻击力为多少”。
    (三）猪吃饭的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪吃得真多”。
     有返回值的方法：
    （一）显示自身信息的方法（show_info)。
    （二）得到此猪品种的方法，要求在此方法中没有输出，返回此猪的品种。
    （三）得到此猪颜色的方法，要求在此方法中没有输出，返回此猪的颜色。
'''
class Pig:
    def __init__(self,type,color,aggressivity):
        self.type = type
        self.color = color
        self.aggressivity = aggressivity
    def walk(self):
        print(f'{self.type}品种的{self.color}颜色的猪走来走去')
    def play(self):
        print(f'{self.type}品种的{self.color}颜色的猪打人了，攻击力为{self.aggressivity}')
    def eat(self):
        print(f'{self.type}品种的{self.color}的猪吃得真多')
    def show_info(self):
        return f'品种：{self.type},颜色：{self.color},攻击力：{self.aggressivity}'
    def get_type(self):
        return self.type
    def get_color(self):
        return self.color
blackPig = Pig('乌克兰','黑色','50点血')
blackPig.walk()
blackPig.play()
blackPig.eat()
print(blackPig.show_info())
print(blackPig.get_color())
print(blackPig.get_type())

'''
8、 写一个汽车的类，类中有属性：品牌，价格，颜色。类中有方法：
    （一）显示当前汽车对象的所有属性的方法show_info。
    （二）汽车启动的方法，要求输出“XX品牌的汽车启动了”。
    （三）汽车加速的方法，要求输出“XX品牌的汽车加速中”。
    （四）汽车被卖的方法，要求输出“XX品牌的汽车被以XX元的价格卖了”。
'''
class Car:
    def __init__(self,type,price,color):
        self.type = type
        self.price = price
        self.color = color
    def show_info(self):
        print(f'汽车品牌：{self.type}，汽车价格：{self.price}，汽车颜色：{self.color}')
    def start_up(self):
        print(f'{self.type}品牌的汽车启动了')
    def speed_up(self):
        print(f'{self.type}品牌的汽车加速中')
    def sale(self):
        print(f'{self.type}品牌的汽车被以{self.price}元的价格卖了')

baoma = Car('宝马','30w','白色')
baoma.show_info()
baoma.sale()
baoma.start_up()
baoma.speed_up()