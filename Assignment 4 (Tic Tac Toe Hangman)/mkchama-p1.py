import sys

lexicon=[]
letters=[]
lex = open(sys.argv[1], "r")
word = str(sys.argv[2])


for line in lex:
    words_in_lex=line.rstrip()
    lexicon.append(words_in_lex)

unique = set(word)

for letter in unique:
    letters.append(letter)
    letters.sort()

if word in lexicon:
    lexicon.index(words_in_lex)
    number = lexicon.index(word) + 1

    temp1=number%10
    temp2=int(number/10)%10
    if temp2!=1:
        if temp1 == 1:
            ordi='st'
        elif temp1 == 2:
            ordi='nd'
        elif temp1 == 3:
            ordi='rd'
        else:
            ordi='th'
    else:
        ordi='th'

    num=str(number)+ordi
    print('According to our lexicon', word, 'is the', num, 'most common word in contemporary American English.')
else:
    print('According to our lexicon', word, 'is not in the 4000 most common words of contemporary American English.')

print('It contains the following letters:\n', *letters)
