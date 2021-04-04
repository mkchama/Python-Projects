import sys
import math
import stddraw
import stdrandom
import random
import stdstats
import stdaudio


rate = 44100
duration = 20
frequency = 0.25

def fill_brownian(a, i0, i1, variance, scale):
    if (i1-i0) < 2:
        return

    ym = (a[i0] + a[i1])/2.0
    ym+=random.gauss(0,math.sqrt(variance))

    midindex=(i0+i1)//2
    a[midindex]=ym

    fill_brownian(a,i0,midindex,variance/scale,scale)
    fill_brownian(a,midindex,i1,variance/scale,scale)

    return a

def brownnoise(brown_a):

    for i in range(882):
        part_a = []
        for i in range(1000):
            part_a.append(0.0)
        part_a = fill_brownian(part_a, 0, 999, 0.05, 2)
        brown_a.extend(part_a)
    return brown_a

def whitenoise(white_a):

    for i in range(rate * duration):

        white = random.uniform(-0.25, 0.25)
        white_a.append(white)

    return white_a

def blend(blend_a):

    for t in range(rate * duration):

        blend = math.sin(math.pi * frequency * t/rate ) ** 6
        blend_a.append(blend)

    return blend_a

def fill_ocean(ocean_a, brown_a, white_a, blend_a):

    for i in range(rate * duration):
        ocean_a.append(0)

    for i in range(rate * duration):
        part = (1 - blend_a[i]) * brown_a[i] + blend_a[i] * white_a[i]
        ocean_a[i] = part

    return ocean_a

def main():

    brown_a = []
    brown_a = brownnoise(brown_a)
    white_a = []
    white_a = whitenoise(white_a)
    blend_a = []
    blend_a = blend(blend_a)

    # for i in range(100):
    #     print("Brown: \t".format(brown_a[i]))
    #     print("White: \t".format(white_a[i]))
    #     print("Blend: \t".format(blend_a[i]))

    ocean_a = []
    ocean_a = fill_ocean(ocean_a, brown_a, white_a, blend_a)

    stdaudio.playSamples(ocean_a)

main()
