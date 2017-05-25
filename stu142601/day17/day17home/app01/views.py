from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
# Create your views here.
def session(func):
    def wrap(request, *args, **kwargs):
        # 如果未登陆，跳转到指定页面
        user = request.session.get('user')
        if not user:
            return redirect('/login')
        return func(request, user, *args, **kwargs)

    return wrap

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        huser=request.POST.get('user')
        hpwd=request.POST.get('pwd')
        obj=models.Userinfo.objects.filter(name=huser,password=hpwd).first()
        res = {'status': True, 'error': None}
        if obj:
            #登录成功，返回正确的字典
            obj=HttpResponse(json.dumps(res))
            #加入session用户认证
            request.session['user']=huser
            request.session['pwd']=hpwd
            return obj
        else:
            res['status']=False
            res['error']='用户名或密码错误'
            #登录失败，页面显示错误信息
            return HttpResponse(json.dumps(res))
@session
def home(request,user=None):
        hosts=models.Host.objects.all()
        return render(request,'home.html',{'yonghu':user,'hosts':hosts})
@session
def user_host(request,user=None):

    user_obj=models.Userinfo.objects.filter(name=user).first()
    user_host=user_obj.m.all()
    return render(request,'user_host.html',{'yonghu':user,'hosts':user_host})
@session
def firm(request,user=None):
    if request.method=='GET':
        firms=models.Firm.objects.all()
        return render(request,'firm.html',{'yonghu':user,'firms':firms})
    elif request.method=='POST':
        new_id=request.POST.get('new_id')
        new_name=request.POST.get('new_name')
        old_id = request.POST.get('old_id')
        id_list=[]
        res = {'status': True, 'error': None}
        firm_objs=models.Firm.objects.all()
        for firm_obj in firm_objs:
            id_list.append(firm_obj.id)

        if old_id ==new_id :
            models.Firm.objects.filter(id=old_id).update(id=int(new_id),firm_nam=new_name)
            obj = HttpResponse(json.dumps(res))
            return obj
        elif  int(new_id) not in id_list :
            #将firm更新-firm表和host表(外键)
            models.Firm.objects.filter(id=old_id).update(id=int(new_id),firm_nam=new_name)
            models.Host.objects.filter(firm_id=old_id).update(firm_id=int(new_id))
            obj = HttpResponse(json.dumps(res))
            return obj
        else:
            res['status']=False
            res['error']='修改id重复-请重新分配'
            return HttpResponse(json.dumps(res))