from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from app import views, viewsets

urlpatterns = [
    url(r'^customer/list/$', viewsets.CustomerListViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
