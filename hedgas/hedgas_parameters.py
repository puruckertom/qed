# -*- coding: utf-8 -*-
"""
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
from django import forms
from django.db import models
from django.utils.safestring import mark_safe

class hedgas_acuteNonOcc_Inp(forms.Form):
    choose_acuteNonOcc = (('1','Yes'),('0','No'))
    run_acuteNonOcc = forms.ChoiceField(required=True,label='Run Acute HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_acuteNonOcc, initial='1')
    mw_acuteNonOcc = forms.FloatField(label='Molecular Weight')
    noael_acuteNonOcc = forms.FloatField(label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_acuteNonOcc = forms.FloatField(label='Hours animal study (acute)')
    hrs_human_acuteNonOcc = forms.FloatField(label='Hours human (acute)')
    dow_animal_acuteNonOcc = forms.FloatField(label='Days of week animal (acute)')
    dow_human_acuteNonOcc = forms.FloatField(label='Days of week human (acute)')
    b0_acuteNonOcc = forms.FloatField(label=mark_safe('b<sub>0</sub>'))
    b1_acuteNonOcc = forms.FloatField(label=mark_safe('b<sub>1</sub>'))
    SAa_acuteNonOcc = forms.FloatField(label='SAa')
    tb_acuteNonOcc = forms.FloatField(label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_acuteNonOcc = forms.FloatField(label=mark_safe('PU (m<sup>2</sup>)'))

class hedgas_stitNonOcc_Inp(forms.Form):
    choose_stitNonOcc = (('1','Yes'),('0','No'))
    run_stitNonOcc = forms.ChoiceField(required=True,label='Run ST/IT HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_stitNonOcc, initial='0')
    mw_stitNonOcc = forms.FloatField(label='Molecular Weight')
    noael_stitNonOcc = forms.FloatField(label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_stitNonOcc = forms.FloatField(label='Hours animal study (subchronic)')
    hrs_human_stitNonOcc = forms.FloatField(label='Hours human (subchronic)')
    dow_animal_stitNonOcc = forms.FloatField(label='Days of week animal*')
    dow_human_stitNonOcc = forms.FloatField(label='Days of week human')
    b0_stitNonOcc = forms.FloatField(label=mark_safe('b<sub>0</sub>'))
    b1_stitNonOcc = forms.FloatField(label=mark_safe('b<sub>1</sub>'))
    SAa_stitNonOcc = forms.FloatField(label='SAa')
    tb_stitNonOcc = forms.FloatField(label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_stitNonOcc = forms.FloatField(label=mark_safe('PU (m<sup>2</sup>)'))

class hedgas_ltNonOcc_Inp(forms.Form):
    choose_ltNonOcc = (('1','Yes'),('0','No'))
    run_ltNonOcc = forms.ChoiceField(required=True,label='Run Acute HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_ltNonOcc, initial='0')
    mw_ltNonOcc = forms.FloatField(required=True,label='Molecular Weight')
    noael_ltNonOcc = forms.FloatField(required=True,label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_ltNonOcc = forms.FloatField(required=True,label='Hours animal study (acute)')
    hrs_human_ltNonOcc = forms.FloatField(required=True,label='Hours human (acute)')
    dow_animal_ltNonOcc = forms.FloatField(required=True,label='Days of week animal (acute)')
    dow_human_ltNonOcc = forms.FloatField(required=True,label='Days of week human (acute)')
    b0_ltNonOcc = forms.FloatField(required=True,label=mark_safe('b<sub>0</sub>'))
    b1_ltNonOcc = forms.FloatField(required=True,label=mark_safe('b<sub>1</sub>'))
    SAa_ltNonOcc = forms.FloatField(required=True,label='SAa')
    tb_ltNonOcc = forms.FloatField(required=True,label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_ltNonOcc = forms.FloatField(required=True,label=mark_safe('PU (m<sup>2</sup>)'))

class hedgas_acuteOcc_Inp(forms.Form):
    choose_acuteOcc = (('1','Yes'),('0','No'))
    run_acuteOcc = forms.ChoiceField(required=True,label='Run Acute HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_acuteOcc, initial='0')
    mw_acuteOcc = forms.FloatField(required=True,label='Molecular Weight')
    noael_acuteOcc = forms.FloatField(required=True,label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_acuteOcc = forms.FloatField(required=True,label='Hours animal study (acute)')
    hrs_human_acuteOcc = forms.FloatField(required=True,label='Hours human (acute)')
    dow_animal_acuteOcc = forms.FloatField(required=True,label='Days of week animal (acute)')
    dow_human_acuteOcc = forms.FloatField(required=True,label='Days of week human (acute)')
    b0_acuteOcc = forms.FloatField(required=True,label=mark_safe('b<sub>0</sub>'))
    b1_acuteOcc = forms.FloatField(required=True,label=mark_safe('b<sub>1</sub>'))
    SAa_acuteOcc = forms.FloatField(required=True,label='SAa')
    tb_acuteOcc = forms.FloatField(required=True,label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_acuteOcc = forms.FloatField(required=True,label=mark_safe('PU (m<sup>2</sup>)'))

class hedgas_stitOcc_Inp(forms.Form):
    choose_stitOcc = (('1','Yes'),('0','No'))
    run_stitOcc = forms.ChoiceField(required=True,label='Run Acute HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_stitOcc, initial='0')
    mw_stitOcc = forms.FloatField(required=True,label='Molecular Weight')
    noael_stitOcc = forms.FloatField(required=True,label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_stitOcc = forms.FloatField(required=True,label='Hours animal study (acute)')
    hrs_human_stitOcc = forms.FloatField(required=True,label='Hours human (acute)')
    dow_animal_stitOcc = forms.FloatField(required=True,label='Days of week animal (acute)')
    dow_human_stitOcc = forms.FloatField(required=True,label='Days of week human (acute)')
    b0_stitOcc = forms.FloatField(required=True,label=mark_safe('b<sub>0</sub>'))
    b1_stitOcc = forms.FloatField(required=True,label=mark_safe('b<sub>1</sub>'))
    SAa_stitOcc = forms.FloatField(required=True,label='SAa')
    tb_stitOcc = forms.FloatField(required=True,label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_stitOcc = forms.FloatField(required=True,label=mark_safe('PU (m<sup>2</sup>)'))

class hedgas_ltOcc_Inp(forms.Form):
    choose_ltOcc = (('1','Yes'),('0','No'))
    run_ltOcc = forms.ChoiceField(required=True,label='Run Acute HEC Non-Occupational?',widget=forms.RadioSelect(attrs={'class':'inline_radio'}), choices=choose_ltOcc, initial='0')
    mw_ltOcc = forms.FloatField(required=True,label='Molecular Weight')
    noael_ltOcc = forms.FloatField(required=True,label='NOAEL')
    #radio button for unit mg/m3  or   ppm
    hrs_animal_ltOcc = forms.FloatField(required=True,label='Hours animal study (acute)')
    hrs_human_ltOcc = forms.FloatField(required=True,label='Hours human (acute)')
    dow_animal_ltOcc = forms.FloatField(required=True,label='Days of week animal (acute)')
    dow_human_ltOcc = forms.FloatField(required=True,label='Days of week human (acute)')
    b0_ltOcc = forms.FloatField(required=True,label=mark_safe('b<sub>0</sub>'))
    b1_ltOcc = forms.FloatField(required=True,label=mark_safe('b<sub>1</sub>'))
    SAa_ltOcc = forms.FloatField(required=True,label='SAa')
    tb_ltOcc = forms.FloatField(required=True,label=mark_safe('TB (cm<sup>2</sup>)'))
    pu_ltOcc = forms.FloatField(required=True,label=mark_safe('PU (m<sup>2</sup>)'))