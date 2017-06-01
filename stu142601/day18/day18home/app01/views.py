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
from utils import my_page
@session
def home(request,user=None):
    if request.method=='GET':
        if request.GET.get('p'):
            current_page = request.GET.get('p')
        else:
            current_page = 1
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        base_url = request.path
        hosts_count=models.Host.objects.all().count()
        page=my_page.Page(current_page,10,base_url,hosts_count,11)
        # select_related('firm_id') == left.join 前端显示的执行速度快。只需执行一条-之前是10条
        hosts_list=models.Host.objects.all().select_related('firm_id').order_by('-id')[page.start():page.end()]
        return render(request,'home.html',{'hosts_list':hosts_list,'page':page,'yonghu':user})
@session
def user_host(request,user=None):

    user_obj=models.Userinfo.objects.filter(name=user).first()
    user_host=user_obj.m.all()
    return render(request,'user_host.html',{'yonghu':user,'hosts':user_host})
from django import forms
from django.forms import fields
from django.forms import widgets
class FirmForm(forms.Form):
    # {  # <input type="text" class="form-control" id="addfirm_id" name="name"#}
    form_id=fields.IntegerField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '格式错误'},
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'addfirm_id',
                'name': 'name',
                'placeholder':"请输入名称"
            }
        )
    )
    #            <input type="text" class="form-control" id="addfirm_name" name="pwd"#}
    form_nam=fields.CharField(
        required=True,
        error_messages = {'required': '不能为空', 'invalid': '格式错误'},
        widget = widgets.TextInput(
            attrs={
            'class': 'form-control',
            'id':'addfirm_name',
            'name':'pwd',
            'placeholder':"请输入名称"
            }
        ),
    )
    b=3333




@session
def firm(request,user=None):
    if request.method=='GET':
        obj=FirmForm()
        obj2=FirmForm()
        obj2.fields['form_id'].widget.attrs['id']='firm_id'
        obj2.fields['form_nam'].widget.attrs['id']='firm_name'
        firms=models.Firm.objects.all()
        return render(request,'firm.html',{'yonghu':user,'firms':firms,'obj':obj, 'obj2':obj2})
    elif request.method=='POST':
        new_id=request.POST.get('new_id')
        new_name=request.POST.get('new_name')
        old_id = request.POST.get('old_id')
        print(new_id,new_name)
        res = {'status': True, 'error': None}
        if len(new_id)==0 or len(new_name)==0:          #如果输入值为空，返回一个信息，可以放到前端页面进行判断
            res['status'] = False
            res['error'] = '设置值不可以为空'
            return HttpResponse(json.dumps(res))
        id_true=models.Firm.objects.filter(id=new_id).first()   #用来判断新id是否在表中存在
        if old_id ==new_id :                                #id 不变的情况下
            models.Firm.objects.filter(id=old_id).update(id=int(new_id),firm_nam=new_name)
            obj = HttpResponse(json.dumps(res))
            return obj
        elif  not id_true:  #如果新ID在表中不存在
            #将firm更新-firm表和host表(外键)
            models.Firm.objects.filter(id=old_id).update(id=int(new_id),firm_nam=new_name)
            models.Host.objects.filter(firm_id=old_id).update(firm_id=int(new_id))
            obj = HttpResponse(json.dumps(res))
            return obj
        else:
            res['status']=False
            res['error']='修改id重复-请重新分配'
            return HttpResponse(json.dumps(res))

@session
def add_firm(request,user=None):
    if request.method=='GET':
        return HttpResponse('请提交POST请求')
    elif request.method=='POST':

        new_id=request.POST.get('new_id')
        new_name=request.POST.get('new_name')
        res = {'status': True, 'error': None}
        print(new_name,new_id)
        if len(new_id)==0 or len(new_name)==0:  #如果输入值为空，返回一个信息，可以放到前端页面进行判断
            res['status'] = False
            res['error'] = '设置值不可以为空'
            return HttpResponse(json.dumps(res))

        id_true = models.Firm.objects.filter(id=new_id).first()  # 用来判断新id是否在表中存在
        if not id_true: #如果新ID不存在
            models.Firm.objects.create(id=new_id,firm_nam=new_name)
            obj = HttpResponse(json.dumps(res))
            return obj
        else:#新ID存在
            res['status']=False
            res['error']='修改id重复-请重新分配'
            return HttpResponse(json.dumps(res))
@session
def del_firm(request,user=None):
    if request.method=='GET':
        return HttpResponse('请提交POST请求')
    elif request.method=='POST':
        del_id=request.POST.get('del_id')
        res = {'status': True, 'error': None}
        id_true = models.Firm.objects.filter(id=del_id).first()  # 用来判断新id是否在表中存在

        if id_true:
            models.Firm.objects.filter(id=del_id).delete()
            return HttpResponse(json.dumps(res))
        else:
            res['status']=False
            res['error']='id不存在'
            return HttpResponse(json.dumps(res))


from django import forms
from django.forms import fields
from django.forms import widgets
class HostForm(forms.Form):
    ip=fields.GenericIPAddressField(
        required=True,
        error_messages={'required': '不能为空','invalid':'格式错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    port =fields.IntegerField(
        required=True,
        error_messages={'required': '不能为空', 'invalid': '格式错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control'}),
    )
    firm_id=fields.IntegerField(
        required=True,
        error_messages={'required': '不能为空'},
        widget=widgets.Select(attrs={'class': 'form-control'},
        choices=models.Firm.objects.values_list('id','firm_nam'),
    ))
    def __init__(self,*args,**kwargs):
        super(HostForm,self).__init__(*args,**kwargs)
        self.fields['firm_id'].widget.choices=models.Firm.objects.values_list('id','firm_nam')
@session
def create_hosts(request):
    for row in range(1,255):
        ip='192.168.0.%s'%row
        port =22
        firm_id=1
        models.Host.objects.create(ip=ip,port=port,firm_id=firm_id)
    # models.Host.objects.all().delete()
    return HttpResponse('添加成功')
@session
def add_host(request):
    if request.method=='GET':
        obj=HostForm()
        return render(request,'add_host.html',{'obj':obj})
    else:
        obj=HostForm(request.POST)
        if obj.is_valid():
            try:
                models.Host.objects.create(**obj.cleaned_data)
            except Exception as e:
                return HttpResponse('ip不可以重复')
            return redirect('/home')
        else:
            return render(request,'add_host.html',{'obj':obj})
@session
def edit_host(request,uid=1):
    if request.method=='GET':
        print(uid)
        host_info=models.Host.objects.filter(id=uid).first()
        print(host_info)
        obj=HostForm(initial={'ip':host_info.ip,'port':host_info.port,'firm_id':host_info.firm_id})
        return render(request,'edit_host.html',{'uid':uid,'obj':obj})
    else:
        obj=HostForm(request.POST)
        if obj.is_valid():
            models.Host.objects.filter(id=uid).update(**obj.cleaned_data)
            return redirect('/home')
        else:
            return render(request,'edit_host.html',{'obj':obj})