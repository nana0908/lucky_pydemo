#面向对象的三大特征
'''
面向对象的三大特性：
    封装：保护隐私，隔离复杂度
        数据封装:把对象的属性具体的值隐藏起来，对外部显示的只是对象的属性名
        方法封装：只需要通过调用方法名访问，不需要知道访问的细节，隐私保护
    在类的外部调用私有属性、方法  实例._类名__方法名（）,因此python为弱面对对象语言，不能封死
    继承：可以从现有的class继承属性和方法，新的class称为子类。（继承即为子类获取父类属性和方法的过程）
        当子类没有构造方法时，默认可以调用父类的构造方法
        如果父类和子类都重新定义了构造方法，那么子类的构造方法不会调用父类的构造方法，如需要调用，有如下方法
            方法一：以父类名.方法调用。类名.__init__(self...)，必须传入self
            方法二：super().方法调用。这种方式不需要传入self
            方法三：super(子类名称，self).方法
        子类重写父类方法，执行方法时优先在自身类中查找，没有找到则去父类中找
        子类继承父类的所有公有属性和方法，而对于私有的属性和方法，子类是不继承的
    多继承：一个子类有多个父类，多个父类名之间用逗号隔开
        class SubClass（SuperClass1，SuperClass2）
        如果SubClass没有重新定义构造方法，他会自动调用第一个父类的构造方法，以第一个父类为中心，且只会执行第一个父类的构造方法
        如果SubClass重新定义了构造方法，需要显示去调用的构造方法，此时调用哪个父类的构造方法由自己决定
        并且若SuperClass1和SuperClass2中有同名的方法，通过字类的实例化队形去调用该方法时调用的是第一个父类中的方法（左边优先原则）
    多态：多态是指一类事务具有多种形态，只有存在父子类关系才会让一类事物具有多种不同的形态，
        因而多态的前提是必须要实现继承
        1. 序列类型有多种形态：字符串，列表，元组
        2. 动物有多种形态：猪，狗，猫，羊...
        多态性：具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数
'''
class People:
    def __init__(self,name,age,phone,idNo):
        self.name =name
        self.age = age
        self.phone = phone
        self.__idNo = idNo #数据的封装，以__开头,私有的属性，只能在类的内部使用，在类的外部是使用不了的
    #方法的封装，通过公有的方法来访问私有的属性
    def get_idno(self):#获取到idno
        return self.__idNo
    def set_idno(self,idno):#设置idno
        self.__idNo = idno
    def __info(self):
        print('私有方法')

zhangsan = People('zhangsan','25','14537470001','430903199007093456')
print(zhangsan.get_idno())#不能直接外部访问私有属性，只能通过调用方法
zhangsan._People__info()#在类的外部调用私有属性、方法  实例._类名__方法名（）

#练习，创建一个银行卡类，属性：id（卡号） 私有属性：password（密码），name（姓名），money（钱），idno（身份证）
# 方法：存钱，取钱，查余额，修改密码（判断密码是否正确），创建对象调用
class BankCardInfo:
    def __init__(self,id,name,password,idno,money):
        self.id = id
        self.__password = password
        self.__name = name
        self.__idno = idno
        self.__money = money
    def savemoney(self,smoney):
        self.__money += smoney
    def takemoney(self,tmoney):
        self.__money -= tmoney
    def querymoney(self):
        return f'当前余额为：{self.__money}'
    def setpassword(self,oldpasswd,newpasswd):
        if self.__password == oldpasswd:
            self.__password = newpasswd
            print('密码修改成功')
        else:
            print('密码错误')

nanbankinfo = BankCardInfo('001','nana','123456','430903199509012839',10000)
print(nanbankinfo.querymoney())
nanbankinfo.savemoney(1000)
print(nanbankinfo.querymoney())
nanbankinfo.takemoney(100)
print(nanbankinfo.querymoney())
nanbankinfo.setpassword('654321','123456')#密码错误
nanbankinfo.setpassword('123456','654321')#修改密码

#定义一个公共类（父类）
class Father:
    def __init__(self,name,age,sex,idno):
        self.name =name
        self.age = age
        self.sex = sex
        self.__idno = idno
    def say(self):
        print('说话')
    def sleep(self):
        print('父类方法：睡觉')
    def __driverCar(self):
        print('私有方法：开车')

