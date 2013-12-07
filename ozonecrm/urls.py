from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
    url(r"^media/(?P<path>.*)$","django.views.static.serve",{"document_root": settings.MEDIA_ROOT,}),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'crmapp/ulogin.html'}),
    # Examples:
    # url(r'^$', 'ozonecrm.views.home', name='home'),
    # url(r'^ozonecrm/', include('ozonecrm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$','crmapp.views.ulogout'),
    url(r'^login/$','crmapp.views.ulogin'),
    url(r'^user_home/$','crmapp.views.user_home'),
    url(r'^write_mail/$','crmapp.views.write_mail'),
    url(r'^direct/(\d+)','crmapp.views.direct_user'),
    url(r'^show_info/(\d+)/(\d+)','crmapp.views.show_info'),
    url(r'^routing_install/(\d+)/(\d+)','crmapp.views.routing_install'),
    url(r'^user_add','crmapp.views.user_add'),
    url(r'^business_add','crmapp.views.business_add'),
    url(r'^routing_add','crmapp.views.routing_add'),
    url(r'^cooper_add','crmapp.views.cooper_add'),
    url(r'^tag_add','crmapp.views.tag_add'),
    url(r'^show_busy','crmapp.views.show_busy'),
    url(r'^show_router','crmapp.views.show_router'),
   # url(r'^index','crmapp.views.index'),
   # url(r'^regist','crmapp.views.regist'),
    url(r'^display_meta','crmapp.views.display_meta'),
)
