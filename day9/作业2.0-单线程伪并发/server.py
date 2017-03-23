#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import socket,select,struct,json,os
sk1 = socket.socket()
sk1.bind(('127.0.0.1',8001,))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1',8002,))
sk2.listen(5)
inputs = [sk1,sk2,]
w_inputs = []
obj_dict={}
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
    print(len(head_bytes))
    obj.send(struct.pack('i', len(head_bytes)))
    obj.send(head_bytes)
while True:
    #实现读写 分离, 将读取和写入的操作都分开
    r,w,e = select.select(inputs,w_inputs,inputs,0.05)  #(inputs=读取,w_inputs=写入,inputs=异常)
    for obj in r:
        if obj in [sk1,sk2]:
            # 新连接捡来了...
            print('新连接来了:',obj)
            conn,addr = obj.accept()
            inputs.append(conn)
        else:
            try:
            # 有连接用户发送消息来了..
            # print('有用户发送数据了:',obj)
                if not obj_dict.get(obj):

                    head_dict=recv_head(obj)
                    if head_dict['cmd'] == 'msg':
                        client_msg=obj.recv(1024)
                        obj.send('收到客户端消息;回复确认'.encode('utf-8'))
                        continue
                    obj_dict[obj]=head_dict
                else:
                    # print(obj_dict[obj]['file_name'])
                    data = obj.recv(20480)
                    with open(obj_dict[obj]['file_name'],'ab') as f:
                        f.write(data)
                    if os.path.exists(obj_dict[obj]['file_name']):
                        if os.path.getsize(obj_dict[obj]['file_name']) == obj_dict[obj]['file_size']:
                            obj_dict.pop(obj)
            except Exception as ex:     #当客户端端口连接,默认会发送数据-----服务端会报错
                print('连接关闭',obj)
                obj.close()
                inputs.remove(obj)




            # try:
            #
            #     data = obj.recv(1024)
            # except Exception as ex:     #当客户端端口连接,默认会发送数据-----服务端会报错
            #     data = ""
            # if data:    #如果data 有数据 : 将 这个实例加入的写操作中
            #     w_inputs.append(obj)
            #     # obj.sendall(data)
            #     print('有数据:',w_inputs)
            # else:   #如果发来的没有数据
            #     obj.close() #关闭这个实例
            #     print('没有数据',inputs)
            #     inputs.remove(obj)  #将inputs中的实例移除
            #     print('没有数据w:',w_inputs)

    # for obj in w:
    #     print(11111111111)
    #     obj.sendall(b'ok')
    #     w_inputs.remove(obj)        #将w_inputs中的实例移除

