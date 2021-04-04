import random
import sys
import stdio

N = int(sys.argv[1])

total = 0
for i in range(N):
    times_rolled = 0
    while True:
        dice_number = random.randrange(1,7)
        times_rolled += 1
        if dice_number == 1:
            break
    total += times_rolled

avg = total / N

stdio.writeln("Simulating {} turns...".format(N))
stdio.writeln("Estimated Expectation: {} ".format(avg))
