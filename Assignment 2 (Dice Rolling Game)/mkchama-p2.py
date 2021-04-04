# import statements
import random
import sys
import stdio
import math

N = int(sys.argv[1])
total = 0
def roll(num):
    result = []
    for i in range(0, num):
        result.append(random.randrange(1,7))
    return result
result = roll(N)
for i in result:
    total += i

stdio.writeln("Rolling {} times...".format(N))
stdio.writeln("Estimated expectation: {}".format(total / N))
