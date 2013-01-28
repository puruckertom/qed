# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:50:49 2013

@author: MSnyder
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
from agdrift import agDriftdb
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import numpy as np
import cgi
import cgitb
import math
import csv

cgitb.enable()
pond_aerial_vf2f = [2.425E+01,2.319E+01,2.227E+01,2.144E+01,2.069E+01,1.997E+01,1.930E+01,
1.866E+01,1.806E+01,1.749E+01,1.696E+01,1.645E+01,1.596E+01,1.549E+01,
1.506E+01,1.464E+01,1.425E+01,1.388E+01,1.353E+01,1.320E+01,1.288E+01,
1.257E+01,1.228E+01,1.200E+01,1.174E+01,1.149E+01,1.125E+01,1.103E+01, 
1.081E+01,1.059E+01,1.039E+01,1.020E+01,1.001E+01,9.837E+00,9.670E+00,
9.510E+00,9.350E+00,9.200E+00,9.058E+00,8.920E+00,8.780E+00,8.650E+00,
8.520E+00,8.400E+00,8.290E+00,8.170E+00,8.060E+00,7.950E+00,7.850E+00,
7.750E+00,7.650E+00,7.554E+00,7.460E+00,7.370E+00,7.290E+00,7.200E+00,
7.120E+00,7.040E+00,6.960E+00,6.880E+00,6.810E+00,6.741E+00,6.670E+00,
6.600E+00,6.540E+00,6.470E+00,6.410E+00,6.350E+00,6.290E+00,6.230E+00,
6.170E+00,6.120E+00,6.060E+00,6.010E+00,5.960E+00,5.904E+00,5.850E+00,
5.806E+00,5.760E+00,5.710E+00,5.670E+00,5.624E+00,5.580E+00,5.540E+00,
5.490E+00,5.450E+00,5.413E+00,5.370E+00,5.340E+00,5.300E+00,5.260E+00,
5.230E+00,5.190E+00,5.160E+00,5.120E+00,5.090E+00,5.060E+00,5.030E+00,
5.000E+00,4.970E+00,4.940E+00]

pond_aerial_f2m = [1.266E+01,1.142E+01,1.050E+01,9.757E+00,9.147E+00,8.623E+00,8.146E+00,
7.698E+00,7.271E+00,6.871E+00,6.509E+00,6.188E+00,5.899E+00,5.635E+00,
5.388E+00,5.160E+00,4.953E+00,4.765E+00,4.594E+00,4.437E+00,4.291E+00,
4.154E+00,4.025E+00,3.903E+00,3.789E+00,3.682E+00,3.581E+00,3.488E+00,
3.403E+00,3.323E+00,3.245E+00,3.170E+00,3.097E+00,3.027E+00,2.961E+00,
2.898E+00,2.839E+00,2.783E+00,2.729E+00,2.677E+00,2.627E+00,2.579E+00,
2.533E+00,2.488E+00,2.446E+00,2.405E+00,2.366E+00,2.329E+00,2.292E+00,
2.258E+00,2.225E+00,2.193E+00,2.162E+00,2.132E+00,2.104E+00,2.076E+00,
2.049E+00,2.023E+00,1.998E+00,1.974E+00,1.950E+00,1.928E+00,1.905E+00,
1.884E+00,1.863E+00,1.842E+00,1.823E+00,1.804E+00,1.785E+00,1.767E+00,
1.749E+00,1.732E+00,1.715E+00,1.698E+00,1.683E+00,1.667E+00,1.652E+00,
1.637E+00,1.623E+00,1.608E+00,1.595E+00,1.581E+00,1.568E+00,1.555E+00,
1.543E+00,1.531E+00,1.519E+00,1.507E+00,1.496E+00,1.485E+00,1.474E+00,
1.464E+00,1.454E+00,1.444E+00,1.434E+00,1.425E+00,1.416E+00,1.407E+00,
1.398E+00,1.389E+00,1.381E+00]

pond_aerial_m2c = [8.918E+00,7.649E+00,6.759E+00,6.103E+00,5.593E+00,5.180E+00,4.829E+00,
4.513E+00,4.217E+00,3.934E+00,3.670E+00,3.437E+00,3.239E+00,3.070E+00,
2.920E+00,2.782E+00,2.654E+00,2.535E+00,2.426E+00,2.324E+00,2.232E+00,
2.149E+00,2.072E+00,2.001E+00,1.933E+00,1.869E+00,1.808E+00,1.750E+00,
1.696E+00,1.645E+00,1.598E+00,1.553E+00,1.511E+00,1.471E+00,1.434E+00,
1.399E+00,1.365E+00,1.334E+00,1.304E+00,1.276E+00,1.249E+00,1.223E+00,
1.198E+00,1.175E+00,1.153E+00,1.132E+00,1.113E+00,1.094E+00,1.076E+00,
1.058E+00,1.041E+00,1.026E+00,1.010E+00,9.957E-01,9.816E-01,9.681E-01,
9.551E-01,9.427E-01,9.307E-01,9.191E-01,9.080E-01,8.972E-01,8.868E-01,
8.768E-01,8.671E-01,8.578E-01,8.487E-01,8.399E-01,8.313E-01,8.231E-01,
8.151E-01,8.073E-01,7.998E-01,7.926E-01,7.855E-01,7.787E-01,7.720E-01,
7.655E-01,7.591E-01,7.529E-01,7.468E-01,7.409E-01,7.352E-01,7.296E-01,
7.242E-01,7.188E-01,7.136E-01,7.085E-01,7.035E-01,6.986E-01,6.939E-01,
6.892E-01,6.847E-01,6.802E-01,6.758E-01,6.716E-01,6.674E-01,6.633E-01,
6.593E-01,6.554E-01,6.516E-01]

pond_aerial_c2vc = [6.879E+00,5.622E+00,4.785E+00,4.190E+00,3.747E+00,3.401E+00,3.123E+00,
2.893E+00,2.692E+00,2.505E+00,2.331E+00,2.175E+00,2.043E+00,1.930E+00,
1.830E+00,1.738E+00,1.653E+00,1.574E+00,1.501E+00,1.434E+00,1.373E+00,
1.318E+00,1.268E+00,1.221E+00,1.178E+00,1.137E+00,1.099E+00,1.064E+00,
1.031E+00,1.000E+00,9.720E-01,9.456E-01,9.208E-01,8.977E-01,8.761E-01,
8.559E-01,8.369E-01,8.190E-01,8.020E-01,7.858E-01,7.705E-01,7.559E-01,
7.420E-01,7.287E-01,7.161E-01,7.039E-01,6.923E-01,6.811E-01,6.703E-01,
6.599E-01,6.497E-01,6.399E-01,6.304E-01,6.211E-01,6.121E-01,6.034E-01,
5.948E-01,5.865E-01,5.783E-01,5.703E-01,5.626E-01,5.550E-01,5.476E-01,
5.403E-01,5.332E-01,5.263E-01,5.194E-01,5.127E-01,5.062E-01,4.998E-01,
4.935E-01,4.874E-01,4.815E-01,4.756E-01,4.699E-01,4.643E-01,4.589E-01,
4.536E-01,4.484E-01,4.434E-01,4.384E-01,4.336E-01,4.290E-01,4.244E-01,
4.200E-01,4.157E-01,4.115E-01,4.075E-01,4.035E-01,3.997E-01,3.960E-01,
3.924E-01,3.889E-01,3.855E-01,3.822E-01,3.790E-01,3.759E-01,3.729E-01,
3.700E-01,3.671E-01,3.644E-01]

