import sys

seen=0
favorite="  "
least="  "
fh = open(sys.argv[1], "r")
ratings_file = open(sys.argv[2], 'r')

name=ratings_file.readline();
print("Hello " + name.rstrip() + '!\n')

rankings= ratings_file.readline()
rankings_array=rankings.split(',')

lines= fh.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].rstrip()
    if rankings_array[i] != '0':
        seen+=1
    if rankings_array[i] == '5':
        favorite += lines[i]+ "\n  "
    elif rankings_array[i] == '1':
        least += lines[i]+ "\n  "
print("It looks like you've seen", seen, "of the 100 movies \n")
print("Your favorite movies were: \n" + favorite)
print("Your least favorite movies were:\n" + least)
