from django.conf.urls import url

from app.user import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.UserindexView, name='index'),
    url(r'^post_create', views.CreatePostView, name='post_form'),
    url(r'^login$', views.UserLoginView, name='user_login'),
    url(r'^logout$', views.UserLogoutView, name='user_logout'),
    url(r'^register$', views.UserRegisterView, name='user_register'),
    url(r'^update/(?P<pk>[0-9]+)$', views.UserUpdateProfileView, name='user_update'),
]
