from django.conf.urls import url
from videora import api, views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='Movies'

urlpatterns = [
    url(r'^api/name=(?P<name>[A-Z,a-z," ",""]+|)?&g=(?P<genre>[A-Z,a-z," ",""]+|)$',api.API_res,name="api"),
]
