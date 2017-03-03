#liuhao
import os,shelve,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
teacher_file=BASE_DIR+r'/database/teacher_database'

class Teacher(object):
    def __init__(self):
       self.teacher_dict={}
    def add(self,name,age,sex,course,school):
        self.teacher_dict.update( {name:{'name':name,'age':age,'sex':sex,'course':course,'school':school}})
        self.school_name=school
    def get(self):
       # print(self.teacher_dict[name])
        return self.teacher_dict
    def show(self,name):    #需要传入老师和学校的名字。来作为字典的key
        print(self.school_name)
        print('''
        --------teacher info:{name}---------------
                name:{name}
                age:{age}
                sex:{sex}
                course:{course}
                school:{school}
        '''.format(name=self.teacher_dict[name]['name'],age=self.teacher_dict[name]['age'],sex=self.teacher_dict[name]['sex'],\
                   course=self.teacher_dict[name]['course'],school=self.school_name))


# a=Teacher()
# a.add('alex',22,'f','py','oldboy')
# a.get('alex')
# a.teacher_show('alex')






