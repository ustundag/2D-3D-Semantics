# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from mayavi import mlab
import numpy as np
from scipy.special import sph_harm

"""
# Create a sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0:pi:101j, 0:2 * pi:101j]

x = r * sin(phi) * cos(theta)
y = r * sin(phi) * sin(theta)
z = r * cos(phi)

mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()
# Represent spherical harmonics on the surface of the sphere
for n in range(1, 6):
    for m in range(n):
        s = sph_harm(m, n, theta, phi).real

        mlab.mesh(x - m, y - n, z, scalars=s, colormap='jet')

        s[s < 0] *= 0.97

        s /= s.max()
        mlab.mesh(s * x - m, s * y - n, s * z + 1.3,
                  scalars=s, colormap='Spectral')

mlab.view(90, 70, 6.2, (-1.3, -2.9, 0.25))
mlab.show()
"""

path = 'camera_04a287849657478ea774727e5bff5202_office_3_frame_equirectangular_domain_rgb.png'
"""
from PIL import Image
f = np.asarray(Image.open(path))
"""
import matplotlib.pyplot as plt # only for manipulating the input image
f = plt.imread(path) # shape (N,M,3), flip along first dim

# parameters for the sphere
R = 1 # radius of the sphere
Nrad = 180 # points along theta and phi
phi = np.linspace(0, 2 * np.pi, Nrad)  # shape (Nrad,)
theta = np.linspace(0, np.pi, Nrad)    # shape (Nrad,)
phigrid,thetagrid = np.meshgrid(phi, theta) # shapes (Nrad, Nrad)

# compute actual points on the sphere
x = R * np.sin(thetagrid) * np.cos(phigrid)
y = R * np.sin(thetagrid) * np.sin(phigrid)
z = R * np.cos(thetagrid)
mlab.mesh(x, y, z, scalars=f, colormap='coolwarm')
mlab.show()







