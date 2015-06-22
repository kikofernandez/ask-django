from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from instance import views

urlpatterns = [
    url(r'^ask/$', views.ServiceList.as_view()),
    url(r'^ask/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
