from django.conf.urls import url, include
from . import views

api_patterns = [
    url(r'^user/login$', views.user_login, name='user-login'),
    url(r'^user/logout$', views.user_logout, name='user-logout'),
    url(r'^user/register$', views.user_register, name='user-register'),
]

urlpatterns = [
    url(r'^(?P<version>(v\d+))/', include(api_patterns)),
]
