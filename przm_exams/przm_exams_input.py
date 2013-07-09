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
from przm_exams import przm_exams_parameters


class PRZMEXAMSInputPage(webapp.RequestHandler):
    def get(self):
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title':'Ubertool'})
        html = html + template.render(templatepath + 'przm_exams_jquery.html', {})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'przm_exams','page':'input'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        html = html + template.render(templatepath + '04uberinput_start_tabbed.html', {
                'model':'przm_exams', 
                'model_attributes':'PRZM-EXAMS Inputs'})
        html = html + """
        <div id="input_nav">
            <ul>
                <li>| <a class="PRZM" style="color:#FFA500; font-weight:bold"> PRZM Inputs</a> </li>
                <li>| <a class="EXAMS" style="font-weight:bold"> EXAMS Inputs</a> |</li>
            </ul>
        </div>
        """
        html = html + """<br><table class="tab tab_PRZM" border="0">"""
        html = html + str(przm_exams_parameters.PRZMInp())
        html = html + """</table><table class="tab tab_EXAMS" border="0" style="display:none">"""
        html = html + str(przm_exams_parameters.EXAMSInp())
        html = html + """</table><table class="tab tab_EXAMS n_ph" border="0" style="display:none">
                                    <tr><th><label for="n_ph">Number of Different pH:</label></th>
                                        <td><select name="n_ph" id="n_ph">
                                            <option value="">Make a selection</option>
                                            <option value="3">3</option>
                                            <option value="4">4</option>
                                            <option value="5">5</option>
                                            <option value="6">6</option>
                                            <option value="7">7</option>
                                            <option value="8">8</option>
                                            <option value="9">9</option>
                                            <option value="10">10</option></select>
                                        </td>
                                    </tr>""" 
        html = html + template.render(templatepath + 'przm_exams_input_end.html', {'sub_title': 'Submit'})
        html = html + template.render(templatepath + '05ubertext_tooltips_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', PRZMEXAMSInputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
    
    