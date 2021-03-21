class StudentInfo:
    def __init__(self, stu_number, stu_name, stu_sex, stu_age, stu_score):
        self.stu_number = stu_number
        self.stu_name = stu_name
        self.stu_sex = stu_sex
        self.stu_age = stu_age
        self.stu_score = stu_score
    def student_info(self):
        stu_info = [self.stu_number, self.stu_name, self.stu_sex, self.stu_age, self.stu_score]