#coding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from crmapp.models import *

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'district', 'address', 'bmap', 'condition', 'installor', 'installtime', 'remarks']
    search_fields = ['number', 'name']
    list_filter = ['number', 'name']
    list_per_page = 10
    save_as = True
    save_on_top = True


class MaintainerAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'phonenumber', 'headImg', 'remarks']
    search_fields = ['number', 'name']
    list_filter = ['number', 'name']
    list_per_page = 10
    save_as = True
    save_on_top = True

admin.site.register(Maintainer,MaintainerAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Routing)
admin.site.register(CooperInfo)
admin.site.register(Tag)
