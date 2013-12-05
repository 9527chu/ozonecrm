# Create your views here.
#coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from crmapp.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

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
    adder = forms.ModelChoiceField(queryset=queryset1,empty_label=None,label=u'添加人员',error_messages={'required':'请选择或添加添加人员'})
    addtime = forms.CharField(label=u'添加时间',error_messages={'required':'请输入添加时间'})
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
    lanip = forms.CharField()
    port = forms.CharField()  
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

def Routing_install(request, id=None):
    business = Business.objects.get(id=id)
    name = business.name
   # shopname = business.shopname
   # address = business.address
    
    business.name = request.POST.get('name','')
    business.save()
    variables = RequestContext(request,locals())
    return render_to_response('routinginstall.html',variables)

def index(request):
    return render_to_response('rinstall.html')

def regist(request):
    number = request.POST.get('rnumber')
    request.session['number'] = number
    return HttpResponse('this is %s' % request.session['number'])
#def index(request):
#    return render_to_response('rinstall.html',{})

#def Routing_install(request):
    #if request.method == "POST":
    #    rf = RoutingForm(request.POST)
    #    rnumber = request.POST.get('number','')
    #    for r in Routing.objects.all():
    #        if rnumber == r.number:
    #            routing = Routing.objects.get(number=rnumber)
    #            if rf.is_valid():
    #                is_main = rf.cleaned_data['is_main']
    #                mac = rf.cleaned_data['mac']
    #                ssid = rf.cleaned_data['ssid']
    #                lanip = rf.cleaned_data['lanip']
    #                port = rf.cleaned_data['port']
    #                routing.is_main = is_main
    #                routing.mac = mac
    #                routing.ssid = ssid
    #                routing.lanip = lanip
    #                routing.port = port
    #                routing.save()
    #                return HttpResponse('ok')
    #else:
    #    rf = RoutingForm()
    #variables = RequestContext(request, locals())
    #return render_to_response('rinstall.html', variables)
#    rnumber = request.POST.get('numbmer','') 
#    return HttpResponse('hello %s' % rnumber)   
#def Routing_install(request):
#    if request.method == "POST":
#        rf = RoutingForm(request.POST)
#        rnumber = request.POST.get('number','')
#        for r in Routing.objects.all():
#            if rnumber == r.number: 
#                routing = Routing.objects.get(number=rnumber)
#                #routing = Routing.objects.get(id=routing.id+1)
#                #RoutingForm(initial={'number':routing.number, 'gateway':routing.gateway,'password':routing.password, 'is_main':routing.is_main, 'mac':routing.mac, 'ssid':routing.ssid,'lanip':routing.lanip,'port':routing.port, 'remarks':routing.remarks})
#                if rf.is_valid():
#                    number = rf.cleaned_data['number']
#                    gateway = rf.cleaned_data['gateway']
#                    password = rf.cleaned_data['password']
#                    is_main = rf.cleaned_data['is_main']
#                    mac = rf.cleaned_data['mac']
#                    ssid = rf.cleaned_data['ssid']
#                    lanip = rf.cleaned_data['lanip']
#                    port = rf.cleaned_data['port']
#                    remarks = rf.cleaned_data['remarks']
#                    business = rf.cleaned_data['business']
#                    routing.number = routing.number
#                    routing.gateway = routing.gateway
#                    routing.password = routing.password
#                    routing.remarks = routing.remarks
#                    routing.is_main=is_main
#                    routing.mac=mac
#                    routing.ssid=ssid
#                    routing.lanip=lanip 
#                    routing.port=port 
#                    routing.save()
#                    return HttpResponse('ok') 
#    else:
#        rnumber = request.POST.get('number','')
#        for r in Routing.objects.all():
#            if rnumber == r.number:    
#                routing = Routing.objects.get(number=rnumber)     
#                rf = RoutingForm(initial={'number':routing.number, 'gateway':routing.gateway,'password':routing.password, 'is_main':routing.is_main, 'mac':routing.mac, 'ssid':routing.ssid,'lanip':routing.lanip,'port':routing.port, 'remarks':routing.remarks})
#    variables = RequestContext(request, locals())
#    return render_to_response('rinstall.html', variables)          
#def Routing_install(request):
#    rnumber = request.POST.get('number','')
#    for r in Routing.objects.all():
#        if rnumber == r.number: 
#            routing = Routing.objects.get(number=rnumber)
#            gateway = routing.gateway
#            rpassword = routing.password
#            is_main = routing.is_main
#            mac = routing.mac
#            ssid = routing.ssid
#            lanip = routing.lanip
#            port = routing.port
#            
#           # is_m = request.POST.get('im')
#           # mac = request.POST.get('mac')
#           # ssid = request.POST.get('ssid')
#           # lanip = request.POST.get('lanip')
#           # port = request.POST.get('port')
#            #Routing(number=routing.number,gateway=gateway,password=rpassword,is_main=is_m,\
#            #mac=mac, ssid=ssid, lanip=lanip, port=port).save()
#            #Routing.save()
#            business = routing.business
#            shopname = business.shopname
#            tag = business.tag
#            district = business.district
#    variables = RequestContext(request, locals())
#    return render_to_response('rinstall.html', variables)
   # if request.method == 'POST':
   #     rf = RoutingForm(request.POST, request.FILES)
   #     bf = BusinessForm(request.POST, request.FILES)
   #     cf = CooperForm(request.POST, request.FILES)
   #     if rf.is_valid() and bf.is_valid() and cf.is_valid():
   #         rnumber = rf.cleaned_data['number']
   #         gateway = rf.cleaned_data['gateway']
   #         rpassword = rf.cleaned_data['password']
   #         is_main = rf.cleaned_data['is_main']
             
       
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


