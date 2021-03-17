#抽象类
'''
抽象类：包含抽象方法的类，而抽象方法不包含任何可实现的代码
    1、包含抽象方法
    2、抽象只定义不实现
    3、要有定义抽象的定义语句(定义必须之用python自带的abc.py库)，导入ABCMeta,abstractmethod方法
    4、抽象类是用来被继承的（子类必须实现父类的抽象方法），如果没有被继承那么毫无意义
'''
from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):#此方法必须实现抽象方法
    #定义抽象类
    #__metaclass__ = ABCMeta#此方法不是强制的必须实现抽象方法，不推荐使用
    def __init__(self,name):
        self.name = name
    #定义抽象方法
    @abstractmethod
    def say(self):#抽象方法，只声明不实现
        pass

class Dog(Animal):
    def say(self):#实现抽象方法
        print('实现抽象方法：汪汪~')
    def sleep(self):
        print('子类方法：睡觉')

class Cat(Animal):
    def say(self):
        print('实现抽象方法：喵喵~')
xiaohei = Dog('xiaohei')
print(xiaohei.name)
xiaohei.sleep()
dog = Dog('土狗')
cat = Cat('西瓜')
dog.say()
cat.say()

class People(metaclass=ABCMeta):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    @abstractmethod
    def goto_Class(self):
        pass

class Student(People):
    def __init__(self,name,sex,check_cource,check_teacher):
        super(Student, self).__init__(name,sex)
        self.check_cource = check_cource
        self.check_teacher = check_teacher
    def goto_Class(self):
        print(f'{self.name}去教室听课')

class Teacher(People):
    def __init__(self,name,sex,student_name):
        super(Teacher, self).__init__(name,sex)
        self.student_name = student_name
    def goto_Class(self):
        print(f'{self.name}去教室授课')

xiaoming = Student('小明','男','语文课','张老师')
zhang = Teacher('张老师','女','小明')
xiaoming.goto_Class()
zhang.goto_Class()
