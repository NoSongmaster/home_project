#liuhao
'''实现功能，雇佣老师，创建课程，查看老师信息，查看课程信息'''
import os,shelve,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
teacher_file=BASE_DIR+r'/database/teacher_database'
school_file=BASE_DIR+r'/database/school_database'
course_file=BASE_DIR+r'/database/course_database'
grade_file=BASE_DIR+r'/database/grade_database'
student_file=BASE_DIR+r'/database/student_database'
print(BASE_DIR)
from lib import teacher_module
from lib import school_module
from lib import course_module
from lib import grade_module
from lib import student_module
def teacher_view():
    while True:
        print('''
        欢迎进入教师视图
        1、查看老师信息
        2、查看班级情况
        ''')
        while True:
            choice=input("请选择：").strip()
            if len(choice)==0:continue
            else:break
        if choice=='1':
            while True:
                name=input("请输入查看的老师:")
                if len(name)==0:continue
                else:break
            teacher_database = shelve.open(teacher_file)
            if len(teacher_database) == 0: print("没有任何老师")
            #teacher_database.get(name)[name].get(name)
            teacher_database.get(name)[name].show(name)
        elif choice=='2':
            while True:
                name=input('请输入班级名称')
                if len(name) == 0:
                    continue
                else:
                    break
            grade_database= shelve.open(grade_file)
            if len(grade_database) ==0:print('没有班级存在')
            grade_database.get(name)[name].show(name)
        elif choice=='q':break

def school_ini():
        school_name1="北京大学"
        school_addr1="北京市"
        school_name2="上海大学"
        school_addr2="上海市"
        a=school_module.School()
        a.add(school_name1,school_addr1)
        b=school_module.School()
        b.add(school_name2,school_addr2)
        school_data=shelve.open(school_file)
        school_data[school_name1]={school_name1:a}
        school_data[school_name2]={school_name2:b}
        school_data.close()

def school_view():
    while True:
        print('''
        选择学校：
        1、北京大学
        2、上海大学
        ''')
        choice=input("请选择:")
        if choice == '1':
            choice=('北京大学')      #后面方便判断选择的学校
            school_data=shelve.open(school_file)
            school=school_data.get(choice)[choice]  #这里获取到的是实例北京大学的内存地址
            print(school)
            school_data.close()
        elif  choice == '2':
            choice='上海大学'
            school_data=shelve.open(school_file)
            school=school_data.get(choice)[choice]  #这里获取到的是实例化上海大学的内存地址
            print(school)
            school_data.close()
        elif choice=='q':break
        else:continue
        while True:
            print('''
            欢迎进入学校视图
            1、创建雇佣新老师
            2、创建课程
            3、创建班级
            4、查看老师信息
            5、查看课程信息
            6、查看班级信息
            ''')
            while True:
                choice1=input('请输入>>: ').strip()
                if len(choice1)==0 :
                    continue
                else:
                    break
            if choice1 == '1':
             #  print(school)
                print(choice)
                name=input('请输入老师的名字：')
                age=input('请输入老师的年龄：')
                sex=input('请输入老师的性别：')
                course=input("请输入老师课程：")

                # school=input("请输入老师所属的学校")
                #存储老师信息
                teacher_database=shelve.open(teacher_file)
                #实例化老师对象，存储到老师文件中
                if name in teacher_database:

                    choice2=input('''%s老师已经存在请重新添加
                       1、继续修改
                       2、放弃退出
                   '''%name)
                    if len(choice2) ==0:
                        continue
                    if choice2 == '1':
                        print("正在修改.......")
                    elif choice2 == '2':
                        continue
                    else:
                        break
                else:
                    print("创建一个实例保存老师信息")
                a=teacher_module.Teacher()
                #name,age,sex,course,school
                a.add(name,age,sex,course,choice)
                teacher_database[name]={ name:a}
                teacher_database.close()
                #将老师的信息存到学校中
                school_data=shelve.open(school_file)
                b =school_data.get(choice)[choice]
                b.add_teacher(name,a) #调用学校中添加老师方法——加入信息
                school_data[choice]={choice:b}    #重新将实例进行保存
                school_data.close()
               # print(school_data.get(choice)[choice].get())
                print("添加老师%s完成"%name)
            if choice1=='2':
                course_name=input("请输入创建课程名：")
                course_mouth=input("请输入课程周期：")
                course_money=input("请输入课程学费：")
                course_data=shelve.open(course_file)
                if course_name in course_data:
                    choice2 = input('''%s课程已经存在请重新添加
                                          1、继续修改
                                          2、放弃退出
                                      ''' % course_name)
                    if len(choice2) == 0:
                        continue
                    if choice2 == '1':
                        print("正在修改.......")
                    elif choice2 == '2':
                        continue
                    else:
                        break
                else:
                    print("创建一个实例进行保存课程信息")
                #实例化一个课程，保存对象。
                a=course_module.Course()
                a.add(course_name,course_mouth,course_money)
                #存储模式：teacher_database['python']={'python':'课程的内存地址'}
                course_data[course_name]={course_name:a}
                course_data.close()
                #将课程信息，保存到学校中。
                school_data = shelve.open(school_file)
                b = school_data.get(choice)[choice]
                b.add_course(course_name,a)
                school_data[choice]={choice:b}
                school_data.close()
                print("添加%s课程完成："%course_name)
            if choice1== '3':
                while True:
                    flag=0
                    grade_id=input("请输入班级ID：")
                    grade_data = shelve.open(grade_file)
                    if grade_id not in grade_data:  #ID不存在
                        grade_teachername=input("请输入老师：")
                        teacher_data=shelve.open(teacher_file)
                        if grade_teachername in teacher_data:       #存在可以关联的老师
                            grade_course=input("请输入课程名字：")
                            if grade_course == teacher_data.get(grade_teachername)[grade_teachername].teacher_dict[grade_teachername]['course']:   #确认老师教授的课程可班级课程是否相等。
                                flag=1          #全部符合，进行添加
                                print("开始添加班级------")
                            else:
                                print("%s教授的课程为%s,请确认后重新输入。"%(grade_teachername,teacher_data.get(grade_teachername)[grade_teachername].teacher_dict[grade_teachername]['course']))
                        else:
                            print("输入的老师不存在，请确认后，重新输入：")
                    else:
                        print("ID已存在，请重新输入：")
                        break
                    if flag == 1:   #添加班级信息，
                        a=grade_module.Grade()
                        a.add(grade_id,teacher_data[grade_teachername][grade_teachername],\
                              teacher_data.get(grade_teachername)[grade_teachername].teacher_dict[grade_teachername]['course'],grade_teachername)
                        grade_data[grade_id]={grade_id:a}
                        grade_data.close()
                        teacher_data.close()
                        print("添加完成")
                        #保存到学校实例中
                        school_data=shelve.open(school_file)
                        b=school_data.get(choice)[choice]
                        b.add_grade(grade_id,a)
                        school_data[choice] = {choice: b}
                        school_data.close()
                        break


            if choice1=='4':
                teacher_name=input("请输入老师的名字")
                teacher_data=shelve.open(teacher_file)
                if teacher_name in teacher_data:
                # print(school_database[choice].get()[teacher_name])
                #t通过传入老师和学校的名字。输出老师的信息。
                    teacher_data.get(teacher_name)[teacher_name].show(teacher_name)
                    teacher_data.close()
                else: print("老师'%s'不存在"%teacher_name)
            if choice1=='5':
                course_name=input("请输入查询课程的名字:")
                course_data=shelve.open(course_file)
                if course_name in course_data:
                    course_data.get(course_name)[course_name].show(course_name)
                    course_data.close()
                else:print("课程'%s'不存在"%course_name)
            if choice1=='6':
                grade_id=input("请输入班级ID:")
                grade_data=shelve.open(grade_file)
                if grade_id in grade_data:
                    grade_data.get(grade_id)[grade_id].show(grade_id)
                    grade_data.close()
                else:print("ID为'%s'的班级不存在"%grade_id)
            if choice1=='q':break
