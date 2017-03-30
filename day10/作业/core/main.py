#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
from concurrent.futures import ThreadPoolExecutor
import paramiko,pymysql
from conf.setting import *
from io import StringIO
import time
import threading



# print(config['host'])
class myconn(object):
    def __init__(self):
        self.user_id=False
        self.all_host=False
        self.pool = ThreadPoolExecutor(5)
        # conn = pymysql.connect(host='172.16.50.192', port=3306, user='root', passwd='123456', db='db')
        self.conn=pymysql.connect(host=config['host'],port=int(config['port']),user=config['user'],passwd=config['passwd'],db=config['db'])
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def auth(self):
        self.username = input('请输入用户名：')
        pwd = input('请输入密码：')
        # cursor.execute 执行SQL，并返回受影响行数
        effect_row = self.cursor.execute("select * from userinfo where name=%s and password = %s", (self.username, pwd,))
        if effect_row >0:

        # 提交，不然无法保存新建或者修改的数据
            self.conn.commit()
        # 获取返回信息
            ret = self.cursor.fetchall()
            self.user_id=ret[0]['user_id']
            print(ret)
        # 关闭游标
        # self.cursor.close()
        return self.user_id

    def show_host(self):
        if self.user_id:
            row=self.cursor.execute("select host_id,ip,port,username,pwd_type from user_to_host left join host on user_to_host.host_to_id = host.host_id where user_to_id =%s",(int(self.user_id)))
            if row >0:
                self.all_host=self.cursor.fetchall()
                print('用户:%s 可以管理下列主机:'%self.username)

                for line in self.all_host:
                    print('''
               ID:{host_id}
               IP:{ip}
               Port:{port}
               pwd_type:{pwd_type}
               '''.format(host_id=line['host_id'],ip=line['ip'],port=line['port'],pwd_type=line['pwd_type']))
            else:
                print('用户:%s没有可以管理的主机,请联系管理员！')

            print('\t共计%s台机器'%len(self.all_host))

    def main(self):
        self.user_id=self.auth()
        if self.user_id:
            self.show_host()
            self.command()
    # def show_res(self,res):
        # result=res.result()
        # if result:
            # print('\033[32;1m%s\033[0m' % result.decode())
        # self.ssh.close()

    def excute(self,data):
        time.sleep(2)
        cmd_str, id_num=data[0],data[1]
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select ip,port,username,pwd_type,password from host where host_id=%s", (int(id_num)))
        host_data = cursor.fetchall()
        print(host_data)
        # print('正在执行：',id_num)
        for host in host_data:

            ssh = paramiko.SSHClient()
            if host['pwd_type'] == 'pwd':
                # print('使用密码')
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=host['ip'], port=int(host['port']), username=host['username'],
                                 password=host['password'])
                stdin, stdout, stderr = ssh.exec_command(cmd_str)
                result = stdout.read()
                ssh.close()
            elif host['pwd_type']=='private_key':
                # print('使用私钥')
                private_key = paramiko.RSAKey(file_obj=StringIO(host['password']))
                transport = paramiko.Transport((host['ip'], int(host['port'])))
                transport.connect(username=host['username'], pkey=private_key)
                ssh._transport = transport
                stdin, stdout, stderr = ssh.exec_command(cmd_str)
                result = stdout.read()
                ssh.close()
            print('\n\033[34;1m主机:%s 执行结果：\033[0m' % host['ip'])
            if result:
                print('\033[32;1m%s\033[0m' % result.decode())

            # return result


    def command(self):
        while True:
            id_str=input('请输入想要操作的主机id,[批量操作,分割]').strip(',')
            if not id_str:continue
            id_list=id_str.split(',')
            print(self.all_host)
            for id_tt in id_list:

                flag = 0
                # if not isinstance(id, int):exit()
                for host in self.all_host:
                    try:

                        if int(id_tt) == host['host_id']:
                            flag+=1
                    except ValueError as e:pass
                if flag==0:
                    print('\033[31;1m ID 错误:%s\033[0m'%id)
                    break
            if flag!=0:
                cmd_str=input('请输入要操作的命令')

                for id_num in id_list:
                    print('开始执行:',id_num)
                    self.pool.submit(self.excute,(cmd_str,id_num))
                    # print('\033[32;1m%s\033[0m' % fu.result().decode())


def run():
    a=myconn()
    a.main()
