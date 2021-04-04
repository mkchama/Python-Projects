import random
import math
import sys
lexicon=[]
word=""
wrongguesses=""
lookupindex=0
attempts=8
rightguesses=""
found= False
reenter=True
lex = open(sys.argv[1], "r")
for line in lex:
    words_in_lex=line.rstrip()
    lexicon.append(words_in_lex)

i = random.randrange(0,len(lexicon)-1)

while len(lexicon[i]) < 4:
    i = random.randrange(0,len(lexicon)-1)
selected=lexicon[i]
for u in range(len(lexicon[i])):
    word=word+'_'
remaining=len(word)
print('Welcome to CPSC 231 Console Hangman!')

while attempts>0 and remaining>0:
    print('\nThe secret word looks like:', word)
    if len(wrongguesses)>1:
        print('Your bad guesses so far:', wrongguesses)
    print('You have', attempts, 'guesses remaining.')
    while reenter:
        reenter=False
        usr = str(input("What's your next guess? "))
        if len(usr)>1 or len(usr) == 0 or usr.isspace():
            print("You can only enter a single character. Please try again.")
            reenter=True
            continue
        for letter in (wrongguesses+rightguesses):
            if letter == usr:
                print("You have already entered that character before. Please try again.")
                reenter=True
    reenter=True
    for letter in selected:
        if letter == usr:
            word=list(word)
            word[lookupindex]=usr
            word="".join(word)
            found=True
            remaining-=1
        lookupindex=lookupindex+1
    if not found:
        attempts-=1
        wrongguesses+=(usr+" ")
        print('Sorry, there is no "'+usr+ '".')
    else:
        rightguesses+=usr
        print('Nice guess!')
    found=False
    lookupindex=0


if remaining == 0:
    print('\nCongratulations!\nYou guessed the secret word:', selected)
if attempts == 0:
    print('\nYou have lost! Try again when you have improved your deductive reasoning skills.\nThe word was', selected)
