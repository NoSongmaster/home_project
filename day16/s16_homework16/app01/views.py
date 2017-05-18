from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
def session(func):
        def wrap(request, *args, **kwargs):
            # 如果未登陆，跳转到指定页面
            user=request.session.get('username')
            if not user:
                return redirect('/login?%s'%user)
            return func(request,user,*args, **kwargs)

        return wrap

#
# user = request.session.get('username')
# if not user:
#     return redirect('/login')

def login(request):
    if request.method=='GET':
        user=request.GET.get('user')
        if user:
            return render(request, 'login.html', {'yonghu',user})
        else:    return render(request,'login.html',{})

    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name and pwd:
            user=models.UserInfo.objects.filter(username=name,pwd=pwd).first()
            if user:

                obj=render(request,'denglu.html',{'yonghu':name})
                request.session['username']=name
                return obj

@session
def qu42(request,user=None):
    # v=request.session.get('username')
    # if not v:
    #     return redirect('/login')
    return render(request,'qu42.html',{'yonghu':user})
@session
def tupian(request,user=None):
    return render(request,'tupian.html',{'yonghu':user})
@session
def duanzi(request,user=None):
    return render(request,'duanzi.html',{'yonghu':user})
@session
def it1024(request,user=None):
    return render(request,'it1024.html',{'yonghu':user})
@session
def niwen(request,user=None):
    return render(request,'niwen.html',{'yonghu':user})


def add(request,user=None):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get("pwd")
        age=request.POST.get('age')
        if name and pwd and age:
            models.UserInfo.objects.create(username=name,pwd=pwd,age=age)
            return render(request,'add.html')

    return redirect('/login')

