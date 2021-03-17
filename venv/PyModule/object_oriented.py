'''
20210303学习日志
1. 日期操作（datetime：获取日期，时间元组/时间戳/时间相互转换/时间格式化等）
2. 面向对象的概念（类和对象（特征和行为））
3. 需预习面向对象
'''
'''
#面向对象
#类：具有相同特征行为的某一类事务的总称 抽象出来
#对象：某个类重具体的一个实例（属性、方法）
    属性：类属性，实例属性，内置属性
        类属性可以通过对象和类访问
        实例属性只能通过对象访问
        内置属性可以通过对象和类访问
    方法：实例方法，类方法，静态方法，内置方法
        实例方法可以通过类和对象访问，但通过类访问实例方法时，self需要传值，会当作一个普通的方法
        类方法可以通过对象和类访问（不推荐使用）
        静态方法可以通过对象和类访问（不推荐用，静态方法会占用大量系统资源）
        常用的内置方法：python自带的方法
            __init__()：构造方法,有构造方法系统会默认调用，支持重载（方法名一样，参数列表不一样），但是系统会调用最后一个
            __del__():析构方法（删除），在释放对象时调用，系统默认调用，支持重载
            __str__():自定义实例输出方法，支持重载
            __add__():两个实例的加法操作
#类和对象的区别
'''
'''
创建类和对象。类命名：一般以驼峰式命名ClassName
创建类：class ClassName：
    pass（具体实现）
创建对象： 对象名称 = 类名()
'''
class People:
    '''我是People类的说明，只能放在第一行'''
    name = 'zhangsan'#类属性，类属性可以直接通过类调用

    #构造方法，完成对象的初始化，在创建对象的时候系统会默认调用
    def __init__(self,name,age,address,idno):
        self.name = name#self是python类中示例方法必带的一个参数，但不需要传值，相当于java中的this，代表对象本身
        self.age = age#实例属性
        self.address = address
        self.__idno = idno#私有属性，以__开头,私有的属性，只能在类的内部使用，在类的外部是使用不了的
    def say(self):#普通方法（称为：实例方法，第一个参数默认self）类里面的方法都会自带self参数，表示当前类的所有属性和方法
        print('类里面的方法')

    @classmethod#修饰器：classmethod下面的方法就是类方法，第一个参数默认cls，可以对类属性进行修改
    def run(cls):
        print('我是一个类方法')

    @staticmethod#修饰器：staticmethod下面的方法就是静态方法，静态方法没有默认参数
    def sleep():
        print('我是一个静态方法')

    def __del__(self):#内置方法--析构方法
        print('我是析构方法，我是在程序运行完之后自动释放资源，系统自动调用')

    def __str__(self):
        return '我是实例输出方法'

    def __add__(self, other):
        return self.age + other.age


# zhangsan = People()#创建对象
# print(zhangsan.name)#调用对象的属性和方法：对象名.属性或者方法名称
# zhangsan.say()
# del zhangsan#手动释放资源
zhangsan = People('zhangsan',20,'湖南岳阳')
lisi = People('lisi',24,'湖南长沙')#创建对象的时候直接初始化，（完成对象的初始化）
print(lisi.name)#通过对象访问类属性
print(People.name)#通过类名访问类属性
print(lisi.age)#实例属性只能通过对象访问
#内置属性：python中自带的属性： 类名.内置属性
print(People.__dict__)#打印出类的所有属性
print(People.__doc__)#类的文档字符串
print(lisi.__doc__)#通过对象访问内置属性，内置属性可以通过对象或类访问
print(People.__name__)#类名
print(People.__module__)#类定义所在的模块
print(People.__bases__)#类的所有父类构成元素
lisi.say()
People.say('汤姆')#通过类访问实例方法，此时self需要传值
lisi.run()
People.run()#类方法可以通过对象和类访问
lisi.sleep()
People.sleep()#静态方法可以通过对象和类访问
#练习：创建一个狗类，属性：name，age，color 方法：睡觉、吃、跑
print(zhangsan)#默认调用__str__方法
print(zhangsan.age + lisi.age)
print(zhangsan + lisi)#默认调用__add__()方法
class Dog:
    name = None
    age = None
    color = None
    def sleep(self):#无参函数
        print('我要睡觉啦')
    def eat(self,thing):#有参函数
        print(f'我要吃{thing}啦')
    def run(self):
        print('我跑了')

ahuang = Dog()
Dog.name = 'Ahuang'
Dog.age = 10
Dog.color = 'yellow'
print(f'我是{Dog.name},我{Dog.age}岁了，是一只{Dog.color}色的狗狗')
ahuang.sleep()
ahuang.run()
ahuang.eat('狗粮')


