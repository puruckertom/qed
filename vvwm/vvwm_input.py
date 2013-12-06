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
from vvwm import vvwm_parameters
from przm5 import przm5_parameters
from uber import uber_lib

class vvwmInputPage(webapp.RequestHandler):
    def get(self):
        templatepath = os.path.dirname(__file__) + '/../templates/'
        ChkCookie = self.request.cookies.get("ubercookie")
        html = uber_lib.SkinChk(ChkCookie)
        html = html + template.render (templatepath + 'vvwm-jquery.html', {})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'vvwm','page':'input'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        html = html + template.render(templatepath + '04uberinput_start_tabbed.html', {
                'model':'vvwm', 
                'model_attributes':'Variable Volume Water Model Inputs'})
        html = html + """
        <div class="input_nav">
            <ul>
                <li class="Chemical tabSel">Chemical </li>
                |<li class="CropLand tabUnsel"> Crop/Land </li>
                |<li class="WaterBody tabUnsel"> Water Body </li>
            </ul>
        </div>
        """
        html = html + """<br><table class="tab tab_Chemical">"""
        html = html + str(przm5_parameters.przm5Inp_chem())
        html = html + str(vvwm_parameters.vvwmInp_chem())
        html = html + """</table><table class="tab tab_Chemical0">"""
        html = html + str(przm5_parameters.przm5Inp_chem0())
        html = html + """</table><table class="tab tab_Chemical1" style="display:none">
                            <tr><th colspan="2">Degradate 1</th></tr>
                            """
        html = html + str(przm5_parameters.przm5Inp_chem1())
        html = html + """</table><table class="tab tab_Chemical_MCF1" style="display:none">
                            <tr><th colspan="2">Molar Conversion Factors (Degradate 1)</th></tr>
                            """
        html = html + str(przm5_parameters.przm5Inp_mcf1())
        html = html + """</table><table class="tab tab_Chemical2" style="display:none">
                            <tr><th colspan="2">Degradate 2</th></tr>
                            """
        html = html + str(przm5_parameters.przm5Inp_chem2())
        html = html + """</table><table class="tab tab_Chemical_MCF2" style="display:none">
                            <tr><th colspan="2">Molar Conversion Factors (Degradate 2)</th></tr>
                            """
        html = html + str(przm5_parameters.przm5Inp_mcf2())
        html = html + template.render (templatepath + 'vvwm_weatherfile.html', {})
        html = html + str(vvwm_parameters.vvwmInp_cropland())
        html = html + """</table><table class="tab tab_WaterBody" style="display:none">"""
        html = html + str(vvwm_parameters.vvwmInp_waterbody())
        html = html + template.render(templatepath + '04uberinput_tabbed_end.html', {'sub_title': 'Submit'})
        html = html + template.render(templatepath + '05ubertext_tooltips_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', vvwmInputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()