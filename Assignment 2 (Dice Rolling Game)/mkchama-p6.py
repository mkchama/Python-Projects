import random
import stdio
import sys

def roll():
    return random.randrange(1,7)

temp = int(input('Enter current score: '))

total = temp
turntotal=0
current_roll = 0
while total <  100 and turntotal < 20:
    current_roll = roll()
    print ('Rolled a', current_roll)
    if current_roll == 1:
        print ('Pigged out!')
        turntotal=0
        total=temp
        break
    elif turntotal > 20:
        break
    else:
        total += current_roll
        turntotal += current_roll


print ('Turn score =', turntotal)
print ('New total score =', total)