def student_view():

    while True:
        school_data=shelve.open(school_file)
        for i in school_data:
           print(school_data.get(i)[i].show(i))
        school_name=input('选择学校： ')
        if school_name in school_data:
            break
        else:
            print('输入有误，请重新输入！')
            continue
        school_data.close
    while True:
        course=False
        grade=False
        course_list=[]
        grade_list=[]
        print(school_name)
        print('''
        欢迎进入学生视图
        1.注册
        2.查看学生信息
        ''')
        choice=input('''>>:''')
        if choice =='1':#name,age,sex,course,grade,school
            name=input('输入学生姓名：')
            age=input('输入学生年龄：')
            sex=input('输入学生性别：')

            school_database = shelve.open(school_file)
            print('可以关联以下课程:')
            for i in school_database.get(school_name)[school_name].school_dict["course"]:
                print(i)
                course_list.append(i)
            course_re=input('输入关联的课程')
            if course_re in course_list:
                course=course_re
            else:
                print('输入有误')
                continue
            print('可以关联以下班级')
            for i in school_database.get(school_name)[school_name].school_dict["grade"]:
                print(i)
                grade_list.append(i)
            grade_re=input('输入关联的班级')
            if grade_re in grade_list:
                grade=grade_re
            else:
                print('输入有误')
                continue
                #school_data[choice]={choice:b}
            student_obj=student_module.Student()
            student_obj.add(name,age,sex,course,grade,school_name)
            student_database=shelve.open(student_file)
            student_database[name]={name:student_obj}
            grade_database = shelve.open(grade_file)
            grade_obj=grade_database.get(grade)[grade]
            grade_obj.add_student(name)
            school_database.get(school_name)[school_name].school_dict["grade"][grade]=grade_obj
            #grade_data[grade_id]={grade_id:a}
            grade_database[grade]={grade:grade_obj}
            student_database.close()
            grade_database.close()
            school_database.close()
        elif choice == '2':
            name= input('输入学生姓名:')
            student_database=shelve.open(student_file)
            student_database.get(name)[name].show(name)
        elif choice =='q':
            break


def run():
    while True:
        view=input('''
                1.管理视图
                2.老师视图
                3.学生视图
                4.初始化学校

                >>:''')
        if view =='1':
            school_view()
        elif view=='2':
            teacher_view()
        elif view=='3':
            student_view()
        elif view=='4':
            school_ini()
        elif view=='q':
            print('退出选课系统')
            break
run()
#teacher_view()
#school_ini()

#查看大学信息
# school_data=shelve.open(school_file)
# print(school_data.get("北京大学")["北京大学"].get())

