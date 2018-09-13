#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from . import views

from django.urls import path





app_name = 'news_base'

urlpatterns = [
    #
    # path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    # 交易列表
    path('events/', views.events, name='events'),
    # 信息提交
    path('imformation/', views.imformation, name='imformations'),
    # 公司介绍
    path('about/', views.about, name='about'),
    # 欢迎合作
    path('', views.cooperation, name='cooperation'),

    # 服务范围
    path('services/', views.services, name='services')


    # 招聘信息
]