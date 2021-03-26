# 接口自动化测试框架组成模块
    关键字驱动测试测试框架
### common 二次封装基础工具类库
### local_config 存放框架配置信息
### test_case 存放可执行的接口测试用例
### test_case_data 存放接口测试用例的数据
### runner 测试用例整体运行模块
### log_report 运行日志及测试报告途径

# 接口自动化测试框架使用工具
1. request：发送请求
2. configparser：配置文件读取
3. xlrd/xlwt/xutils：excel操作
4. ast/json：数据格式处理
5. unittest/pytest：单元测试框架
6. paramunittest：数据驱动
7. HTMLTestReportCN：测试报表
8. smtplib/email：格式/收发邮件
9. pymysql：数据库读取
10. logging：日志记录

# 接口自动化核心业务实现
1. 用例数据转换
2. 数据驱动实现
3. 断言库实现
4. 数据依赖实现
5. 测试结果保存：报表输出/写入excel

# 切换实现
1. pytest 替换 unittest
2. excel 替换 mysql