pond_ground_low_f = [2.681E+00,1.549E+00,1.250E+00,1.087E+00,9.800E-01,9.006E-01,8.380E-01,
7.864E-01,7.426E-01,7.047E-01,6.714E-01,6.417E-01,6.150E-01,5.908E-01,
5.687E-01,5.484E-01,5.296E-01,5.122E-01,4.960E-01,4.809E-01,4.667E-01,
4.534E-01,4.409E-01,4.290E-01,4.178E-01,4.072E-01,3.971E-01,3.875E-01,
3.783E-01,3.696E-01,3.613E-01,3.533E-01,3.456E-01,3.383E-01,3.313E-01,
3.246E-01,3.181E-01,3.118E-01,3.058E-01,3.000E-01,2.944E-01,2.890E-01,
2.838E-01,2.788E-01,2.739E-01,2.692E-01,2.646E-01,2.602E-01,2.559E-01,
2.517E-01,2.477E-01,2.438E-01,2.400E-01,2.363E-01,2.327E-01,2.292E-01,
2.258E-01,2.225E-01,2.193E-01,2.161E-01,2.131E-01,2.101E-01,2.072E-01,
2.043E-01,2.016E-01,1.989E-01,1.962E-01,1.937E-01,1.911E-01,1.887E-01,
1.863E-01,1.839E-01,1.816E-01,1.794E-01,1.772E-01,1.751E-01,1.730E-01,
1.709E-01,1.689E-01,1.669E-01,1.650E-01,1.631E-01,1.612E-01,1.594E-01,
1.576E-01,1.559E-01,1.542E-01,1.525E-01,1.508E-01,1.492E-01,1.476E-01,
1.461E-01,1.445E-01,1.430E-01,1.415E-01,1.401E-01,1.387E-01,1.373E-01,
1.359E-01,1.345E-01,1.332E-01]

pond_ground_high_fine = [6.164E+00,4.251E+00,3.425E+00,2.936E+00,2.607E+00,2.364E+00,2.173E+00,
 2.017E+00,1.886E+00,1.773E+00,1.674E+00,1.586E+00,1.508E+00,1.437E+00,
 1.372E+00,1.314E+00,1.260E+00,1.210E+00,1.163E+00,1.120E+00,1.080E+00,
1.042E+00,1.007E+00,9.740E-01,9.427E-01,9.132E-01,8.853E-01,8.588E-01,
 8.337E-01,8.099E-01,7.871E-01,7.655E-01,7.449E-01,7.251E-01,7.063E-01,
 6.882E-01,6.709E-01,6.544E-01,6.385E-01,6.232E-01,6.085E-01,5.944E-01,
 5.808E-01,5.677E-01,5.551E-01,5.429E-01,5.312E-01,5.198E-01,5.089E-01,
 4.983E-01,4.880E-01,4.781E-01,4.685E-01,4.592E-01,4.502E-01,4.415E-01,
 4.331E-01,4.249E-01,4.169E-01,4.092E-01,4.017E-01,3.944E-01,3.873E-01,
 3.804E-01,3.737E-01,3.672E-01,3.609E-01,3.547E-01,3.487E-01,3.428E-01,
 3.371E-01,3.316E-01,3.262E-01,3.209E-01,3.157E-01,3.107E-01,3.058E-01,
 3.010E-01,2.964E-01,2.918E-01,2.874E-01,2.830E-01,2.788E-01,2.746E-01,
 2.706E-01,2.666E-01,2.628E-01,2.590E-01,2.553E-01,2.516E-01,2.481E-01,
 2.446E-01,2.412E-01,2.379E-01,2.347E-01,2.315E-01,2.284E-01,2.253E-01,
 2.223E-01,2.194E-01,2.165E-01]
 
pond_ground_low_m2c = [1.090E+00,6.124E-01,5.272E-01,4.774E-01,4.422E-01,4.147E-01,3.922E-01,
3.730E-01,3.563E-01,3.416E-01,3.284E-01,3.165E-01,3.056E-01,2.956E-01,
2.863E-01,2.778E-01,2.698E-01,2.623E-01,2.553E-01,2.487E-01,2.425E-01,
2.366E-01,2.311E-01,2.258E-01,2.207E-01,2.159E-01,2.113E-01,2.069E-01,
2.027E-01,1.987E-01,1.948E-01,1.911E-01,1.876E-01,1.841E-01,1.808E-01,
1.776E-01,1.746E-01,1.716E-01,1.687E-01,1.659E-01,1.633E-01,1.607E-01,
1.581E-01,1.557E-01,1.533E-01,1.510E-01,1.488E-01,1.466E-01,1.445E-01,
1.425E-01,1.405E-01,1.385E-01,1.366E-01,1.348E-01,1.330E-01,1.312E-01,
1.295E-01,1.279E-01,1.263E-01,1.247E-01,1.231E-01,1.216E-01,1.201E-01,
1.187E-01,1.173E-01,1.159E-01,1.145E-01,1.132E-01,1.119E-01,1.107E-01,
1.094E-01,1.082E-01,1.070E-01,1.059E-01,1.047E-01,1.036E-01,1.025E-01,
1.014E-01,1.004E-01,9.935E-02,9.834E-02,9.734E-02,9.637E-02,9.541E-02,
9.447E-02,9.354E-02,9.263E-02,9.174E-02,9.087E-02,9.001E-02,8.916E-02,
8.833E-02,8.751E-02,8.671E-02,8.591E-02,8.514E-02,8.437E-02,8.362E-02,
8.288E-02,8.215E-02,8.143E-02]

pond_ground_high_m2c = [1.650E+00,9.842E-01,8.413E-01,7.572E-01,6.978E-01,6.515E-01,6.135E-01,
5.813E-01,5.534E-01,5.287E-01,5.067E-01,4.868E-01,4.686E-01,4.520E-01,
4.367E-01,4.225E-01,4.093E-01,3.970E-01,3.854E-01,3.745E-01,3.643E-01,
3.546E-01,3.454E-01,3.368E-01,3.285E-01,3.206E-01,3.131E-01,3.060E-01,
2.991E-01,2.926E-01,2.863E-01,2.803E-01,2.745E-01,2.689E-01,2.636E-01,
2.584E-01,2.535E-01,2.487E-01,2.440E-01,2.396E-01,2.353E-01,2.311E-01,
2.270E-01,2.231E-01,2.193E-01,2.157E-01,2.121E-01,2.086E-01,2.053E-01,
2.020E-01,1.988E-01,1.958E-01,1.928E-01,1.898E-01,1.870E-01,1.842E-01,
1.815E-01,1.789E-01,1.764E-01,1.739E-01,1.714E-01,1.690E-01,1.667E-01,
1.645E-01,1.623E-01,1.601E-01,1.580E-01,1.559E-01,1.539E-01,1.520E-01,
1.500E-01,1.481E-01,1.463E-01,1.445E-01,1.427E-01,1.410E-01,1.393E-01,
1.376E-01,1.360E-01,1.344E-01,1.329E-01,1.313E-01,1.298E-01,1.284E-01,
1.269E-01,1.255E-01,1.241E-01,1.227E-01,1.214E-01,1.201E-01,1.188E-01,
1.175E-01,1.163E-01,1.151E-01,1.139E-01,1.127E-01,1.115E-01,1.104E-01,
1.093E-01,1.082E-01,1.071E-01]

