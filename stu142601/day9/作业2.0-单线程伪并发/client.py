#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import struct,json
import socket,os
client = socket.socket()
client.connect(('127.0.0.1',8001))
#接收数据报头
def recv_head(obj):
    data = obj.recv(4)
    head_len = struct.unpack('i', data)[0]
    head_bytes = obj.recv(head_len)
    head_json = head_bytes.decode('utf-8')
    head_dict = json.loads(head_json)
    print('接收:', head_dict)
    return head_dict
#发送数据报头
def send_head(obj, head_dict):
    head_json = json.dumps(head_dict)
    head_bytes = head_json.encode('utf-8')
    print('发送:', head_dict)
    obj.send(struct.pack('i', len(head_bytes)))
    obj.send(head_bytes)

while True:
    v = input('>>>')
    if len(v)==0:continue

    if isinstance(v,str):
        if v.startswith('put '):
            put_list=v.split(' ')
            if len(put_list) ==2:
                cmd=put_list[0]
                file_path=put_list[1]
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    file_name=os.path.basename(file_path)
                    file_size=os.path.getsize(file_path)
                    head_dict={'cmd':'put',
                               'file_name':file_name,
                               'file_size':file_size,
                               }
                    send_head(client,head_dict)
                    f=open(file_path,'rb')
                    for i in f :
                        client.send(i)
                    f.close()
        else:
            msg_size = len(v.encode('utf-8'))
            msg = v.encode('utf-8')
            head_dict = {
                'cmd': 'msg',
                'msg_size': msg_size
            }
            # print(head_dict)
            send_head(client, head_dict)
            client.send(msg)
            data = client.recv(1024)
            print('来自服务端的回复:', data.decode('utf-8'))

