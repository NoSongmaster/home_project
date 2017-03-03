import os,shelve,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
student_file=BASE_DIR+r'/database/student_database'

class Student(object):
    def __init__(self):
       self.student_dict={}
    def add(self,name,age,sex,course,grade,school):
        self.name=name
        self.student_dict.update( {name:{'name':name,'age':age,'sex':sex,'course':course,'grade':grade,'school':school}})
        self.school_name=school
    def get(self):
       # print(self.teacher_dict[name])
        return self.student_dict
    def show(self,name):    #需要传入老师和学校的名字。来作为字典的key
        print(self.school_name)
        print('''
        --------teacher info:{name}---------------
                name:{name}
                age:{age}
                sex:{sex}
                course:{course}
                grade:{grade}
                school:{school}
        '''.format(name=self.student_dict[name]['name'],age=self.student_dict[name]['age'],sex=self.student_dict[name]['sex'],\
                   course=self.student_dict[name]['course'],grade=self.student_dict[name]['grade'],school=self.school_name))