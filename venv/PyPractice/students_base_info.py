#需求：把excel中的学生信息转换成列表对象的方式==统计excel中的人数
'''
思路： 对象 == 类
'''
class StudentsBaseInfo:
    def __init__(self,stu_id,stu_name,stu_sex,stu_age,stu_score):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_sex = stu_sex
        self.stu_age = stu_age
        self.stu_score = stu_score
    def show(self):
        pass
