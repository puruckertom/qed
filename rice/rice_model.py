import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import numpy as np
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
import numpy as np
import cgi
import cgitb
cgitb.enable()

# The mass of the sediment at equilibrium with the water column

def msed(dsed,a,pb):
    try:
        dsed = float(dsed)
        a = float(a)
        pb = float(pb)
    except IndexError:
        raise IndexError\
        ('The sediment depth, area of the rice paddy, and/or the bulk'\
        ' density of the sediment must be supplied the command line.')
    except ValueError:
        raise ValueError\
        ('The sediment depth must be a real number, not "%m"' % dsed)
    except ValueError:
        raise ValueError\
        ('The area of the rice paddy must be a real number, not "%ha"' % a)
    except ValueError:
        raise ValueError\
        ('The bulk density of the sediment must be a real number, not "%kg/m3".' %pb)
    if dsed < 0:
        raise ValueError\
        ('dsed=%g is a non-physical value.' % dsed)
    if a < 0:
        raise ValueError\
        ('a=%g is a non-physical value.' % a)
    if pb < 0:
        raise ValueError\
        ('pb=%g is a non-physical value.' %pb)
    return dsed * a * pb


class MsedService(webapp.RequestHandler):
    
    def get(self):
        data = simplejson.loads(self.request.body)
        data = json_utils.convert(data)
        msed_output = msed(data['dsed'],data['a'],data['pb'])
        msed_json = simplejson.dumps(msed_output)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(msed_json)


# The volume of the water column plus pore water

def vw(dw,a,dsed,osed):
    try:
        dw = float(dw)
        a = float(a)
        dsed = float(dsed)
        osed = float(osed)
    except IndexError:
        raise IndexError\
        ('The water column depth, area of the rice paddy, sediment depth, and/or'\
        ' porosity of sediment must be supplied the command line.')
    except ValueError:
        raise ValueError\
        ('The water column depth must be a real number, not "%m"' % dw)
    except ValueError:
        raise ValueError\
        ('The area of the rice paddy must be a real number, not "%ha"' % a)
    except ValueError:
        raise ValueError\
        ('The sediment depth must be a real number, not "%cm"' % dsed)
    except ValueError:
        raise ValueError\
        ('The porosity of sediment must be a real number"' % osed)
    if dw < 0:
        raise ValueError\
        ('dw=%g is a non-physical value.' % dw)
    if a < 0:
        raise ValueError\
        ('a=%g is a non-physical value.' % a)
    if dsed < 0:
        raise ValueError\
        ('dsed=%g is a non-physical value.' % dsed)
    if osed < 0:
        raise ValueError\
        ('osed=%g is a non-physical value.' % osed)
    return(dw * a) + (dsed * osed * a)



# The pesticide mass per unit area

def mai1(mai,a):
    mai = float(mai)
    a = float(a)*1e-4
    return mai/a
#    if a <= 0:
#     print('The area of the rice paddy must be greater than 0 m2')




# Water Concentration

def cw(mai1,dw,dsed,osed,pb,kd):
    try:
        mai1 = float(mai1)
        dw = float(dw)
        dsed = float(dsed)
        osed = float(osed)
        pb = float(pb)
        kd = float(kd)
    except IndexError:
        raise IndexError\
        ('The mass of pesticide applied per unit area, water column depth,'\
        ' the sediment depth, porosity of sediment, the bulk density of sediment,'\
        'and/or the water-sediment partitioning coefficient must be supplied on'\
        ' the command line.')
    except ValueError:
        raise ValueError\
        ('The mass of pesticide applied per unit area must be a real number, '\
        'not "%kg/ha"' %mai1)
    except ValueError:
        raise ValueError\
        ('The water column depth must be a real number, not "%cm"' % dw)
    except ValueError:
        raise ValueError\
        ('The sediment depth must be a real number, not "%cm"' %dsed)
    except ValueError:
        raise ValueError\
        ('The porosity of the sediment must be a real number' %osed)
    except ValueError:
        raise ValueError\
        ('The bulk density of the sediment must be a real number, not"%kg/m3"' %pb)
    except ValueError:
        raise ValueError\
        ('The water-sediment partitioning coefficient must be a real number,'\
        ' not"%kg/L"' %kd)
    if mai1 < 0:
        raise ValueError\
        ('mai1=%g is a non-physical value.' % mai1)
    if dw < 0:
        raise ValueError\
        ('dw=%g is a non-physical value.' % dw)
    if dsed < 0:
        raise ValueError\
        ('dsed=%g is a non-physical value.' % dsed)
    if osed < 0:
        raise ValueError\
        ('osed=g% is a non-physical value.' %osed)
    if pb < 0:
        raise ValueError\
        ('pb=g% is a non-physical value.' %pb)
    if kd < 0:
        raise ValueError\
        ('kd=g% is a non-physical value.' % kd)
    return mai1*1e-2 / (dw + (dsed * (osed + (pb * kd*0.001))))

app = webapp.WSGIApplication([('/msed', MsedService)],
                              debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()