pond_vineyard = [2.433E-01,1.658E-01,1.274E-01,1.039E-01,8.835E-02,7.712E-02,6.860E-02,
6.188E-02,5.642E-02,5.188E-02,4.804E-02,4.474E-02,4.186E-02,3.933E-02,
3.709E-02,3.508E-02,3.327E-02,3.163E-02,3.014E-02,2.877E-02,2.752E-02,
2.636E-02,2.529E-02,2.429E-02,2.336E-02,2.250E-02,2.169E-02,2.093E-02,
2.021E-02,1.954E-02,1.891E-02,1.831E-02,1.774E-02,1.720E-02,1.669E-02,
1.621E-02,1.575E-02,1.531E-02,1.489E-02,1.449E-02,1.411E-02,1.375E-02,
1.340E-02,1.306E-02,1.274E-02,1.243E-02,1.214E-02,1.185E-02,1.158E-02,
1.132E-02,1.106E-02,1.082E-02,1.059E-02,1.036E-02,1.014E-02,9.928E-03,
9.724E-03,9.527E-03,9.336E-03,9.152E-03,8.973E-03,8.800E-03,8.632E-03,
8.470E-03,8.312E-03,8.160E-03,8.011E-03,7.868E-03,7.728E-03,7.592E-03,
7.460E-03,7.332E-03,7.207E-03,7.086E-03,6.968E-03,6.853E-03,6.742E-03,
6.633E-03,6.527E-03,6.423E-03,6.323E-03,6.224E-03,6.129E-03,6.035E-03,
5.944E-03,5.855E-03,5.769E-03,5.684E-03,5.601E-03,5.521E-03,5.442E-03,
5.365E-03,5.289E-03,5.215E-03,5.143E-03,5.073E-03,5.004E-03,4.937E-03,
4.871E-03,4.806E-03,4.743E-03]

pond_orchard =[2.180E+00,1.642E+00,1.301E+00,1.067E+00,8.998E-01,7.748E-01,6.784E-01,
6.021E-01,5.404E-01,4.896E-01,4.472E-01,4.112E-01,3.805E-01,3.539E-01,
3.307E-01,3.103E-01,2.922E-01,2.761E-01,2.617E-01,2.487E-01,2.369E-01,
2.262E-01,2.164E-01,2.075E-01,1.992E-01,1.916E-01,1.846E-01,1.781E-01,
1.720E-01,1.663E-01,1.610E-01,1.561E-01,1.514E-01,1.470E-01,1.429E-01,
1.389E-01,1.352E-01,1.317E-01,1.284E-01,1.252E-01,1.222E-01,1.194E-01,
1.166E-01,1.140E-01,1.115E-01,1.092E-01,1.069E-01,1.047E-01,1.026E-01,
1.005E-01,9.861E-02,9.674E-02,9.493E-02,9.320E-02,9.152E-02,8.991E-02,
8.835E-02,8.684E-02,8.538E-02,8.397E-02,8.261E-02,8.128E-02,8.000E-02,
7.876E-02,7.755E-02,7.638E-02,7.525E-02,7.414E-02,7.307E-02,7.202E-02,
7.101E-02,7.002E-02,6.906E-02,6.812E-02,6.721E-02,6.632E-02,6.545E-02,
6.461E-02,6.378E-02,6.297E-02,6.219E-02,6.142E-02,6.067E-02,5.994E-02,
5.922E-02,5.852E-02,5.784E-02,5.717E-02,5.651E-02,5.587E-02,5.524E-02,
5.463E-02,5.403E-02,5.344E-02,5.286E-02,5.229E-02,5.174E-02,5.119E-02,
5.066E-02,5.014E-02,4.962E-02]

lake_aerial_f2vf = [2.154E+01,2.066E+01,1.989E+01,1.920E+01,1.856E+01,1.796E+01,1.739E+01,
1.685E+01,1.634E+01,1.586E+01,1.540E+01,1.497E+01,1.455E+01,1.416E+01,
1.378E+01,1.343E+01,1.310E+01,1.278E+01,1.248E+01,1.219E+01,1.191E+01,
1.164E+01,1.139E+01,1.115E+01,1.092E+01,1.070E+01,1.050E+01,1.030E+01,
1.010E+01,9.919E+00,9.741E+00,9.571E+00,9.409E+00,9.254E+00,9.106E+00,
8.964E+00,8.825E+00,8.691E+00,8.562E+00,8.437E+00,8.316E+00,8.200E+00,
8.087E+00,7.978E+00,7.873E+00,7.771E+00,7.672E+00,7.575E+00,7.480E+00,
7.389E+00,7.301E+00,7.215E+00,7.132E+00,7.051E+00,6.972E+00,6.895E+00,
6.819E+00,6.745E+00,6.674E+00,6.606E+00,6.540E+00,6.476E+00,6.414E+00,
6.353E+00,6.292E+00,6.232E+00,6.174E+00,6.117E+00,6.062E+00,6.009E+00,
5.958E+00,5.907E+00,5.857E+00,5.808E+00,5.760E+00,5.712E+00,5.666E+00,
5.622E+00,5.579E+00,5.537E+00,5.496E+00,5.455E+00,5.415E+00,5.375E+00,
5.337E+00,5.299E+00,5.263E+00,5.228E+00,5.194E+00,5.160E+00,5.126E+00,
5.093E+00,5.060E+00,5.028E+00,4.997E+00,4.967E+00,4.938E+00,4.910E+00,
4.882E+00,4.854E+00,4.826E+00]

lake_aerial_f2m = [1.071E+01,9.723E+00,8.981E+00,8.384E+00,7.891E+00,7.465E+00,7.077E+00,
6.712E+00,6.364E+00,6.037E+00,5.741E+00,5.476E+00,5.237E+00,5.018E+00,
4.814E+00,4.624E+00,4.451E+00,4.294E+00,4.150E+00,4.018E+00,3.895E+00,
3.779E+00,3.670E+00,3.567E+00,3.470E+00,3.378E+00,3.293E+00,3.213E+00,
3.139E+00,3.070E+00,3.003E+00,2.938E+00,2.875E+00,2.815E+00,2.758E+00,
2.703E+00,2.652E+00,2.603E+00,2.556E+00,2.511E+00,2.467E+00,2.425E+00,
2.385E+00,2.346E+00,2.308E+00,2.272E+00,2.238E+00,2.205E+00,2.173E+00,
2.142E+00,2.113E+00,2.084E+00,2.057E+00,2.030E+00,2.004E+00,1.979E+00,
1.955E+00,1.932E+00,1.909E+00,1.887E+00,1.866E+00,1.846E+00,1.826E+00,
1.806E+00,1.787E+00,1.769E+00,1.751E+00,1.733E+00,1.716E+00,1.700E+00,
1.684E+00,1.668E+00,1.653E+00,1.638E+00,1.624E+00,1.610E+00,1.596E+00,
1.582E+00,1.569E+00,1.557E+00,1.544E+00,1.532E+00,1.520E+00,1.509E+00,
1.497E+00,1.486E+00,1.476E+00,1.465E+00,1.455E+00,1.445E+00,1.435E+00,
1.426E+00,1.416E+00,1.407E+00,1.398E+00,1.390E+00,1.381E+00,1.373E+00,
1.365E+00,1.357E+00,1.350E+00]

