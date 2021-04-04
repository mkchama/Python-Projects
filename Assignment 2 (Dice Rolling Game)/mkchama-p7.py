import random
import stdio
import sys

def roll():
    return random.randrange(1,7)

def program():
    total=0
    turntotal=0
    current_roll=0
    temp=0
    while total < 100:
        while turntotal < 20 :
            current_roll = roll()
            turntotal += current_roll
            temp += current_roll
            print ('Rolled a', current_roll)
            if current_roll == 1:
                print ('Pigged out!')
                turntotal=0
                break
            if temp >= 100:
                break
        total += turntotal
        temp = total
        print ('Turn score =', turntotal)
        turntotal = 0
        print ('New total score =', total)

program()
