import stdio
import sys

# Average Number of Movies seen.
seen = 0
counter=0
pop=0
sumrating=0
var=0

fh = open(sys.argv[1], "r")
ratings_file = open(sys.argv[2], 'r')
rranks=[]
mranks=[]
popularity=[]
mostpop=[]
leastpop=[]
allsumratings=[]
mostrating=[]
leastrating=[]
cont=[]
mostcont=[]

for line in fh:
    movie=line.rstrip()
    mranks.append(movie)

for line in ratings_file:
    counter+=1
    row_rating=line.rstrip()
    row_rating=row_rating.split(',')
    if len(row_rating)==100:
        rranks.append(row_rating)

for r in range(len(rranks)):
    for c in range(len(rranks[r])):
        if rranks[r][c] != '0':
            seen+=1
avg=(seen/((r+1)*(c+1)))*100
rounded=round(avg,1)

for c in range(len(rranks[0])):
    for r in range(len(rranks)):
        if rranks[r][c] != '0' :
            pop += 1
            sumrating += int(rranks[r][c])
    if pop<10:
        pop=0
        sumrating=0
        continue
    popularity.append(pop)
    sumrating/=pop
    roundsum=round(sumrating)
    allsumratings.append(sumrating)
    for r in range(len(rranks)):
        if rranks[r][c] != '0' :
            var+=(int(rranks[r][c])-sumrating)**2
    var/=(pop-1)
    pop=0
    sumrating=0
    cont.append(var)

allsumrating_sorted=sorted(range(len(allsumratings)), key=lambda i:allsumratings[i])

popularity_sorted=sorted(range(len(popularity)), key=lambda k:popularity[k])

contentious_sorted=sorted(range(len(cont)), key=lambda k:cont[k])

for i in range(5):
    mostcont.append(mranks[contentious_sorted[len(cont)-i-1]])

for i in range(5):
    mostpop.append(mranks[popularity_sorted[len(popularity)-i-1]])
for i in range(5):
    mostrating.append(mranks[allsumrating_sorted[len(allsumratings)-i-1]])

for i in range(5):
    leastpop.append(mranks[popularity_sorted[i]])
for i in range(5):
    leastrating.append(mranks[allsumrating_sorted[i]])


print('The average student in CPSC 231 has seen', rounded, 'of the 100 movies')
print('\nThe most popular movies were:', *mostpop,sep="\n")
print('\nThe least popular movies were:', *leastpop, sep='\n')
print('\nThe highest rated movies were:', *mostrating, sep='\n')
print('\nThe lowest rated movies were:', *leastrating, sep='\n')
print('\nThe most contentious movies were:', *mostcont, sep='\n')



#How many of our 100 movies, has the class seen.
#Calculate the average number of non-zero ratings per individual in our data set

#Most Popular movies. Find the 5 movies that ahve been seen by most students

#Least Popular movies. Find the 5 movies that have been seen least. Zero ratings_file

#Highest Rated movies. Find 5 movies with the highest average rating in class(object):

#Lowest Rated Movies. Worst movies, find 5 movies with the lowest rating. Dont include 0 ratings_file

#Most contentious movies, find 5 movies with the highest variance. Dont include 0self.
