import sys

temp = input("What's your name? ")
print("Hi, "+temp+"! \nPlease tell us your favorite movies using the following scale:")
print(" 0 = Never seen it. \n 1 = It was terrible! \n 2 = Didn’t like it. \n 3 = It was OK. \n 4 = Liked it. \n 5 = It was awesome!")
s='6'
scores = ['0','1','2','3','4','5']
fh = open("cpsc231-movies.txt", "r")
output_file = open('my-ratings.txt', 'w')
output_file.write(temp)
output_file.write('\n')
while s not in scores:
    s = input(fh.readline().rstrip()+ '? ')
output_file.write(s)
s='6'
for line in fh:

    while s not in scores:
        s = input(line.rstrip()+ '? ')
    output_file.write(',' + s)
    s='6'
fh.close()

print('Thank you!')
print('Your ratings were saved to my-ratings.txt')
