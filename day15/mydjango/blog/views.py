from django.shortcuts import render,HttpResponse,redirect
import time
# Create your views here.
def index(request):
    return HttpResponse('bolg_index')

# request：请求对象      HttpResponse:响应信息对象
def login(request):
    if request.method=='POST':
        APPEND_SLASH = False
        #关键字根据html中form表单里input框中的name
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        if username=='liuhao' and password=='123':
            # 返回一个字符串信息。
            # return HttpResponse('登录成功')
            return redirect('/book/')
        #返回一个页面render
    return render(request,'bootstrap_login.html')

def book(request):
    #查找到书籍库中全部数据
    book_list=NewBook.objects.all()
    return render(request,'book.html',locals())


from blog.models import *
import urllib.parse
def addbook(request):
    if request.method=='POST':
        title=urllib.parse.unquote(request.POST.get('title',None))
        author=urllib.parse.unquote(request.POST.get('author',None))
        price=urllib.parse.unquote(request.POST.get('price',None))
        pub_data=urllib.parse.unquote(request.POST.get('pub_data',None))
        if title and author and price and pub_data:
            if time.mktime(time.strptime(pub_data ,'%Y-%m-%d'))   < time.time():
                print(pub_data,title,author,price)
                NewBook.objects.create(title=title,author=author,price=price,pub_data=pub_data)
                return redirect('/book/')
    return render(request,'addbook.html')
def delbook(request):
    nid=request.GET.get('id')
    # 找到ID等于页面传过来的id的书籍，删除
    NewBook.objects.filter(id=nid).delete()
    return redirect('/book/')
def editbook(request):
    if request.method == 'POST':
        title = urllib.parse.unquote(request.POST.get('title', None))
        author = urllib.parse.unquote(request.POST.get('author', None))
        price = urllib.parse.unquote(request.POST.get('price', None))
        pub_data = urllib.parse.unquote(request.POST.get('pub_data', None))
        nid = urllib.parse.unquote(request.POST.get('id', None))
        if title and author and price and pub_data:
            try:
                if time.mktime(time.strptime(pub_data ,'%Y-%m-%d')) < time.time():  #出版时间不能大于当前时间
                    NewBook.objects.filter(id=nid).update(title=title,author=author,price=price,pub_data=pub_data)
                    return redirect('/book/')
            except Exception as e :
                return redirect('/editbook/?id=%s'%nid)
    nid=request.GET.get('id')
    #
    book_obj=NewBook.objects.filter(id=nid).all()[0]
    return render(request,'editbook.html',locals())
