'''
模拟简单的计算器，要求如下：
定义名为Number的类
其中有两个整型数据成员n1和n2
应声明为私有。编写构造方法：赋予n1和n2初始值
再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有成员方法
分别对两个成员变量执行加、减、乘、除的运算。
创建Number类的对象，调用各个方法，并显示计算结果。

定义名为MyTime的类：
其中应有三个整型成员：时（hour）、分（minute）、秒（second）
1）为了保证数据的安全性，这三个成员变量应声明为私有。
2）为MyTime类定义构造方法，以方便创建对象时初始化成员变量。
3）再定义diaplay方法，用于将时间信息打印出来。
4）为MyTime类添加以下方法addSecond(int sec) addMinute(int min) addHour(int hou) subSecond(int sec)
subMinute(int min) subHour(int hou) 分别对时、分、秒进行加减运算。
5）定义封装的get和set方法，方便另外一个类对三个私有变量进行使用，并写成另外类如何调用该方法


设计一个交通工具类vehicle，
其中的属性包括速度speed、种类kind、颜色color；方法包括：设置颜色setColor，取得颜色getColor。再设计一个子类Car，增加属性passenger表示可容纳旅客人数，添加方法取得最大速度getMaxSpeed()。对两个类都进行初始化构造
创建Car的对象，输出Car的所有属性


创建一个父类Animal类
属性：姓名、动物种类、年龄、性别
方法：吃
在父类的基础上创建两个子类 Dog cat ，新有尾巴、奔跑速度属性
新有方法：跑  叫
要求，新建对象时所有的属性都能进行初始化


1、在异常处理中这些try、except、else、finally、raise有什么含义
2、创建一个用户自定义异常UsernameInputError,如果用户用户名输入错误，能通过捕获错误并提示用户名***输入错误
3、调研完成python读取 .ini文件
'''