lake_aerial_m2c = [7.368E+00,6.369E+00,5.663E+00,5.141E+00,4.733E+00,4.401E+00,4.117E+00,
3.861E+00,3.622E+00,3.394E+00,3.180E+00,2.991E+00,2.829E+00,2.691E+00,
2.568E+00,2.454E+00,2.348E+00,2.250E+00,2.159E+00,2.075E+00,1.999E+00,
1.929E+00,1.865E+00,1.805E+00,1.748E+00,1.695E+00,1.643E+00,1.595E+00,
1.549E+00,1.506E+00,1.466E+00,1.428E+00,1.393E+00,1.359E+00,1.327E+00,
1.296E+00,1.268E+00,1.241E+00,1.215E+00,1.191E+00,1.168E+00,1.146E+00,
1.125E+00,1.105E+00,1.085E+00,1.067E+00,1.050E+00,1.034E+00,1.018E+00,
1.003E+00,9.881E-01,9.741E-01,9.607E-01,9.478E-01,9.354E-01,9.235E-01,
9.120E-01,9.009E-01,8.902E-01,8.799E-01,8.700E-01,8.604E-01,8.511E-01,
8.421E-01,8.334E-01,8.249E-01,8.167E-01,8.088E-01,8.011E-01,7.936E-01,
7.864E-01,7.794E-01,7.726E-01,7.660E-01,7.596E-01,7.534E-01,7.473E-01,
7.414E-01,7.356E-01,7.299E-01,7.244E-01,7.190E-01,7.138E-01,7.087E-01,
7.037E-01,6.988E-01,6.940E-01,6.893E-01,6.848E-01,6.803E-01,6.759E-01,
6.716E-01,6.674E-01,6.633E-01,6.593E-01,6.554E-01,6.515E-01,6.477E-01,
6.440E-01,6.404E-01,6.368E-01]

lake_aerial_c2vc = [5.606E+00,4.622E+00,3.964E+00,3.495E+00,3.144E+00,2.868E+00,2.646E+00,
2.462E+00,2.300E+00,2.150E+00,2.010E+00,1.885E+00,1.778E+00,1.686E+00,
1.605E+00,1.530E+00,1.461E+00,1.396E+00,1.337E+00,1.281E+00,1.231E+00,
1.186E+00,1.144E+00,1.106E+00,1.069E+00,1.036E+00,1.004E+00,9.742E-01,
9.465E-01,9.206E-01,8.965E-01,8.740E-01,8.528E-01,8.330E-01,8.143E-01,
7.967E-01,7.802E-01,7.645E-01,7.495E-01,7.353E-01,7.217E-01,7.087E-01,
6.963E-01,6.845E-01,6.731E-01,6.622E-01,6.516E-01,6.415E-01,6.317E-01,
6.221E-01,6.129E-01,6.039E-01,5.952E-01,5.867E-01,5.784E-01,5.704E-01,
5.625E-01,5.549E-01,5.474E-01,5.401E-01,5.330E-01,5.261E-01,5.193E-01,
5.127E-01,5.062E-01,4.999E-01,4.937E-01,4.876E-01,4.817E-01,4.759E-01,
4.703E-01,4.648E-01,4.594E-01,4.541E-01,4.490E-01,4.440E-01,4.392E-01,
4.344E-01,4.298E-01,4.253E-01,4.209E-01,4.166E-01,4.124E-01,4.084E-01,
4.045E-01,4.006E-01,3.969E-01,3.932E-01,3.897E-01,3.863E-01,3.830E-01,
3.797E-01,3.766E-01,3.735E-01,3.706E-01,3.677E-01,3.649E-01,3.621E-01,
3.595E-01,3.569E-01,3.544E-01]

lake_ground_low_f = [2.721E+00,1.312E+00,1.063E+00,9.340E-01,8.487E-01,7.851E-01,7.345E-01,
6.926E-01,6.569E-01,6.258E-01,5.983E-01,5.737E-01,5.514E-01,5.312E-01,
5.126E-01,4.955E-01,4.796E-01,4.648E-01,4.510E-01,4.381E-01,4.260E-01,
4.145E-01,4.037E-01,3.935E-01,3.838E-01,3.745E-01,3.657E-01,3.574E-01,
3.494E-01,3.417E-01,3.344E-01,3.274E-01,3.207E-01,3.142E-01,3.080E-01,
3.020E-01,2.963E-01,2.907E-01,2.854E-01,2.802E-01,2.752E-01,2.704E-01,
2.657E-01,2.612E-01,2.568E-01,2.526E-01,2.485E-01,2.445E-01,2.406E-01,
2.369E-01,2.332E-01,2.297E-01,2.262E-01,2.229E-01,2.196E-01,2.164E-01,
2.133E-01,2.103E-01,2.074E-01,2.045E-01,2.017E-01,1.990E-01,1.963E-01,
1.938E-01,1.912E-01,1.887E-01,1.863E-01,1.840E-01,1.817E-01,1.794E-01,
1.772E-01,1.750E-01,1.729E-01,1.708E-01,1.688E-01,1.668E-01,1.649E-01,
1.630E-01,1.611E-01,1.593E-01,1.575E-01,1.558E-01,1.540E-01,1.523E-01,
1.507E-01,1.491E-01,1.475E-01,1.459E-01,1.444E-01,1.429E-01,1.414E-01,
1.399E-01,1.385E-01,1.371E-01,1.357E-01,1.344E-01,1.330E-01,1.317E-01,
1.305E-01,1.292E-01,1.279E-01]

lake_ground_high_f = [5.254E+00,3.538E+00,2.865E+00,2.479E+00,2.218E+00,2.024E+00,1.871E+00,
1.745E+00,1.638E+00,1.546E+00,1.465E+00,1.392E+00,1.328E+00,1.269E+00,
1.215E+00,1.166E+00,1.120E+00,1.078E+00,1.039E+00,1.003E+00,9.684E-01,
9.363E-01,9.062E-01,8.778E-01,8.509E-01,8.255E-01,8.014E-01,7.785E-01,
7.568E-01,7.360E-01,7.163E-01,6.974E-01,6.794E-01,6.622E-01,6.456E-01,
6.298E-01,6.146E-01,6.000E-01,5.860E-01,5.725E-01,5.596E-01,5.471E-01,
5.350E-01,5.234E-01,5.122E-01,5.013E-01,4.909E-01,4.808E-01,4.710E-01,
4.615E-01,4.524E-01,4.435E-01,4.349E-01,4.265E-01,4.185E-01,4.106E-01,
4.030E-01,3.956E-01,3.884E-01,3.815E-01,3.747E-01,3.681E-01,3.617E-01,
3.554E-01,3.494E-01,3.435E-01,3.377E-01,3.321E-01,3.266E-01,3.213E-01,
3.161E-01,3.111E-01,3.061E-01,3.013E-01,2.966E-01,2.920E-01,2.876E-01,
2.832E-01,2.789E-01,2.748E-01,2.707E-01,2.667E-01,2.628E-01,2.590E-01,
2.553E-01,2.516E-01,2.481E-01,2.446E-01,2.412E-01,2.379E-01,2.346E-01,
2.314E-01,2.283E-01,2.252E-01,2.222E-01,2.193E-01,2.164E-01,2.136E-01,
2.108E-01,2.081E-01,2.054E-01]

