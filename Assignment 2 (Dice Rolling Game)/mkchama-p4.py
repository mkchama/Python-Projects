import random
import stdio

def roll():
    return random.randrange(1,7)

def roll1(times_rolled):
    count = 0
    for i in range(times_rolled):
        die = roll()
        if die ==1:
            count = count + 1
    return count

def prob():
    times_rolled = 10000
    count6=0
    count12=0
    for i in range(times_rolled):
        count = roll1(6)
        if count >= 1:
            count6 = count6 + 1
        count = roll1(12)
        if count >= 2:
            count12 = count12 + 1
    roll_6 = float(count6)/times_rolled
    roll_12 = float(count12)/times_rolled
    stdio.writeln("Estimated likelyhood of 1 once in 6: {}".format(roll_6))
    stdio.writeln("Estimated likelyhood of 1 twice in 12: {}".format(roll_12))
    if roll_6 > roll_12:
        stdio.writeln("Therefore, there is a greater probability of recieiving a 1 once in 6 than 1 twice in 12")
    elif roll_6 < roll_12:
        stdio.writeln("Therefore, there is a greater probability of recieiving a 1 twice in 12 than 1 once in 6")

prob()
