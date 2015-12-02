from django.conf.urls import url
from app.user import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.userindex, name='user_index'),
]