class Students(Father):  #student 继承于people_01类
    #当子类没有构造方法时，默认可以调用父类的构造方法
    #当子类有构造方法时，子类必须手动调用父类的构造方法。一般都需要实现父类的构造方法，方法一：以父类名.方法调用，方法二：super()
    def __init__(self,name,age,sex,idno,classname):
        #people_01.__init__(self,name,age,sex,idno)#方法一：以父类名.方法调用。类名.__init__(self...)，必须传入self
        super().__init__(name,age,sex,idno)#方法二：super().方法调用。这种方式不需要传入self。
        #super(students, self).__init__(name,age,sex,idno)#方法三：super(子类名称，self).方法
        self.classname = classname
    def study(self):
        print('学习')
    def hobby(self):
        print('爱好')
    #子类重写父类方法，执行方法时优先在自身类中查找，没有找到则去父类中找
    def sleep(self):
        print('子类方法：睡觉')

#mike = Students('mike',19,'male')#当子类没有构造方法时，默认可以调用父类的构造方法
mike = Students('mike',20,'male','123456','7')
print(mike.name)
mike.say()#调用父类的方法
mike.study()#调用子类的方法
mike.sleep()#当父类和子类有相同方法名，优先执行子类（方法重写）

#练习：创建一个动物类，属性：颜色，名称，体重  方法：吃，睡觉，游泳（私有）
#创建一个狗类继承动物类，属性：品种，身高 方法：抓老鼠，看家
#创建狗类对象进行测试
class Animal:
    def __init__(self,color,weigth,name):
        self.color = color
        self.weigth = weigth
        self.name = name

    def eat(self):
        print('父类方法：吃')
    def sleep(self):
        print('父类方法：睡觉')
    def __swim(self):
        print('父类私有方法：游泳')

class Dog(Animal):
    def __init__(self,color,weigth,name,variety,high):
        super(Dog, self).__init__(color,weigth,name)
        self.variety = variety
        self.high = high
    def catch_mouse(self):
        print('子类方法：抓老鼠')
    def look_house(self):
        print('子类方法：看家')

xiaobai = Dog('白色','20斤','小白','萨摩耶','40cm')
print(xiaobai.name)#调用父类属性
print(xiaobai.variety)#调用子类属性
xiaobai.sleep()#调用父类方法
xiaobai.catch_mouse()#调用子类方法

#多继承
class Cls01:
    def __init__(self,name):
        self.name = name
        print('Cls01的构造方法')
    def fun01(self):
        print('第一个类的方法1')

class Cls02:
    def __init__(self,name01):
        self.name01 = name01
        print('Cls02的构造方法')
    def fun01(self):
        print('第二个类的方法1')

class Cls03(Cls01,Cls02):#多继承，左边优先
    #当父类中有同名的方法，那么就按照继承的先后顺序执行
    #调用多个父类的构造方法
    def __init__(self,name,name01,name02):
        Cls01.__init__(self,name)
        Cls02.__init__(self,name01)
        self.name02 = name02
    def fun01(self):
        print('子类方法1')
    def fun04(self):
        print('子类方法2')

class Cls04(Cls01,Cls02):
    pass#当subclass没有重新定义构造方法，会自动调用第一个父类的构造方法，以第一个父类为中心，只会执行第一个父类的构造方法

class Cls05(Cls01,Cls02):
    def __init__(self,name):
        Cls02.__init__(self,name)#子类重新定义构造方法，需要显示去调用的父类构造方法，此时调用哪个父类由自己决定

zhang = Cls03('zhangsan','lisi','wangwu')
print(zhang.name)
zhang.fun01()
cc = Cls04('cc')#当subclass没有重新定义构造方法，只会执行第一个父类的构造方法
cc.fun01()
li = Cls05('lisi')
li.fun01()#同名的方法，调用的是第一个父类中的方法

#isinstance(obj,Class)用于检查实例类型，检查对象是否属于某个类==对象是都是类创建的
#issubclass(sub,sup)用于检查类继承
print( isinstance(zhang,Cls03) )
a = 'hello'
print( isinstance(a,str) )#检查对象类型

print( issubclass(Cls03,Cls01) )

from abc import ABCMeta,abstractmethod
class File(metaclass=ABCMeta):
    @abstractmethod
    def double_click(self):
        pass

class TxtFile(File):
    def double_click(self):
        print('open file')
class ExeFile(File):
    def double_click(self):
        print('exeute file')
class VideoFile(File):
    def double_click(self):
        print('player file')

def double_click(file_object):#多态性
    file_object.double_click()

txt_file = TxtFile()
exe_file = ExeFile()

double_click(txt_file)
double_click(exe_file)
