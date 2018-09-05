from django.conf.urls import include, url

from userauth import views


urlpatterns = [
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
