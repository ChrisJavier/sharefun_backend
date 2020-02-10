from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/page_login.html'), name='login'),
    url(r'^home/$', auth_views.LoginView.as_view(template_name='app/home.html'), name='home'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='app/home.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
