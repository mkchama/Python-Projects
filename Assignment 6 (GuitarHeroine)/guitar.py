import stdaudio
import math
import sys
import random
import collections
import stddraw
from picture import Picture
from mkchamap3 import GuitarString

keyboard = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/' ";

strings= [GuitarString(110)]
for i in range(1,37):
    strings.append(GuitarString(strings[i-1].frequency*2**(1/12)))

escape=False
ind=-1
while not escape:
    # check for and process events
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        ind= keyboard.find(key)
        if key == chr(27):
            escape = True
        elif ind==-1:
            print("wrong input key")
        else:
            strings[ind].pluck()


    y=strings[ind].tick()
    stdaudio.playSample(y)
