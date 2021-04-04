import stdaudio
import math
import sys
import random
import collections
import stddraw

class GuitarString():
    def __init__(self, frequency):
        self.frequency = frequency
        self.wavetable= collections.deque()
        for i in range(math.ceil(44100/frequency)):
            self.wavetable.append(0)

    def pluck(self):
        for i in range(len(self.wavetable)):
            self.wavetable[i]=random.uniform(-0.5,0.5)

    def tick(self):
        y=0.996*0.5*(self.wavetable[0]+self.wavetable[1])
        self.wavetable.popleft()
        self.wavetable.append(y)
        return y
