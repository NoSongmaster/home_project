#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

import pika
import json
import sys
import subprocess
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.102'))
channel = connection.channel()
channel.exchange_declare(exchange='saltstack',type='direct')
channel.queue_declare(queue='salt')
channel.queue_bind(exchange='saltstack',queue='salt',routing_key="1")

def callback(ch, method, properties, body):
    cmd_dict=json.loads(body.decode())
    print(cmd_dict)
    cmd=cmd_dict['cmd']

    callback_queue_name=cmd_dict['queuename']
    res = subprocess.Popen(cmd,  # 通过subprocess获取命令的执行结果
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    err = res.stderr.read()  # 获取错误信息
    if err:  # 如果错误信息存在
        back_msg = err  # 返回信息为错误信息
    else:
        back_msg = res.stdout.read()  # 否则返回信息为标准输出
    # print(back_msg.decode('gbk'))       #需要根据不同的系统修改
    #有agent发送执行完成后的结果
    back_msg_dict={'msg':back_msg.decode('utf-8')}
    print(back_msg_dict['msg'])
    channel.basic_publish(
        exchange="",
        routing_key=callback_queue_name,  # 消息队列的名称
        body=json.dumps(back_msg_dict) #需要根据不同的系统修改
    )

channel.basic_consume(callback,queue="salt") #接收到数据
channel.start_consuming()           #开始执行agent消费

