#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import pymysql
import paramiko
from io import StringIO
conn = pymysql.connect(host='172.16.141.42', port=3306, user='root', passwd='123456', db='db')
cursor =conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select ip,port,username,pwd_type,password from user_to_host left join host on user_to_host.host_to_id = host.host_id where user_to_id =%s",(1))
data=cursor.fetchall()
ssh = paramiko.SSHClient()
host=data[1]
# print(host['password'])
private_key = paramiko.RSAKey(file_obj=StringIO(host['password']))
transport = paramiko.Transport((host['ip'], int(host['port'])))
transport.connect(username=host['username'], pkey=private_key)
ssh._transport = transport
stdin, stdout, stderr = ssh.exec_command('df -h')
result = stdout.read()
print(result.decode())
ssh.close()


