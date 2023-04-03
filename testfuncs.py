import numpy as np
from mayavi.mlab import *

def point_test():
    xList = [n for n in range(10)]
    yList = [0 for n in range(10)]
    zList = yList

    scaleList = [n + 1 for n in range(10)]

    return points3d(xList, yList, zList, scaleList, scale_factor = 0.1)

def triangle_test(**kwargs):
    xList = [0, 0.5, 1]
    yList = [0, 0,   0]
    zList = [0, 1,   0]
    
    # Note that triangles are indicated by the index of their position in the array. So 0 represents the vertex (0,0,0), 1 represents the vertex (0.5, 0, 1), 
    # and 2 represents the vertex (1,0,0).
    tri_indices = [(0, 1, 2)]

    return triangular_mesh(xList, yList, zList, tri_indices, **kwargs)

def triangle_unfilled_test(**kwargs):
    xList = [0, 0.5, 1, 0]
    yList = [0, 0,   0, 0]
    zList = [0, 1,   0, 0]

    plot3d(xList, yList, zList, **kwargs)


def simplex_3d_test(**kwargs):
    xList = [0, 0.5, 1, 0.5]
    yList = [0, 0,   0, 1  ]
    zList = [0, 1,   0, 0.5]

    # Note that triangles are indicated by the index of their position in the array. So 0 represents the vertex (0,0,0), 1 represents the vertex (0.5, 0, 1)
    tri_indices = [(0, 1, 2), (1,2,3), (0,2,3), (0,1,3)]

    return triangular_mesh(xList, yList, zList, tri_indices, **kwargs)

#Function below taken from https://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html#mayavi.mlab.triangular_mesh
def test_triangular_mesh():
    """An example of a cone, ie a non-regular mesh defined by its
        triangles.
    """
    n = 8
    t = np.linspace(-np.pi, np.pi, n)
    z = np.exp(1j * t)
    x = z.real.copy()
    y = z.imag.copy()
    z = np.zeros_like(x)

    triangles = [(0, i, i + 1) for i in range(1, n)]
    x = np.r_[0, x]
    y = np.r_[0, y]
    z = np.r_[1, z]
    t = np.r_[0, t]

    return triangular_mesh(x, y, z, triangles, scalars=t)