lake_ground_low_m2c = [1.804E+00,5.296E-01,4.582E-01,4.186E-01,3.903E-01,3.681E-01,3.497E-01,
3.339E-01,3.201E-01,3.079E-01,2.969E-01,2.869E-01,2.777E-01,2.693E-01,
2.614E-01,2.541E-01,2.473E-01,2.409E-01,2.349E-01,2.292E-01,2.238E-01,
2.187E-01,2.138E-01,2.092E-01,2.048E-01,2.006E-01,1.965E-01,1.927E-01,
1.890E-01,1.854E-01,1.820E-01,1.787E-01,1.755E-01,1.725E-01,1.695E-01,
1.667E-01,1.639E-01,1.613E-01,1.587E-01,1.562E-01,1.538E-01,1.514E-01,
1.492E-01,1.470E-01,1.448E-01,1.427E-01,1.407E-01,1.388E-01,1.368E-01,
1.350E-01,1.332E-01,1.314E-01,1.297E-01,1.280E-01,1.263E-01,1.247E-01,
1.232E-01,1.217E-01,1.202E-01,1.187E-01,1.173E-01,1.159E-01,1.145E-01,
1.132E-01,1.119E-01,1.106E-01,1.094E-01,1.082E-01,1.070E-01,1.058E-01,
1.047E-01,1.035E-01,1.024E-01,1.014E-01,1.003E-01,9.927E-02,9.826E-02,
9.726E-02,9.628E-02,9.532E-02,9.437E-02,9.344E-02,9.253E-02,9.164E-02,
9.076E-02,8.990E-02,8.905E-02,8.822E-02,8.740E-02,8.659E-02,8.580E-02,
8.502E-02,8.426E-02,8.351E-02,8.277E-02,8.204E-02,8.132E-02,8.061E-02,
7.992E-02,7.923E-02,7.856E-02]

lake_ground_high_m2c = [2.156E+00,8.452E-01,7.259E-01,6.590E-01,6.113E-01,5.739E-01,5.429E-01,
5.165E-01,4.935E-01,4.730E-01,4.547E-01,4.380E-01,4.228E-01,4.088E-01,
3.958E-01,3.837E-01,3.725E-01,3.619E-01,3.520E-01,3.426E-01,3.338E-01,
3.254E-01,3.174E-01,3.099E-01,3.027E-01,2.958E-01,2.892E-01,2.830E-01,
2.769E-01,2.712E-01,2.656E-01,2.603E-01,2.552E-01,2.502E-01,2.455E-01,
2.409E-01,2.365E-01,2.322E-01,2.281E-01,2.241E-01,2.202E-01,2.164E-01,
2.128E-01,2.093E-01,2.059E-01,2.026E-01,1.993E-01,1.962E-01,1.932E-01,
1.902E-01,1.873E-01,1.845E-01,1.818E-01,1.791E-01,1.766E-01,1.740E-01,
1.716E-01,1.692E-01,1.669E-01,1.646E-01,1.623E-01,1.602E-01,1.580E-01,
1.560E-01,1.539E-01,1.520E-01,1.500E-01,1.481E-01,1.463E-01,1.445E-01,
1.427E-01,1.409E-01,1.392E-01,1.376E-01,1.359E-01,1.343E-01,1.328E-01,
1.312E-01,1.297E-01,1.283E-01,1.268E-01,1.254E-01,1.240E-01,1.226E-01,
1.213E-01,1.200E-01,1.187E-01,1.174E-01,1.162E-01,1.149E-01,1.137E-01,
1.126E-01,1.114E-01,1.103E-01,1.091E-01,1.080E-01,1.070E-01,1.059E-01,
1.048E-01,1.038E-01,1.028E-01]

lake_vineyard = [2.003E-01,1.348E-01,1.039E-01,8.554E-02,7.328E-02,6.441E-02,5.766E-02,
5.231E-02,4.794E-02,4.429E-02,4.120E-02,3.852E-02,3.618E-02,3.412E-02,
3.228E-02,3.063E-02,2.913E-02,2.778E-02,2.653E-02,2.540E-02,2.434E-02,
2.337E-02,2.247E-02,2.163E-02,2.085E-02,2.011E-02,1.943E-02,1.878E-02,
1.817E-02,1.759E-02,1.705E-02,1.653E-02,1.605E-02,1.558E-02,1.514E-02,
1.472E-02,1.432E-02,1.394E-02,1.358E-02,1.323E-02,1.289E-02,1.257E-02,
1.227E-02,1.197E-02,1.169E-02,1.142E-02,1.116E-02,1.091E-02,1.067E-02,
1.044E-02,1.021E-02,9.995E-03,9.786E-03,9.584E-03,9.390E-03,9.201E-03,
9.019E-03,8.843E-03,8.672E-03,8.507E-03,8.347E-03,8.191E-03,8.041E-03,
7.895E-03,7.753E-03,7.615E-03,7.482E-03,7.352E-03,7.226E-03,7.103E-03,
6.984E-03,6.868E-03,6.755E-03,6.645E-03,6.538E-03,6.433E-03,6.332E-03,
6.233E-03,6.136E-03,6.042E-03,5.950E-03,5.861E-03,5.773E-03,5.688E-03,
5.605E-03,5.523E-03,5.444E-03,5.366E-03,5.291E-03,5.216E-03,5.144E-03,
5.073E-03,5.004E-03,4.936E-03,4.870E-03,4.805E-03,4.742E-03,4.680E-03,
4.619E-03,4.559E-03,4.501E-03]

lake_orchard = [1.753E+00,1.322E+00,1.052E+00,8.692E-01,7.380E-01,6.398E-01,5.638E-01,
5.035E-01,4.545E-01,4.141E-01,3.802E-01,3.515E-01,3.267E-01,3.053E-01,
2.865E-01,2.700E-01,2.552E-01,2.421E-01,2.303E-01,2.196E-01,2.098E-01,
2.010E-01,1.929E-01,1.854E-01,1.785E-01,1.721E-01,1.662E-01,1.607E-01,
1.556E-01,1.508E-01,1.463E-01,1.420E-01,1.380E-01,1.343E-01,1.307E-01,
1.273E-01,1.241E-01,1.211E-01,1.182E-01,1.155E-01,1.129E-01,1.104E-01,
1.080E-01,1.057E-01,1.035E-01,1.014E-01,9.939E-02,9.746E-02,9.560E-02,
9.381E-02,9.208E-02,9.042E-02,8.882E-02,8.727E-02,8.578E-02,8.434E-02,
8.294E-02,8.159E-02,8.028E-02,7.902E-02,7.779E-02,7.660E-02,7.544E-02,
7.432E-02,7.323E-02,7.217E-02,7.114E-02,7.014E-02,6.917E-02,6.822E-02,
6.729E-02,6.639E-02,6.552E-02,6.466E-02,6.383E-02,6.302E-02,6.222E-02,
6.145E-02,6.069E-02,5.995E-02,5.923E-02,5.853E-02,5.784E-02,5.716E-02,
5.650E-02,5.586E-02,5.523E-02,5.461E-02,5.400E-02,5.341E-02,5.283E-02,
5.226E-02,5.170E-02,5.116E-02,5.062E-02,5.010E-02,4.958E-02,4.908E-02,
4.858E-02,4.810E-02,4.762E-02]

stream_aerial_f2vf = [3.773E+01,3.564E+01,3.407E+01,3.271E+01,3.130E+01,2.988E+01,2.860E+01,
2.753E+01,2.656E+01,2.558E+01,2.459E+01,2.362E+01,2.270E+01,2.185E+01,
2.109E+01,2.040E+01,1.977E+01,1.913E+01,1.850E+01,1.790E+01,1.733E+01,
1.678E+01,1.624E+01,1.576E+01,1.535E+01,1.500E+01,1.463E+01,1.423E+01,
1.382E+01,1.344E+01,1.309E+01,1.278E+01,1.249E+01,1.223E+01,1.197E+01,
1.174E+01,1.150E+01,1.127E+01,1.106E+01,1.085E+01,1.062E+01,1.041E+01,
1.022E+01,1.006E+01,9.910E+00,9.762E+00,9.606E+00,9.447E+00,9.284E+00,
9.125E+00,8.981E+00,8.852E+00,8.736E+00,8.620E+00,8.492E+00,8.353E+00,
8.218E+00,8.097E+00,7.988E+00,7.886E+00,7.790E+00,7.707E+00,7.631E+00,
7.545E+00,7.445E+00,7.343E+00,7.250E+00,7.169E+00,7.092E+00,7.018E+00,
6.951E+00,6.888E+00,6.816E+00,6.732E+00,6.647E+00,6.573E+00,6.517E+00,
6.467E+00,6.415E+00,6.360E+00,6.304E+00,6.240E+00,6.166E+00,6.092E+00,
6.032E+00,5.992E+00,5.958E+00,5.917E+00,5.872E+00,5.825E+00,5.773E+00,
5.712E+00,5.648E+00,5.593E+00,5.555E+00,5.527E+00,5.498E+00,5.467E+00,
5.436E+00,5.399E+00,5.350E+00]

