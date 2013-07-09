# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:50:59 2012

@author: JHarston
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from google.appengine.api import users
import datetime

class RiceInp(forms.Form):

    config_name = forms.CharField(label="Use Configuration Name", initial="use-config-%s"%datetime.datetime.now())     
    chemical_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}))
    mai = forms.FloatField(required=True,label='Mass of Applied Ingredient Applied to Paddy (kg)')
    dsed = forms.FloatField(required=True,label='Sediment Depth (m)')
    area = forms.FloatField(required=True,label=mark_safe('Area of the Rice Paddy (m<sup>2</sup>)'))
    pb = forms.FloatField(required=True,label=mark_safe('Bulk Density of Sediment (kg/m<sup>3</sup>)'))
    dw = forms.FloatField(required=True,label='Water Column Depth (m)')
    osed = forms.FloatField(required=True,label='Porosity of Sediment')
    Kd = forms.FloatField(required=True,label='Water-Sediment Partitioning Coefficient (L/kg)')
