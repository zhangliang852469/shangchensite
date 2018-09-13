#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django import forms


class ImformationForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=128, required=False)
    tel = forms.CharField(label='电话', max_length=128, required=False)
    sub = forms.CharField(label='其他', max_length=50, )
