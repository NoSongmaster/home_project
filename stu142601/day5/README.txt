作者:LiuHao
博客园：http://www.cnblogs.com/NoSong/
版本:示例版本 v0.2
程序介绍:
    实现ATM常用功能
    课程要求作业已全部完成：
    购物车程序：
        1、实现购物商城，买东西加入 购物车，调用信用卡接口结账
        2、调用支付接口使用 用户认证用装饰器
    atm：
        功能性：
            1、查询账户信息
            2、提供还款接口
            3、可以提现，手续费根据配置文件修改
            4、支持账户间转账
            5、账单：记录日常消费流水
            6、提供购物支付api接口
        其他：
            1、支持多账户登录      
            2、ATM记录操作日志     登录情况和金额操作情况
            3、提供管理接口，包括添加账户，解冻账户
            4、实现用户验证三次后锁定用户。
            
程序入口:
atm/bin/manager     管理程序入口
atm/bin/atm         atm程序入口
shopping_mall/shopping  购物商场入口

目录结构说明：            
ATM/core/    程序文件
db/accounts/ 存储用户信息文件，还有用户账单文件
log/         存储atm操作日志文件

#已创建用户名密码：
账户id:123    密码：123
账户id:1234 密码：1234

#atm中默认b返回上一层

程序结构:
day5-atm/
├── README
├── atm #ATM主程目录
│   ├── __init__.py
│   ├── bin #ATM 执行文件 目录
│   │   ├── __init__.py
│   │   ├── atm.py  #ATM 执行程序
│   │   └── manage.py #ATM 管理端,进行创建信用卡用户，解锁用户
│   ├── conf #配置文件
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core #主要程序逻辑都 在这个目录 里
│   │   ├── __init__.py
│   │   ├── accounts.py  #用于从文件里加载和存储账户数据
│   │   ├── auth.py      #用户认证模块
│   │   ├── db_handler.py   #数据库连接引擎
│   │   ├── logger.py       #日志记录模块
│   │   ├── main.py         #主逻辑交互程序
│   │   ├── transaction.py  #记账\还钱\取钱等所有的与账户金额相关的操作都在这
│   │   └── bill.py         #用于记录用户账单
│   ├── db  #用户数据存储的地方
│   │   ├── __init__.py
│   │   ├── account_sample.py #生成一个初始的账户数据 ,把这个数据 存成一个 以这个账户id为文件名的文件,放在accounts目录 就行了,程序自己去会这里找
│   │   └── accounts #存各个用户的账户数据 ,一个用户一个文件
│   │       └── 1234.json #一个用户账户示例文件
│   │       └── 1234.bill #一个用户的账单信息
│   └── log #日志目录
│       ├── __init__.py
│       ├── access.log #用户访问和操作的相关日志
│       └── transactions.log    #所有的交易日志
└── shopping_mall #电子商城程序,已实现
    └── shopping        #调用信用卡接口结账