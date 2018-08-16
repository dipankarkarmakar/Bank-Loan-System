from django.conf.urls import url
from .views import addloan, getallloan, updateloan, deleteloan, getloan, fetchloan

urlpatterns = [
    url(r'^addloan/$', addloan),
    url(r'^getloan/$', getloan),
    url(r'^fetchloan/$', fetchloan),
    url(r'^getallloan/$', getallloan),
    url(r'^updateloan/$', updateloan),
    url(r'^deleteloan/$', deleteloan),

]