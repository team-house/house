# coding: utf-8

from django.conf.urls import url

from website.views import (
    home,
    user,
)

# 管理后台
urlpatterns = [
    # 首页
    url(r'^$', home.index, name='home_index'),
    url(r'^register$', home.register, name='home_register'),
    url(r'^login$', home.login, name='home_login'),

    # 用户
    url(r'^user$', user.index, name='user_index'),
    url(r'^user/update_profile$', user.update_profile, name='update_profile'),
    url(r'^user/update_avatar$', user.update_avatar, name='update_avatar'),
    url(r'^login_out$', user.login_out, name='login_out'),
    # 房源发布
    url(r'^housing_resources/create$', user.housing_resource_create, name='housing_resource_create'),
    url(r'^housing_resources/(?P<housing_resources_id>\d+)/edit$', user.housing_resource_edit, name='housing_resource_edit'),
    url(r'^housing_resources$', user.housing_resources, name='housing_resources'),
    # 求租发布
    url(r'^rent_house_create$', user.rent_house_create, name='rent_house_create'),
    url(r'^rent_house$', user.rent_house, name='rent_house'),
]
