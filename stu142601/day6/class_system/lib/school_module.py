#liuhao
import pickle,os,sys,shelve
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
school_database=BASE_DIR+r'/database/school_database'

class School(object):
    def __init__(self):
        self.school_dict={}
        self.school_dict["teacher"]={}
        self.school_dict["course"]={}
        self.school_dict["grade"]={}
        self.school_dict["student"]={}
    def add(self,school_name,school_addr):
        self.school_dict.update({school_name:{'school_name':school_name,'school_addr':school_addr}})
    def get(self):
       # print(self.school_dict)
        return self.school_dict
    def show(self,school_name): #需要传入学校的名字来作为字典的key
        return self.school_dict[school_name]["school_name"]
    def add_teacher(self,teacher_name,teacher_obj):
        self.school_dict["teacher"].update({teacher_name:teacher_obj})
    def add_course(self,course_name,course_obj):
        self.school_dict["course"].update({course_name:course_obj})
    def show_teacher(self,school_name,teacher_name):
        print("这里是%s",school_name)
        self.school_dict[school_name][teacher_name].show(school_name,teacher_name)
    def add_grade(self,grade_id,grade_obj):
        self.school_dict["grade"].update({grade_id:grade_obj})

    # def add_course(self,course,money,cycle):3333
    #     print("新增课程:%s , 学费: %s ,教学周期 : %s "%(course,money,cycle))

# school_data=shelve.open(school_database)
# print(school_data.get("北京大学")["北京大学"].get())


