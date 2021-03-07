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
    多继承：一个子类有多个父类
    多态：
'''
class people:
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

zhangsan = people('zhangsan','25','14537470001','430903199007093456')
print(zhangsan.get_idno())#不能直接外部访问私有属性，只能通过调用方法
zhangsan._people__info()#在类的外部调用私有属性、方法  实例._类名__方法名（）

#练习，创建一个银行卡类，属性：id（卡号） 私有属性：password（密码），name（姓名），money（钱），idno（身份证）
# 方法：存钱，取钱，查余额，修改密码（判断密码是否正确），创建对象调用
class bankcardinfo:
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

nanbankinfo = bankcardinfo('001','nana','123456','430903199509012839',10000)
print(nanbankinfo.querymoney())
nanbankinfo.savemoney(1000)
print(nanbankinfo.querymoney())
nanbankinfo.takemoney(100)
print(nanbankinfo.querymoney())
nanbankinfo.setpassword('654321','123456')#密码错误
nanbankinfo.setpassword('123456','654321')#修改密码

#定义一个公共类（父类）
class father:
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

class students(father):  #student 继承于people_01类
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

#mike = students('mike',19,'male')#当子类没有构造方法时，默认可以调用父类的构造方法
mike = students('mike',20,'male','123456','7')
print(mike.name)
mike.say()#调用父类的方法
mike.study()#调用子类的方法
mike.sleep()#当父类和子类有相同方法名，优先执行子类（方法重写）

#练习：创建一个动物类，属性：颜色，名称，体重  方法：吃，睡觉，游泳（私有）
#创建一个狗类继承动物类，属性：品种，身高 方法：抓老鼠，看家
#创建狗类对象进行测试
class animal:
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

class dog(animal):
    def __init__(self,color,weigth,name,variety,high):
        super(dog, self).__init__(color,weigth,name)
        self.variety = variety
        self.high = high
    def catch_mouse(self):
        print('子类方法：抓老鼠')
    def look_house(self):
        print('子类方法：看家')

xiaobai = dog('白色','20斤','小白','萨摩耶','40cm')
print(xiaobai.name)#调用父类属性
print(xiaobai.variety)#调用子类属性
xiaobai.sleep()#调用父类方法
xiaobai.catch_mouse()#调用子类方法

#多继承
class cls01:
    def __init__(self,name):
        self.name = name
    def fun01(self):
        print('第一个类的方法1')

class cls02:
    def __init__(self,name01):
        self.name01 = name01
    def fun01(self):
        print('第二个类的方法1')

class cls03(cls01,cls02):#多继承
    #当父类中有同名的方法，那么就按照继承的先后顺序执行
    #调用多个父类的构造方法
    def __init__(self,name,name01,name02):
        cls01.__init__(self,name)
        cls02.__init__(self,name01)
        self.name02 = name02
    def fun01(self):
        print('子类方法1')
    def fun04(self):
        print('子类方法2')

zhang = cls03('zhangsan','lisi','wangwu')
print(zhang.name)
zhang.fun01()