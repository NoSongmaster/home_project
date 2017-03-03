#liuhao
class Course(object):
    def __init__(self):
        self.course_dict={}
    def add(self,course_name,course_mouth,course_money):
        self.course_dict.update({course_name:{"course_name":course_name,'course_mouth':course_mouth,'course_money':course_money}})
    def get(self,course_name):
        return self.course_dict[course_name]
    def show(self,course_name):
        print('''
        ---------课程信息：{course_name}--------
        课程名称：{course_name}
        课程周期：{course_mouth}
        课程学费：{course_money}
        '''.format(course_name=self.course_dict[course_name]["course_name"],course_mouth=self.course_dict[course_name]["course_mouth"],course_money=self.course_dict[course_name]["course_money"] ))



