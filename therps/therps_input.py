# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012

@author: tao.hong
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import cgi
import cgitb
cgitb.enable()
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import django
from django import forms
from therps import therps_parameters,therps_tooltips
from uber import uber_lib

class THerpsInputPage(webapp.RequestHandler):
    def get(self):
        text_file = open('therps/therps_description.txt','r')
        x = text_file.read()
        templatepath = os.path.dirname(__file__) + '/../templates/'
        ChkCookie = self.request.cookies.get("ubercookie")
        html = uber_lib.SkinChk(ChkCookie, "T-Herps Inputs")
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'therps','page':'input'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})        
        html = html + template.render(templatepath + '04uberinput_start_tabbed.html', {
                'model':'therps', 
                'model_attributes':'T-Herps Inputs'})
        html = html + """
        <div class="input_nav">
            <ul>
                <li class="Chemical tabSel"> Chemical</li>
                |<li class="Avian tabUnsel"> Avian</li>
                |<li class="Herptile tabUnsel"> Herptile</li>
            </ul>
        </div>
        """
        html = html + """<br><table class="tab tab_Chemical" border="0">"""
        html = html + str(therps_parameters.trexInp_chem())
        html = html + """</table><table class="tab tab_Avian" border="0" style="display:none">"""
        html = html + str(therps_parameters.trexInp_bird())
        html = html + """</table><table class="tab tab_Herptile" border="0" style="display:none">"""
        html = html + str(therps_parameters.trexInp_herp())
        html = html + template.render(templatepath + '04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
        html = html + template.render(templatepath + 'therps-jquery.html', {})
        # Check if tooltips dictionary exists
        if hasattr(therps_tooltips, 'tooltips'):
            tooltips = therps_tooltips.tooltips
        else:
            tooltips = {}
        html = html + template.render (templatepath + '05ubertext_tooltips_right.html', {'tooltips':tooltips})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', THerpsInputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    
    