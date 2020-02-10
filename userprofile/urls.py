from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list', views.all_posts, name='list'),
    url(r'^details', views.profile, name='profile'),
    url(r'^update/profile/(?P<pk>\d+)/$', views.update_user, name='update_pro'),
    url(r'^update/profile', views.update_dart, name='updateper'),
    url(r'^service/(?P<pk>\d+)/$', views.update_user, name='service_in'),
    url(r'^service/main', views.update_dart, name='updateper'),
    url(r'^update/(?P<pk>\d+)/$', views.update_post, name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_post, name='delete'),
]
