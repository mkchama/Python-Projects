import sys
import math
import stddraw
import stdrandom
import random
import stdstats

def fill_brownian(a, i0, i1, variance, scale):
    if (i1-i0) < 2:
        return

    ym = (a[i0] + a[i1])/2.0
    ym+=random.gauss(0,math.sqrt(variance))
    midindex=(i0+i1)//2
    a[midindex]=ym
    fill_brownian(a,i0,midindex,variance/scale,scale)
    fill_brownian(a,midindex,i1,variance/scale,scale)


hurstExponent = float(sys.argv[1])
stddraw.setCanvasSize(500,500)
stddraw.setXscale(0,150)
stddraw.setYscale(-5,5)
stddraw.setPenRadius(0.0)
scale = 2 ** (2.0 * hurstExponent)
a= [0 for i in range(129)]
fill_brownian(a,0,128,1,scale)

stdstats.plotLines(a)
stddraw.show()
