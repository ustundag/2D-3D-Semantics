import numpy as np
from mayavi import mlab
from tvtk.api import tvtk
import matplotlib.pyplot as plt # only for manipulating the input image

def manual_sphere(image_file):
    # caveat 1: flip the input image along its first axis
    img = plt.imread(image_file) # shape (N,M,3), flip along first dim
    #outfile = image_file.replace('.png', '_flipped.png')
    # flip output along first dim to get right chirality of the mapping
    #img = img[::-1,...]
    #plt.imsave(outfile, img)
    #image_file = outfile  # work with the flipped file from now on

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

    # create figure
    mlab.figure(size=(600, 600))
    # create meshed sphere
    mesh = mlab.mesh(x,y,z)
    mesh.actor.actor.mapper.scalar_visibility = False
    mesh.actor.enable_texture = True  # probably redundant assigning the texture later

    # load the (flipped) image for texturing
    img = tvtk.PNGReader(file_name=image_file)
    texture = tvtk.Texture(input_connection=img.output_port, interpolate=0, repeat=0)
    mesh.actor.actor.texture = texture

    # tell mayavi that the mapping from points to pixels happens via a sphere
    mesh.actor.tcoord_generator_mode = 'sphere' # map is already given for a spherical mapping
    cylinder_mapper = mesh.actor.tcoord_generator
    # caveat 2: if prevent_seam is 1 (default), half the image is used to map half the sphere
    cylinder_mapper.prevent_seam = 0 # use 360 degrees, might cause seam but no fake data
    #cylinder_mapper.center = np.array([0,0,0])  # set non-trivial center for the mapping sphere if necessary

if __name__ == "__main__":
    image_file = 'test_pano_rgb.png'
    manual_sphere(image_file)
    mlab.show()