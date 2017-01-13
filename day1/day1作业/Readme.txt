本次作业：用户登录
要求：
1、验证用户、密码
2、三次验证失败，锁定
3、博客
博客地址：http://www.cnblogs.com/NoSong/p/6265133.html
昵称：saynobody

程序文件：
.
├── login
│	├── __init__.py
│   ├── login.py
│   ├── user_admin.py
│   ├── users_database.bak
│   ├── users_database.dat
│   └── users_database.dir
├── Readme.txt
└── python_day1_用户登录流程图.png

程序实现：
两个模块
1、用户登录验证模块	login.py
2、用户管理模块 user_admin.py

用户登录验证模块;
1、用户登录，验证用户名和密码
2、验证失败三次，会自动锁定用户

用户管理模块：
1、实现添加用户
2、解锁已经锁定的用户

输入密码，不在屏幕上显示，pycharm运行有问题，先注释了~ 在linux环境和windows CMD下可以正常运行

使用模块shelve
保存用户信息和锁定信息。
生成文件
users_database.bak
users_database.dat
users_database.dir

已经存在用户有：
admin\123456
liuhao\123
alex\666	#已锁定