stream_aerial_f2m = [2.559E+01,2.201E+01,1.978E+01,1.848E+01,1.760E+01,1.674E+01,1.562E+01,
1.430E+01,1.304E+01,1.205E+01,1.131E+01,1.067E+01,9.971E+00,9.259E+00,
8.626E+00,8.076E+00,7.607E+00,7.229E+00,6.917E+00,6.628E+00,6.349E+00,
6.076E+00,5.801E+00,5.531E+00,5.260E+00,5.021E+00,4.855E+00,4.740E+00,
4.633E+00,4.515E+00,4.381E+00,4.233E+00,4.086E+00,3.954E+00,3.843E+00,
3.750E+00,3.664E+00,3.579E+00,3.493E+00,3.408E+00,3.327E+00,3.250E+00,
3.175E+00,3.102E+00,3.033E+00,2.966E+00,2.901E+00,2.840E+00,2.783E+00,
2.729E+00,2.678E+00,2.630E+00,2.583E+00,2.538E+00,2.495E+00,2.453E+00,
2.413E+00,2.375E+00,2.339E+00,2.305E+00,2.272E+00,2.239E+00,2.207E+00,
2.176E+00,2.146E+00,2.117E+00,2.089E+00,2.063E+00,2.038E+00,2.013E+00,
1.989E+00,1.965E+00,1.942E+00,1.921E+00,1.900E+00,1.879E+00,1.859E+00,
1.840E+00,1.820E+00,1.801E+00,1.783E+00,1.764E+00,1.747E+00,1.730E+00,
1.713E+00,1.697E+00,1.682E+00,1.666E+00,1.651E+00,1.635E+00,1.621E+00,
1.606E+00,1.592E+00,1.579E+00,1.566E+00,1.554E+00,1.541E+00,1.529E+00,
1.517E+00,1.505E+00,1.493E+00]

stream_aerial_m2c = [2.065E+01,1.670E+01,1.411E+01,1.252E+01,1.157E+01,1.098E+01,1.042E+01,
9.584E+00,8.489E+00,7.422E+00,6.605E+00,6.077E+00,5.702E+00,5.356E+00,
5.019E+00,4.712E+00,4.403E+00,4.087E+00,3.819E+00,3.610E+00,3.439E+00,
3.296E+00,3.170E+00,3.051E+00,2.924E+00,2.785E+00,2.652E+00,2.541E+00,
2.443E+00,2.352E+00,2.264E+00,2.177E+00,2.095E+00,2.019E+00,1.951E+00,
1.888E+00,1.829E+00,1.773E+00,1.720E+00,1.670E+00,1.621E+00,1.574E+00,
1.530E+00,1.491E+00,1.454E+00,1.420E+00,1.387E+00,1.356E+00,1.326E+00,
1.297E+00,1.270E+00,1.245E+00,1.221E+00,1.198E+00,1.175E+00,1.154E+00,
1.134E+00,1.114E+00,1.095E+00,1.078E+00,1.061E+00,1.045E+00,1.030E+00,
1.015E+00,1.000E+00,9.863E-01,9.725E-01,9.591E-01,9.461E-01,9.337E-01,
9.221E-01,9.112E-01,9.007E-01,8.907E-01,8.812E-01,8.721E-01,8.630E-01,
8.538E-01,8.448E-01,8.363E-01,8.282E-01,8.205E-01,8.131E-01,8.059E-01,
7.987E-01,7.916E-01,7.847E-01,7.779E-01,7.713E-01,7.649E-01,7.586E-01,
7.525E-01,7.465E-01,7.406E-01,7.349E-01,7.293E-01,7.238E-01,7.183E-01,
7.130E-01,7.079E-01,7.028E-01]

stream_aerial_c2vc = [1.776E+01,1.378E+01,1.111E+01,9.208E+00,7.952E+00,7.244E+00,6.783E+00,
6.254E+00,5.559E+00,4.856E+00,4.321E+00,3.955E+00,3.694E+00,3.480E+00,
3.273E+00,3.064E+00,2.854E+00,2.644E+00,2.458E+00,2.313E+00,2.194E+00,
2.085E+00,1.983E+00,1.888E+00,1.798E+00,1.710E+00,1.627E+00,1.551E+00,
1.482E+00,1.419E+00,1.360E+00,1.306E+00,1.256E+00,1.210E+00,1.169E+00,
1.132E+00,1.097E+00,1.064E+00,1.033E+00,1.004E+00,9.771E-01,9.512E-01,
9.271E-01,9.051E-01,8.851E-01,8.665E-01,8.488E-01,8.317E-01,8.154E-01,
7.999E-01,7.853E-01,7.714E-01,7.581E-01,7.454E-01,7.330E-01,7.210E-01,
7.092E-01,6.976E-01,6.867E-01,6.763E-01,6.664E-01,6.569E-01,6.477E-01,
6.387E-01,6.299E-01,6.210E-01,6.120E-01,6.032E-01,5.947E-01,5.865E-01,
5.785E-01,5.707E-01,5.631E-01,5.557E-01,5.483E-01,5.410E-01,5.338E-01,
5.268E-01,5.199E-01,5.131E-01,5.066E-01,5.002E-01,4.939E-01,4.877E-01,
4.815E-01,4.754E-01,4.694E-01,4.636E-01,4.580E-01,4.525E-01,4.472E-01,
4.421E-01,4.371E-01,4.322E-01,4.275E-01,4.229E-01,4.184E-01,4.140E-01,
4.098E-01,4.058E-01,4.019E-01]

stream_ground_low_fine = [4.747E+00,3.408E+00,2.688E+00,2.236E+00,1.926E+00,1.697E+00,1.522E+00,
1.383E+00,1.269E+00,1.174E+00,1.093E+00,1.024E+00,9.630E-01,9.096E-01,
8.622E-01,8.198E-01,7.815E-01,7.468E-01,7.151E-01,6.861E-01,6.595E-01,
6.348E-01,6.120E-01,5.908E-01,5.710E-01,5.525E-01,5.352E-01,5.189E-01,
5.036E-01,4.891E-01,4.754E-01,4.625E-01,4.502E-01,4.385E-01,4.275E-01,
4.169E-01,4.068E-01,3.972E-01,3.880E-01,3.792E-01,3.708E-01,3.627E-01,
3.550E-01,3.476E-01,3.404E-01,3.335E-01,3.269E-01,3.205E-01,3.143E-01,
3.084E-01,3.027E-01,2.971E-01,2.918E-01,2.866E-01,2.816E-01,2.767E-01,
2.720E-01,2.674E-01,2.630E-01,2.587E-01,2.545E-01,2.505E-01,2.466E-01,
2.427E-01,2.390E-01,2.354E-01,2.319E-01,2.285E-01,2.251E-01,2.219E-01,
2.187E-01,2.156E-01,2.126E-01,2.097E-01,2.068E-01,2.040E-01,2.013E-01,
1.986E-01,1.960E-01,1.935E-01,1.910E-01,1.886E-01,1.862E-01,1.839E-01,
1.816E-01,1.794E-01,1.772E-01,1.751E-01,1.730E-01,1.710E-01,1.690E-01,
1.670E-01,1.651E-01,1.632E-01,1.614E-01,1.595E-01,1.578E-01,1.560E-01,
1.543E-01,1.527E-01,1.510E-01]

