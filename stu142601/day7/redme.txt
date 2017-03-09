作业功能:
用户加密认证  (用户验证时通过md5加密认证)
允许同时多用户登录
每个用户有自己的家目录 ，且只能访问自己的家目录
允许用户在ftp server上随意切换目录，限制在家目录下
允许用户查看当前目录下文件
允许上传和下载文件，保证文件一致性
文件传输过程中显示进度条
FTPserver:
    FTP_manager.py              FTP用户管理程序:添加ftp用户
    FTP_server.py               FTPserver 主程序
    user_file/[users]/          用户目录,用户上传下载查看的目录(用户家目录)
    users/[users]               用户信息文件
FTPclient:
    FTP_client.py               FTPclient 主程序
    

测试使用账户:
用户名:liuhao      密码:123456
用户名:alex        密码:123456

enter ftp server_IP port:   127.0.0.1 8080
enter your name:liuhao
enter your passwd:123456
验证通过
enter your action: get red_spider_v721718.zip
完成进度 >:[################################################################################################### ]100%
MD5一致性验证：通过
enter your action: put E:\s15.mp4
完成进度 >:[############################################################################                        ]76%

可以执行的命令: ['cd','ls','mkdir','pwd','dir',]
mkdir,ls,ls -l 只能linux上可以使用


范例


    enter your action: cd dir2
    enter your action: pwd
E:\python s16作业\day7\ftp作业\FTPserver/user_file/liuhao/dir2
    enter your action: dir
dir
 驱动器 E 中的卷是 学习
 卷的序列号是 7895-3167

 E:\python s16作业\day7\ftp作业\FTPserver\user_file\liuhao\dir2 的目录

2017/03/09  18:36    <DIR>          .
2017/03/09  18:36    <DIR>          ..
2017/03/09  18:36                 0 in the dir2.txt
               1 个文件              0 字节
               2 个目录 70,464,782,336 可用字节





