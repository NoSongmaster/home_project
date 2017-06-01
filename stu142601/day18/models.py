from django.db import models

class Userinfo(models.Model):
    #用户信息表
    name=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    age=models.IntegerField()
class Article(models.Model):
    #文章标题
    article_title=models.CharField(max_length=32,unique=True)
    #文章内容
    article_content=models.CharField(max_length=2000,)
    #文章评论   这里应该与下面的评论一对多
    article_comment=models.ManyToManyField('Comment')
    #文章作者:
    article_auther=models.ForeignKey('Userinfo')
class Comment(models.Model):
	#评论者
    comment_user=models.ForeignKey('Userinfo')
    #评论文章
	comment_article=models.ForeignKey('Article')
    #评论内容
	comment_content=models.CharField(max_length=500)

