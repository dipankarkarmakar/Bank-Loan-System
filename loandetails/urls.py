from django.conf.urls import url
from .views import updateloandata

urlpatterns = [
    url(r'^updateloandata/$', updateloandata)
]