stream_ground_high_fine= [1.406E+01,1.010E+01,7.862E+00,6.451E+00,5.483E+00,4.775E+00,4.234E+00,
3.805E+00,3.456E+00,3.166E+00,2.921E+00,2.710E+00,2.528E+00,2.367E+00,
2.226E+00,2.099E+00,1.986E+00,1.883E+00,1.790E+00,1.705E+00,1.627E+00,
1.555E+00,1.489E+00,1.428E+00,1.371E+00,1.318E+00,1.268E+00,1.222E+00,
1.178E+00,1.138E+00,1.099E+00,1.063E+00,1.028E+00,9.960E-01,9.653E-01,
9.361E-01,9.083E-01,8.819E-01,8.568E-01,8.328E-01,8.100E-01,7.881E-01,
7.672E-01,7.472E-01,7.280E-01,7.096E-01,6.920E-01,6.751E-01,6.588E-01,
6.431E-01,6.281E-01,6.136E-01,5.996E-01,5.861E-01,5.731E-01,5.606E-01,
5.485E-01,5.368E-01,5.255E-01,5.145E-01,5.040E-01,4.937E-01,4.838E-01,
4.742E-01,4.649E-01,4.558E-01,4.471E-01,4.386E-01,4.303E-01,4.223E-01,
4.145E-01,4.070E-01,3.996E-01,3.925E-01,3.856E-01,3.788E-01,3.722E-01,
3.658E-01,3.596E-01,3.535E-01,3.476E-01,3.418E-01,3.362E-01,3.307E-01,
3.254E-01,3.202E-01,3.151E-01,3.101E-01,3.053E-01,3.006E-01,2.960E-01,
2.915E-01,2.871E-01,2.828E-01,2.786E-01,2.744E-01,2.704E-01,2.665E-01,
2.627E-01,2.589E-01,2.552E-01]

stream_ground_low_m2c = [1.589E+00,1.228E+00,1.022E+00,8.860E-01,7.875E-01,7.124E-01,6.528E-01,
6.041E-01,5.634E-01,5.287E-01,4.988E-01,4.725E-01,4.493E-01,4.285E-01,
4.098E-01,3.929E-01,3.775E-01,3.634E-01,3.504E-01,3.384E-01,3.272E-01,
3.169E-01,3.072E-01,2.981E-01,2.896E-01,2.816E-01,2.740E-01,2.669E-01,
2.601E-01,2.537E-01,2.476E-01,2.418E-01,2.363E-01,2.310E-01,2.260E-01,
2.212E-01,2.165E-01,2.121E-01,2.079E-01,2.038E-01,1.999E-01,1.961E-01,
1.925E-01,1.890E-01,1.856E-01,1.823E-01,1.792E-01,1.761E-01,1.732E-01,
1.703E-01,1.675E-01,1.649E-01,1.623E-01,1.598E-01,1.573E-01,1.549E-01,
1.526E-01,1.504E-01,1.482E-01,1.461E-01,1.440E-01,1.420E-01,1.401E-01,
1.382E-01,1.363E-01,1.345E-01,1.328E-01,1.310E-01,1.294E-01,1.277E-01,
1.261E-01,1.246E-01,1.230E-01,1.215E-01,1.201E-01,1.186E-01,1.173E-01,
1.159E-01,1.146E-01,1.132E-01,1.120E-01,1.107E-01,1.095E-01,1.083E-01,
1.071E-01,1.059E-01,1.048E-01,1.037E-01,1.026E-01,1.015E-01,1.005E-01,
9.947E-02,9.846E-02,9.747E-02,9.650E-02,9.554E-02,9.460E-02,9.368E-02,
9.278E-02,9.189E-02,9.102E-02]

stream_ground_high_m2c = [637E+00,2.028E+00,1.678E+00,1.447E+00,1.279E+00,1.152E+00,1.051E+00,
9.688E-01,9.000E-01,8.415E-01,7.910E-01,7.469E-01,7.078E-01,6.730E-01,
6.417E-01,6.134E-01,5.876E-01,5.641E-01,5.424E-01,5.224E-01,5.039E-01,
4.866E-01,4.706E-01,4.555E-01,4.414E-01,4.282E-01,4.157E-01,4.039E-01,
3.928E-01,3.822E-01,3.722E-01,3.627E-01,3.536E-01,3.450E-01,3.367E-01,
3.289E-01,3.213E-01,3.141E-01,3.072E-01,3.006E-01,2.942E-01,2.881E-01,
2.822E-01,2.765E-01,2.710E-01,2.657E-01,2.606E-01,2.557E-01,2.510E-01,
2.464E-01,2.420E-01,2.377E-01,2.335E-01,2.295E-01,2.255E-01,2.218E-01,
2.181E-01,2.145E-01,2.110E-01,2.077E-01,2.044E-01,2.012E-01,1.981E-01,
1.951E-01,1.921E-01,1.893E-01,1.865E-01,1.838E-01,1.811E-01,1.785E-01,
1.760E-01,1.736E-01,1.712E-01,1.688E-01,1.665E-01,1.643E-01,1.621E-01,
1.600E-01,1.579E-01,1.559E-01,1.539E-01,1.519E-01,1.500E-01,1.482E-01,
1.463E-01,1.445E-01,1.428E-01,1.411E-01,1.394E-01,1.377E-01,1.361E-01,
1.345E-01,1.330E-01,1.315E-01,1.300E-01,1.285E-01,1.271E-01,1.257E-01,
1.243E-01,1.229E-01,1.216E-01]

stream_vineyard = [6.461E-01,4.514E-01,3.379E-01,2.654E-01,2.159E-01,1.804E-01,1.540E-01,
1.337E-01,1.177E-01,1.048E-01,9.421E-02,8.539E-02,7.795E-02,7.158E-02,
6.609E-02,6.131E-02,5.711E-02,5.339E-02,5.008E-02,4.712E-02,4.445E-02,
4.204E-02,3.985E-02,3.784E-02,3.601E-02,3.433E-02,3.277E-02,3.134E-02,
3.001E-02,2.877E-02,2.762E-02,2.654E-02,2.554E-02,2.459E-02,2.371E-02,
2.288E-02,2.209E-02,2.135E-02,2.065E-02,1.999E-02,1.936E-02,1.877E-02,
1.820E-02,1.766E-02,1.715E-02,1.666E-02,1.620E-02,1.575E-02,1.533E-02,
1.492E-02,1.454E-02,1.416E-02,1.381E-02,1.347E-02,1.314E-02,1.282E-02,
1.252E-02,1.223E-02,1.195E-02,1.168E-02,1.142E-02,1.116E-02,1.092E-02,
1.069E-02,1.046E-02,1.024E-02,1.003E-02,9.830E-03,9.632E-03,9.441E-03,
9.257E-03,9.078E-03,8.904E-03,8.736E-03,8.573E-03,8.414E-03,8.261E-03,
8.112E-03,7.967E-03,7.826E-03,7.689E-03,7.556E-03,7.427E-03,7.301E-03,
7.179E-03,7.060E-03,6.944E-03,6.831E-03,6.721E-03,6.614E-03,6.510E-03,
6.408E-03,6.308E-03,6.212E-03,6.117E-03,6.025E-03,5.935E-03,5.847E-03,
5.761E-03,5.678E-03,5.596E-03]

