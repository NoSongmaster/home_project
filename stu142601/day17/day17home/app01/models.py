from django.db import models

class Host(models.Model):
    #主机IP
    ip=models.CharField(max_length=32,unique=True)
    #主机端口
    port=models.IntegerField()
    #主机业务线(外键---)
    firm=models.ForeignKey(to='Firm',to_field='id')

class Firm(models.Model):
    #业务线名称
    firm_nam=models.CharField(max_length=32,unique=True)

class Userinfo(models.Model):
    #用户信息表
    name=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    age=models.IntegerField()
    #多对多关系表
    m=models.ManyToManyField('Host')