def business_add(request):
   if request.method == "POST":
      bf = BusyForm(request.POST)
      if bf.is_valid():
          number = bf.cleaned_data['number']
          name = bf.cleaned_data['name']
          shopname = bf.cleaned_data['shopname']
          tag = bf.cleaned_data['tag']
          district = bf.cleaned_data['district']
          address = bf.cleaned_data['address']
          bmap = bf.cleaned_data['bmap']
          adder = bf.cleaned_data['adder']
          Maintainer.name = adder
          adder = Maintainer.name
          addtime = bf.cleaned_data['addtime']
          condition = bf.cleaned_data['condition']
          installor = bf.cleaned_data['installor']
          Maintainer.name = installor
          installor = Maintainer.name
          installtime = bf.cleaned_data['installtime']
          remarks = bf.cleaned_data['remarks']
          Business.objects.create(number=number, name=name, shopname=shopname, district=district, address=address\
          ,bmap=bmap, adder=adder, addtime=addtime, condition=condition, installor=adder, installtime=installtime, remarks=remarks)
          return HttpResponse('ok')
   else:
       bf = BusyForm()
   variables = RequestContext(request,{'bf':bf})
   return render_to_response('business_add.html',variables)

def routing_add(request):
    if request.method == "POST":
        rf = RoutingForm(request.POST)
        if rf.is_valid():
            number = rf.cleaned_data['number']
            gateway = rf.cleaned_data['gateway']
            password = rf.cleaned_data['password']
            is_main = rf.cleaned_data['is_main']
            mac = rf.cleaned_data['mac']
            ssid = rf.cleaned_data['ssid']
            port = rf.cleaned_data['port']
            remarks = rf.cleaned_data['remarks']
            business = rf.cleaned_data['business']
            Routing.objects.create(number=number, gateway=gateway, password=password, is_main=is_main, mac=mac, ssid=ssid, port=port, remarks=remarks, business=business)
    else:
        rf = RoutingForm()
    variables = RequestContext(request,{'rf':rf})
    return render_to_response('routing_add.html',variables)
  
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

def tag_add(request):
   if request.method == "POST":
       tf = TagForm(request)
       if tf.is_valid():
           tag = tf.cleaned_data['tag']
   else:
       tf = TagForm()
   variables = RequestContext(request,{'tf':tf})
   return render_to_response('tag_add.html', variables)

def show_busy(request):
    business = Business.objects.all()
    variables = RequestContext(request,{'business':business})
    return render_to_response('show_busy.html',variables)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
