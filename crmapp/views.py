# Create your views here.
#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crmapp.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
users = User.objects.all()


class LogForm(forms.Form):
    username = forms.CharField(label=u'账号',error_messages={'required':'请输入帐号'})
    password = forms.CharField(widget = forms.PasswordInput,label=u'密码',error_messages={'required':'请输入密码'})

class UserForm(forms.Form):
    number = forms.CharField(label=u'编号',error_messages={'required':'请输入编号'})
    username = forms.CharField(label=u'账号',error_messages={'required':'请输入帐号'})
    name = forms.CharField(label=u'姓名',error_messages={'required':'请输入名字'})
    password = forms.CharField(widget = forms.PasswordInput,label=u'密码',error_messages={'required':'请输入密码'})
    email = forms.EmailField(label=u'邮箱',error_messages={'required':'请输入邮箱'})
    phonenumber = forms.CharField(label=u'手机号码',error_messages={'required':'请输入手机号码'})
    headImg = forms.FileField(label=u'头像',required=False) 
    identity = forms.CharField(widget=forms.Select(choices=idtype), label=u'身份')
    remarks = forms.CharField(label=u'备注', required=False,widget = forms.Textarea)

class BusyForm(forms.Form):
    number = forms.CharField(label=u'商家编号',error_messages={'required':'请输入编号'})
    name =  forms.CharField(label=u'商家名字',error_messages={'required':'请输入商家名字'})
    shopname = forms.CharField(label=u'门店名字',error_messages={'required':'请输入门店名字'})
    queryset0 = Tag.objects.all()
    tag = forms.ModelChoiceField(queryset=queryset0,empty_label=None,label=u'经营内容',error_messages={'required':'请输入经营内容'})
    district = forms.CharField(label=u'地区',error_messages={'required':'请输入地区信息'})
    address = forms.CharField(label=u'详细地址',error_messages={'required':'请输入详细地址'})
    bmap = forms.BooleanField(label=u'是否有地图',error_messages={'required':'请选择'})
    queryset1 = Maintainer.objects.all()
    condition = forms.CharField(label=u'安装情况',error_messages={'required':'请选择安装状况'}, widget=forms.Select(choices=CONDITION_CHOICES))
    installor = forms.ModelChoiceField(queryset=queryset1,empty_label=None,label=u'安装人员',error_messages={'required':'请选择或添加安装人员'})
    installtime = forms.CharField(label=u'安装时间',error_messages={'required':'请输入安装时间'})
    remarks = forms.CharField(label=u'备注',required=False)

class RoutingForm(forms.Form):
    number = forms.CharField()
    gateway = forms.CharField()
    password = forms.CharField()
    is_main = forms.BooleanField()
    mac = forms.CharField()
    ssid = forms.CharField()
    remarks = forms.CharField()
    queryset = Business.objects.all()
    business = forms.ModelChoiceField(queryset=queryset,empty_label=None)
    
         
class CooperForm(forms.Form):
    number = forms.CharField()
    starttime = forms.DateField()
    endtime = forms.DateField()
    cooperImg = forms.FileField()
    desc = forms.CharField(widget=forms.Textarea)
    queryset = Business.objects.all()
    business = forms.ModelChoiceField(queryset=queryset, empty_label=None)

class TagForm(forms.Form):
    tag = forms.CharField()

class DirForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Maintainer.objects.all(),empty_label=None,label='指定安装人员')

def direct_user(request,id=None):
    router = Routing.objects.get(id=id)
    busy = router.business
    if request.method == 'POST':
        df = DirForm(request.POST)
        if df.is_valid():
            user = df.cleaned_data['user']
    else:
        df = DirForm()
    variables = RequestContext(request,{'df':df,'router':router,'busy':busy})
    return render_to_response('direct.html',variables)

       
def Routing_install(request, id=None):
    condition = not_installed
    router = Routing.objects.get(id=id)
    busy = router.business
     
    return render_to_response('routinginstall.html',variables)


def ulogin(request):
    if request.method == 'POST':
        lf = LogForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                if user in users:
                    login(request,user)
                    return HttpResponseRedirect('/show_busy/')
            else:
                return HttpResponseRedirect('/ulogin')
    else:
        lf = LogForm()
    variables = RequestContext(request, {'lf':lf})
    return render_to_response('ulogin.html',variables)
