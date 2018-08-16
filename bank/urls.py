from django.conf.urls import url
from .views import addbank, getbank, getallbank, updatebank, delbank

urlpatterns = [
    url(r'^addbank/$', addbank),
    url(r'^getallbank/$', getallbank),
    url(r'^getbank/$', getbank),
    url(r'^updatebank/$', updatebank),
    url(r'^delbank/$', delbank),

]
