from django.conf.urls import url

from .views import addperson, getperson, getallperson, delperson, updateperson

urlpatterns = [
    url(r'^addperson/$', addperson),
    url(r'^getallperson/$', getallperson),
    url(r'^getperson/$', getperson),
    url(r'^updateperson/$', updateperson),
    url(r'^delperson/$', delperson)

]