stream_orchard = [6.599E+00,4.859E+00,3.721E+00,2.940E+00,2.382E+00,1.970E+00,1.658E+00,
1.416E+00,1.225E+00,1.072E+00,9.469E-01,8.440E-01,7.581E-01,6.858E-01,
6.243E-01,5.715E-01,5.258E-01,4.861E-01,4.513E-01,4.207E-01,3.935E-01,
3.693E-01,3.477E-01,3.282E-01,3.106E-01,2.947E-01,2.802E-01,2.670E-01,
2.549E-01,2.438E-01,2.335E-01,2.241E-01,2.153E-01,2.072E-01,1.996E-01,
1.926E-01,1.860E-01,1.798E-01,1.741E-01,1.686E-01,1.635E-01,1.587E-01,
1.541E-01,1.498E-01,1.458E-01,1.419E-01,1.382E-01,1.347E-01,1.314E-01,
1.282E-01,1.252E-01,1.223E-01,1.196E-01,1.169E-01,1.144E-01,1.120E-01,
1.097E-01,1.074E-01,1.053E-01,1.032E-01,1.012E-01,9.931E-02,9.747E-02,
9.569E-02,9.397E-02,9.231E-02,9.071E-02,8.916E-02,8.765E-02,8.620E-02,
8.480E-02,8.343E-02,8.211E-02,8.083E-02,7.958E-02,7.837E-02,7.720E-02,
7.606E-02,7.495E-02,7.387E-02,7.282E-02,7.180E-02,7.081E-02,6.984E-02,
6.890E-02,6.798E-02,6.708E-02,6.620E-02,6.535E-02,6.452E-02,6.370E-02,
6.291E-02,6.213E-02,6.138E-02,6.063E-02,5.991E-02,5.920E-02,5.851E-02,
5.783E-02,5.717E-02,5.652E-02]

y = []

class agdriftOutputPage(webapp.RequestHandler):
    def post(self):        
        form = cgi.FieldStorage()   
        drop_size = form.getvalue('drop_size')
        waterbody_type = form.getvalue('waterbody_type')
        application_method = form.getvalue('application_method')
        boom_height = form.getvalue('boom_height')
        print "drop_size", drop_size
        print "waterbody_type", waterbody_type
        print "application_method", application_method
        print "boom_height", boom_height

        
        orchard_type = form.getvalue('orchard_type')
        if (waterbody_type == '1' and application_method == 'a' and drop_size == '1'):
            y = pond_aerial_vf2f
        elif (waterbody_type == '1' and application_method == 'a' and drop_size == '2'):
            y = pond_aerial_f2m
        elif (waterbody_type == '1' and application_method == 'a' and drop_size == '3'):
            y = pond_aerial_m2c
        elif (waterbody_type == '1' and application_method == 'a' and drop_size == '4'):
            y = pond_aerial_c2vc
        elif (waterbody_type == '1' and application_method == 'b' and drop_size == '1' and boom_height == '1'):
            y = pond_ground_low_f
        elif (waterbody_type == '1' and application_method == 'b' and drop_size == '1' and boom_height == '2'): 
            y = pond_ground_high_fine
        elif (waterbody_type == '1' and application_method == 'b' and drop_size == '3' and boom_height == '1'):
            y = pond_ground_low_m2c
        elif (waterbody_type == '1' and application_method == 'b' and drop_size == '3' and boom_height == '2'):
            y = pond_ground_high_m2c
        elif (waterbody_type == '1' and application_method == 'c' and orchard_type == '1'):
            y = pond_vineyard
        elif (waterbody_type == '1' and application_method == 'c' and orchard_type == '2'):
            y = pond_orchard
        elif (waterbody_type == '2' and application_method == 'a' and drop_size == '1'):
            y = lake_aerial_f2vf
        elif (waterbody_type == '2' and application_method == 'a' and drop_size == '2'):
            y = lake_aerial_f2m
        elif (waterbody_type == '2' and application_method == 'a' and drop_size == '3'):
            y = lake_aerial_m2c
        elif (waterbody_type == '2' and application_method == 'a' and drop_size == '4'):
            y = lake_aerial_c2vc
        elif (waterbody_type == '2' and application_method == 'b' and drop_size == '1' and boom_height == '1'):
            y = lake_ground_low_f
        elif (waterbody_type == '2' and application_method == 'b' and drop_size == '1' and boom_height == '2'): 
            y = lake_ground_high_f
        elif (waterbody_type == '2' and application_method == 'b' and drop_size == '3' and boom_height == '1'):
            y = lake_ground_low_m2c
        elif (waterbody_type == '2' and application_method == 'b' and drop_size == '3' and boom_height == '2'):
            y = lake_ground_high_m2c
        elif (waterbody_type == '2' and application_method == 'c' and orchard_type == '1'):
            y = lake_vineyard
        elif (waterbody_type == '2' and application_method == 'c' and orchard_type == '2'):
            y = lake_orchard    
        elif (waterbody_type == '3' and application_method == 'a' and drop_size == '1'):
            y = stream_aerial_f2vf
        elif (waterbody_type == '3' and application_method == 'a' and drop_size == '2'):
            y = stream_aerial_f2m
        elif (waterbody_type == '3' and application_method == 'a' and drop_size == '3'):
            y = stream_aerial_m2c
        elif (waterbody_type == '3' and application_method == 'a' and drop_size == '4'):
            y = stream_aerial_c2vc
        elif (waterbody_type == '3' and application_method == 'b' and drop_size == '1' and boom_height == '1'):
            y = stream_ground_low_fine
        elif (waterbody_type == '3' and application_method == 'b' and drop_size == '1' and boom_height == '2'): 
            y = stream_ground_high_fine
        elif (waterbody_type == '3' and application_method == 'b' and drop_size == '3' and boom_height == '1'):
            y = stream_ground_low_m2c
        elif (waterbody_type == '3' and application_method == 'b' and drop_size == '3' and boom_height == '2'):
            y = stream_ground_high_m2c
        elif (waterbody_type == '3' and application_method == 'c' and orchard_type == '1'):
            y = stream_vineyard
        elif (waterbody_type == '3' and application_method == 'c' and orchard_type == '2'):
            y = stream_orchard
#        else:
#            y = 0
        
        templatepath = os.path.dirname(__file__) + '/../templates/'
        html = template.render(templatepath + '01uberheader.html', {'title':'Ubertool'})
        html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'agdrift'})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        html = html + template.render(templatepath + '04uberoutput_start.html', {})
        html = html + """
        <table border="1">
        <tr><H3>User Inputs</H3></tr>
        <tr>
        <td>Application method</td>
        <td>%s</td>
        </tr>
        <tr>
        <td>Drop size</td>
        <td>%s</td>
        </tr>
        <tr>
        <td>Waterbody type</td>
        <td>%s</td>
        </tr>
        <tr>
        </table>
        """ % (application_method, drop_size, waterbody_type)
        html = html +  """<table width="400" border="1", style="display:none">
                          <tr>
                          <td>deposition</td>
                          <td id="deposition">%s</td>
                          </tr>                                                    
                          </table>"""%(y)
        html = html + template.render(templatepath + 'agdrift-output-jqplot.html', {})         
        html = html + template.render(templatepath + '04uberoutput_end.html', {})
        html = html + template.render(templatepath + '05ubertext_links_right.html', {})
        html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})
          
       
        self.response.out.write(html)
          
app = webapp.WSGIApplication([('/.*', agdriftOutputPage)], debug=True)
        
      
def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()