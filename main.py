from mayavi.mlab import *
import testfuncs as test
import numpy as np


def main():
    test.point_test()
    #test.axes()
    #test.triangle_test(color = (0,1,0), opacity = 0.5)
    #test.triangle_test()
    #test.simplex_3d_test()
    #test.triangle_unfilled_test()
    #test.axes()
    #test.text3d(0, 0, 1, "Test", scale = 0.2)
    show()


if __name__ == "__main__":
    main()