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


def whitenoise(array):
    for i in range(rate * duration):
        white = random.uniform(-0.25, 0.25)
        array.append(white)
    return array


def sin(sina):
    for t in range(rate * duration):
        st = math.sin(math.pi * frequency * t/rate ) ** 6
        sina.append(st)
    return sina


def fill_ocean(ocean, brown_a, array, sina):
    for i in range (rate * duration):
        ocean.append(0)

    for i in range (rate * duration):
        wave = (1-sina[i])* brown_a[i] + sina[i]* array[i]
        ocean[i]=wave
    return ocean

def main():
    brown_a = []
    brown_a = brownnoise(brown_a)

    array = []
    array = whitenoise(array)

    sina = []
    sina = sin(sina)

    ocean = []
    ocean = fill_ocean(ocean, brown_a, array, sina)

    stdaudio.playSamples(ocean)


main()
