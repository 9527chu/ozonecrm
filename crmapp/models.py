#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CONDITION_CHOICES= (
     (u'未安装', u'未安装'),
     (u'安装中', u'安装中'),
     (u'已安装', u'已安装中'),
)

idtype=(
    (u'管理员', u'管理员'),
    (u'安装员', u'安装员'),
)

class Maintainer(models.Model):
    number = models.CharField(max_length=30, verbose_name='编号')
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    phonenumber= models.IntegerField(max_length=200, verbose_name=u'手机号码')
    headImg = models.FileField(upload_to='./images', verbose_name=u'头像', blank=True)
    remarks = models.TextField(verbose_name=u'备注')
    identity = models.CharField(max_length=20, choices=idtype, verbose_name=u'身份')
    user = models.OneToOneField(User, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'人员管理'
        verbose_name_plural = u'人员管理'
        ordering = ['number']


class Tag(models.Model):
    tag = models.CharField(max_length=30, verbose_name=u'经营内容')
    
    def __unicode__(self):
       return self.tag
    
    class Meta:
        verbose_name = u'经营内容'
        verbose_name_plural = u'经营内容'

class Business(models.Model):
    number = models.CharField(max_length=30,verbose_name=u'编号')
    name   = models.CharField(max_length=30, verbose_name=u'商家名称')
    shopname = models.CharField(max_length=30, verbose_name=u'门店名称')
    tag = models.ManyToManyField(Tag, verbose_name='经营内容')
    district = models.CharField(max_length=300, verbose_name=u'地区')
    address = models.CharField(max_length=300, verbose_name=u'地址')
    bmap = models.BooleanField(verbose_name=u'地图')
    adder = models.ForeignKey(Maintainer, verbose_name=u'添加人员', related_name='adder')
    addtime = models.DateField(verbose_name=u'添加日期')
    condition = models.CharField(max_length=30, choices=CONDITION_CHOICES,verbose_name=u'状态')
    installor = models.ForeignKey(Maintainer, verbose_name=u'安装人员', related_name='installor')
    installtime = models.DateField(verbose_name=u'安装时间')
    remarks = models.CharField(max_length=150, verbose_name=u'备注')

    def __unicode__(self):
        return self.name 
    
    class Meta:
        verbose_name = u'商家管理'
        verbose_name_plural =u'商家管理'
        ordering = ['number']


class Routing(models.Model):
    number = models.CharField(max_length=30, verbose_name=u'路由编号')
    gateway = models.CharField(max_length=50, verbose_name=u'网关ID')
    password = models.CharField(max_length=50, verbose_name=u'路由密码')
    is_main = models.BooleanField(verbose_name=u'是否是主要路由')
    mac = models.CharField(max_length=30, verbose_name=u'mac地址')
    ssid = models.CharField(max_length=30, verbose_name=u'ssid')
    lanip = models.CharField(max_length=30, verbose_name=u'LAN_IP')
    port  = models.CharField(max_length=30, verbose_name=u'远程端口')
    remarks = models.CharField(max_length=30, verbose_name=u'备注')    
    business = models.OneToOneField(Business, verbose_name=u'商家', blank=True)
    
    def __unicode__(self):
        return self.ssid
    
    class Meta:
        verbose_name = u'路由信息'
        verbose_name_plural = u'路由信息'
        ordering = ['number']                                                                 
                                                                     
class CooperInfo(models.Model):
    number = models.CharField(max_length=30, verbose_name=u'合同编号')
    starttime = models.DateField(verbose_name=u'起始日期')
    endtime = models.DateField(verbose_name=u'结束日期')
    cooperImg = models.FileField(upload_to='./images/cooper', verbose_name=u'合作复印件')
    desc = models.TextField(verbose_name=u'商家描述')
    business = models.OneToOneField(Business, verbose_name=u'商家')
    
    def __unicode__(self):
        return self.number
    class Meta:
        verbose_name = u'合作信息'
        verbose_name_plural = u'合作信息'
        ordering = ['number']                                                                       
