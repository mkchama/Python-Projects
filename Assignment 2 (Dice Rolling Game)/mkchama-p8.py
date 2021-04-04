import random
import stdio
import sys

def roll():
    return random.randrange(1,7)
cpu = ['Player One', 'Player Two']
total = {"Player One's score": 0, "Player Two's score": 0}
random.shuffle(cpu)
total1 = 0
total2 = 0
temp = 0

while total1 < 100 and total2 <100:
    for i in cpu:
        print("Player One's score is", total1)
        print("Player Two's score is", total2)
        if i == 'Player One':
            turntotal = 0
            print("It is " + str(i) + "'s turn.")
            current_roll = 0
            temp= total1
            while turntotal < 20 :
                    current_roll = roll()
                    turntotal += current_roll
                    temp += current_roll
                    print ('Rolled a', current_roll)
                    if current_roll == 1:
                        print ('Rolled a', current_roll)
                        print ('Pigged out!')
                        turntotal=0
                        break
                    if temp >= 100:
                        break
            total1 += turntotal
            print ('Total turn score =', turntotal)
        else:
            turntotal = 0
            print("It is " + str(i) + "'s turn.")
            temp = total2
            while turntotal < 20 :
                current_roll = roll()
                turntotal += current_roll
                temp += current_roll
                print ('Rolled a', current_roll)
                if current_roll == 1:
                    turntotal= 0
                    print ('Pigged out!')
                    break
                if temp >= 100:
                    break
            total2 += turntotal
            print("Total turn score is:", turntotal)

        if total1>=100 or total2>=100:
            break
print("Final score: " , total1 , " vs " , total2)
if total1 > 100: print ('Player One wins!')
else: print ('Player Two wins!')
