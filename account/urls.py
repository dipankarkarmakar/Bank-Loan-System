from django.conf.urls import url
from .views import addaccount, getallaccount, getaccount, updateaccount,delaccount,nameaccount,fetchaccount

urlpatterns = [
    url(r'^addaccount/$', addaccount),
    url(r'^getallaccount/$', getallaccount),
    url(r'^getaccount/$', getaccount),
    url(r'^updateaccount/$', updateaccount),
    url(r'^delaccount/$', delaccount),
    url(r'^nameaccount/$', nameaccount),
    url(r'^fetchaccount/$', fetchaccount),

]