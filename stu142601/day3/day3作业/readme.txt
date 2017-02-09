博客地址：http://www.cnblogs.com/NoSong/p/6365805.html
作业：
需要对员工信息文件，实现增删改查操作
主程序文件：main.py
模拟数据库文件:staff_database\user_database
原始文件：bak
函数介绍：
本次作业一共写了11个函数，
check_contain_chinese：负责检查字符是不是中文，用于美化数据输出。
output_head：负责输出select头部，美化输出
output_body: 负责输出select数据，美化输出
output_tail: 负责输出各个函数结尾，输出统计条数。美化输出
show_user_list：读取数据库文件内容，形成列表方便函数调用数据，
返回格式：[{'staff_id': None, 'name': None, 'age': None, 'phone': None, 'dept': None, 'enroll_date': None},{2},{3},{...}]
check：负责进行运算符判断：<、>、=、like。
add_user_list：用于添加数据，判断加入数据中手机号是否存在，存在提示添加失败。存入到数据库文件中
select_search：用于查询数据。
delete：用于删除数据，存入数据库文件中
modify：用于修改数据，存入数据库文件
main:   程序主体。调用增删改查函数。

实现功能：
可以对文件进行增删改差，条件运算<>=like全部实现。
add_user_list() 判断加入数据中手机号是否存在。phone为唯一建
delete删除时，和添加数据时：staff_id 为自增id
modify()函数不允许修改staff_id 和 phone
可以对多个数据库文件进行操作


范例：
             select * from user_database
             select staff_id,name,age from user_database where dept like '实习'
             insert into user_database value(alex,33,11111,teacher,2017-1-1)
             delete from user_database where staff_id > '10'
             update user_database set age = 100 where age = 77