@login_required    
def user_add(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            number = uf.cleaned_data['number']
            username = uf.cleaned_data['username']
            name = uf.cleaned_data['name']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            phonenumber = uf.cleaned_data['phonenumber']
            headImg = uf.cleaned_data['headImg']
            identity = uf.cleaned_data['identity']
            remarks = uf.cleaned_data['remarks']
            user = User.objects.create_user(username=username,password=password,email=email)
            Maintainer.objects.create(number=number, name=name, phonenumber=phonenumber, headImg=headImg, identity=identity, remarks=remarks, user=user)
            return HttpResponse('ok')
    else:
        uf = UserForm()
    variables = RequestContext(request, {'uf':uf})
    return render_to_response('user_add.html',variables)


@login_required    
def business_add(request):
   if request.method == "POST":
      bf = BusyForm(request.POST)
      if bf.is_valid():
          number = bf.cleaned_data['number']
          name = bf.cleaned_data['name']
          tag = bf.cleaned_data['tag']
          district = bf.cleaned_data['district']
          address = bf.cleaned_data['address']
          bmap = bf.cleaned_data['bmap']
          condition = bf.cleaned_data['condition']
          installor = bf.cleaned_data['installor']
          Maintainer.name = installor
          installor = Maintainer.name
          installtime = bf.cleaned_data['installtime']
          remarks = bf.cleaned_data['remarks']
          Business.objects.create(number=number, name=name, shopname=shopname, district=district, address=address\
          ,bmap=bmap, condition=condition, installor=adder, installtime=installtime, remarks=remarks)
          return HttpResponse('ok')
   else:
       bf = BusyForm()
   variables = RequestContext(request,{'bf':bf})
   return render_to_response('business_add.html',variables)

@login_required    
def routing_add(request):
    if request.method == "POST":
        rf = RoutingForm(request.POST)
        if rf.is_valid():
            number = rf.cleaned_data['number']
            password = rf.cleaned_data['password']
            mac = rf.cleaned_data['mac']
            ssid = rf.cleaned_data['ssid']
            remarks = rf.cleaned_data['remarks']
            business = rf.cleaned_data['business']
            Routing.objects.create(number=number, password=password, mac=mac, ssid=ssid, remarks=remarks, business=business)
    else:
        rf = RoutingForm()
    variables = RequestContext(request,{'rf':rf})
    return render_to_response('routing_add.html',variables)
  
@login_required    
def cooper_add(request):
   if request.method == "POST":
       cf = CooperForm(request.POST)
       if cf.is_valid():
           number = cf.cleaned_data['number']
           starttime = cf.cleaned_data['starttime']
           endtime = cf.cleaned_data['endtime']
           cooperImg = cf.cleaned_data['cooperImg']
           desc = cf.cleaned_data['desc']
           business = cf.cleaned_data['business']
           Business.name = business
           CooperInfo.objects.create(number=number, starttime=starttime, endtime=endtime, cooperImg=cooperImg, desc=desc, bussiness=Business.name)
   else:
       cf = CooperForm()
   variables = RequestContext(request,{'cf':cf})
   return render_to_response('cooper_add.html',variables)

@login_required    
def tag_add(request):
   if request.method == "POST":
       tf = TagForm(request)
       if tf.is_valid():
           tag = tf.cleaned_data['tag']
   else:
       tf = TagForm()
   variables = RequestContext(request,{'tf':tf})
   return render_to_response('tag_add.html', variables)

@login_required    
def show_busy(request):
    user = request.user
    group = user.groups.all()[0]
    business = Business.objects.all()
    variables = RequestContext(request,{'business':business,'group':group})
    return render_to_response('show_busy.html',variables)

@login_required    
def show_router(request):
    user = request.user
    group = user.groups.all()[0]
    routers = Routing.objects.all()
    variables = RequestContext(request,{'routers':routers,'group':group})
    return render_to_response('show_router.html',variables)

def ulogout(request):
    logout(request)
    del request.user
    return HttpResponseRedirect('/login/')

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
