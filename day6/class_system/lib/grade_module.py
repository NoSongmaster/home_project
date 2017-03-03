#liuhao
class Grade(object):
    def __init__(self):
        self.grade_dict={}
    def add(self,id,teacher,course,grade_teachername):
        '''创建一个班级'''
        self.grade_dict.update({id:{"id":id,"teacher":teacher,"course":course,"student":{}}})
        self.teachername=grade_teachername      #传入实例teacher时，实例字典key就是teachername。在这里保存一份
        self.student=[]
    def get(self,id):
        self.grade_dict[id]
    def show(self,id):
        print('''
        -------grade info of {id}:{course}
        课程id:{id}
        老师:{teacher}
        课程名字:{course}
        学生:{student}
        '''.format(id=self.grade_dict[id]['id'],teacher=self.grade_dict[id]["teacher"].teacher_dict[self.teachername]['name'],\
                   course=self.grade_dict[id]["course"],student=self.student))
    def add_student(self,student_name):
        self.student.append(student_name)
# g1=Grade()
# g1.add(1,"oldboy","linux")
# g1.add_student(1,"郭上")
# g1.show(1)
# print(g1)





