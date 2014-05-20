
class rice(object):
    def __init__(self, chemical_name, mai, dsed, a, pb, dw, osed, kd):
        self.chemical_name = chemical_name
        self.mai = mai
        self.dsed = dsed
        self.a = a
        self.pb = pb
        self.dw = dw
        self.osed = osed
        self.kd = kd
        #outputs
        self.msed = -1
        self.vw = -1
        self.mai1 = -1
        self.cw = -1
        self.run_methods()

    def run_methods(self):
        self.Calcmsed()
        self.Calcvw()
        self.Calcmai1()
        self.Calccw()

    # The mass of the sediment at equilibrium with the water column
    def Calcmsed(self):
        if self.msed == -1:
            try:
                self.dsed = float(self.dsed)
                self.a = float(self.a)
                self.pb = float(self.pb)
            except IndexError:
                raise IndexError\
                ('The sediment depth, area of the rice paddy, and/or the bulk'\
                ' density of the sediment must be supplied the command line.')
            except ValueError:
                raise ValueError\
                ('The sediment depth must be a real number, not "%m"' % self.dsed)
            except ValueError:
                raise ValueError\
                ('The area of the rice paddy must be a real number, not "%ha"' % self.a)
            except ValueError:
                raise ValueError\
                ('The bulk density of the sediment must be a real number, not "%kg/m3".' % self.pb)
            if self.dsed < 0:
                raise ValueError\
                ('dsed=%g is a non-physical value.' % self.dsed)
            if self.a < 0:
                raise ValueError\
                ('a=%g is a non-physical value.' % self.a)
            if self.pb < 0:
                raise ValueError\
                ('pb=%g is a non-physical value.' % self.pb)
            self.msed = self.dsed * self.a * self.pb
        return self.msed



    # The volume of the water column plus pore water
    def Calcvw(self):
        if self.vw == -1:
            try:
                self.dw = float(self.dw)
                self.a = float(self.a)
                self.dsed = float(self.dsed)
                self.osed = float(self.osed)
            except IndexError:
                raise IndexError\
                ('The water column depth, area of the rice paddy, sediment depth, and/or'\
                ' porosity of sediment must be supplied the command line.')
            except ValueError:
                raise ValueError\
                ('The water column depth must be a real number, not "%m"' % self.dw)
            except ValueError:
                raise ValueError\
                ('The area of the rice paddy must be a real number, not "%ha"' % self.a)
            except ValueError:
                raise ValueError\
                ('The sediment depth must be a real number, not "%cm"' % self.dsed)
            except ValueError:
                raise ValueError\
                ('The porosity of sediment must be a real number"' % self.osed)
            if self.dw < 0:
                raise ValueError\
                ('dw=%g is a non-physical value.' % self.dw)
            if self.a < 0:
                raise ValueError\
                ('a=%g is a non-physical value.' % self.a)
            if self.dsed < 0:
                raise ValueError\
                ('dsed=%g is a non-physical value.' % self.dsed)
            if self.osed < 0:
                raise ValueError\
                ('osed=%g is a non-physical value.' % self.osed)
            self.vw = (self.dw * self.a) + (self.dsed * self.osed * self.a)
        return self.vw



    # The pesticide mass per unit area
    def Calcmai1(self):
        if self.mai1 == -1:
            try:
                self.mai = float(self.mai)
                self.a = float(self.a)
            except IndexError:
                raise IndexError\
                ('The mass applied to patty and area of the patty must be supplied the command line.')
            except ValueError:
                raise ValueError\
                ('The area of the rice paddy must be a real number, not "%ha"' % self.a)
            except ValueError:
                raise ValueError\
                ('The area of the rice paddy must be a real number, not "%ha"' % self.mai)
            if self.a < 0:
                raise ValueError\
                ('a=%g is a non-physical value.' % self.a)
            if self.mai < 0:
                raise ValueError\
                ('mai=%g is a non-physical value.' % self.mai)
            self.mai1 = (self.mai/self.a)*10000
        return self.mai1

    #    if a <= 0:
    #     print('The area of the rice paddy must be greater than 0 m2')


    # Water Concentration
    def Calccw(self):
        if self.cw == -1:
            try:
                self.mai1 = float(self.mai1)
                self.dw = float(self.dw)
                self.dsed = float(self.dsed)
                self.osed = float(self.osed)
                self.pb = float(self.pb)
                self.kd = float(self.kd)
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
                ('The water column depth must be a real number, not "%cm"' % self.dw)
            except ValueError:
                raise ValueError\
                ('The sediment depth must be a real number, not "%cm"' % self.dsed)
            except ValueError:
                raise ValueError\
                ('The porosity of the sediment must be a real number' % self.osed)
            except ValueError:
                raise ValueError\
                ('The bulk density of the sediment must be a real number, not"%kg/m3"' % self.pb)
            except ValueError:
                raise ValueError\
                ('The water-sediment partitioning coefficient must be a real number,'\
                ' not"%kg/L"' % self.kd)
            if self.mai1 < 0:
                raise ValueError\
                ('mai1=%g is a non-physical value.' % self.mai1)
            if self.dw < 0:
                raise ValueError\
                ('dw=%g is a non-physical value.' % self.dw)
            if self.dsed < 0:
                raise ValueError\
                ('dsed=%g is a non-physical value.' % self.dsed)
            if self.osed < 0:
                raise ValueError\
                ('osed=g% is a non-physical value.' % self.osed)
            if self.pb < 0:
                raise ValueError\
                ('pb=g% is a non-physical value.' % self.pb)
            if self.kd < 0:
                raise ValueError\
                ('kd=g% is a non-physical value.' % self.kd)
            self.cw = (self.mai1 / (self.dw + (self.dsed * (self.osed + (self.pb * self.kd*1e-5)))))*100
        return self.cw
