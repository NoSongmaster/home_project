数据库目录中包含有,数据库的结构和数据
作业/bin/run.py   程序入口文件
作业/core/main    主程序
作业/conf/setting.py 配置文件
rabbitmq_agent   :agent_rabbit2.py agent_rabbit1.py 

实现功能:
            - 用户登录 （用户表中做验证，id）
                通过连接数据库查询user表，实现用户登录验证
            - 显示当前用户管理的所有主机列表（）
                通过输入主机id进行批量管理主机,
            
            - 选中一批机器远程执行命令：
                通过线程池批量执行命令：
                根据host表中pwd_type类型区分验证方式：用户名密码验证 和 用户名私钥验证
    新增功能:
            - 选中主机后:
                输入salt          #适用于linux机器
                    使用rabbtmq=RPC方式远程执行命令--
                    -输入要执行的命令-  
                    -并获取结果-返回-
                    