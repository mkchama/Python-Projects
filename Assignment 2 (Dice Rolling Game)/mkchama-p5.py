import random
import sys
import stdio

def roll():
    return random.randrange(1,7)

total = 0
turntotal = 0
current_roll = 0

while total <  100 and turntotal < 20:
    current_roll = roll()
    print ('Rolled a', current_roll)
    if current_roll == 1:
        print ('Pigged out!')
        turntotal=0
        break
    elif turntotal > 20:
        break
    else:
        total += current_roll
        turntotal += current_roll


print ('Turn score =', turntotal)
