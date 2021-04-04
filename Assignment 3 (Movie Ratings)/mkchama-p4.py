import stdio
import sys
import numpy

fh = open(sys.argv[1], "r")
ratings_file = open(sys.argv[2], 'r')
myratings_file = open(sys.argv[3], 'r')

counter=0
reviewcount=0
sumreview=0
rranks=[]
mranks=[]
values=[]
temp=[]
myranks=[]
similarity=[]
sorted_reviews=[]
unseen=[]
average_recom=[]
recom_list=[]
recom_rev=[]
for line in fh:
    movie=line.rstrip()
    mranks.append(movie)

for line in ratings_file:
    counter+=1
    row_rating=line.rstrip()
    row_rating=row_rating.split(',')
    if len(row_rating)==100:
        rranks.append(row_rating)

name=myratings_file.readline();
print("Hello " + name.rstrip() + '!\n')

rankings= myratings_file.readline()
rankings_array=rankings.split(',')
for i in range(len(rankings_array)):
    if rankings_array[i] == '1' :
        myranks.append(-5)
    elif rankings_array[i] == '2':
        myranks.append(-3)
    elif rankings_array[i] == '3':
        myranks.append(1)
    elif rankings_array[i] == '4':
        myranks.append(3)
    elif rankings_array[i] == '5':
        myranks.append(5)
    elif rankings_array[i] == '0':
        myranks.append(0)

for r in range(len(rranks)):
    for c in range(len(rranks[r])):
        if rranks[r][c] == '1' :
            temp.append(-5)
        elif rranks[r][c] == '2':
            temp.append(-3)
        elif rranks[r][c] == '3':
            temp.append(1)
        elif rranks[r][c] == '4':
            temp.append(3)
        elif rranks[r][c] == '5':
            temp.append(5)
        elif rranks[r][c] == '0':
            temp.append(0)
#    values.append(temp)

values=numpy.reshape(temp,(179,100))
for r in range(len(values)):
    s=numpy.dot(values[r],myranks)
    similarity.append(s)

similarity_sorted=sorted(range(len(similarity)), key=lambda k:similarity[k],reverse=True)

for r in range(len(similarity)):
    sorted_reviews.append(rranks[similarity_sorted[r]])

for i in range(len(myranks)):
    if myranks[i] == 0:
        unseen.append(i)
for i in range(len(unseen)):
    for j in range(len(sorted_reviews)):
        if sorted_reviews[j][unseen[i]] != '0':
            sumreview+= int(sorted_reviews[j][unseen[i]])
            reviewcount+=1
            if reviewcount==5:
                break
    average_recom.append(sumreview/5)
    sumreview=0
    reviewcount=0

if len(unseen)==0:
    print('There are no movie recommendations, as you have seen them all.')
else:
    average_recom_sorted=sorted(range(len(average_recom)), key=lambda k:average_recom[k],reverse=True)
    i=0
    while i < min(12,len(unseen)) and average_recom[average_recom_sorted[i]]>3.5: #This will print the first 12 recommendations, unless the number of unseen movies is less than 12, or the rating drops below 3.5
        recom_list.append(mranks[average_recom_sorted[i]])
        i+=1

    print('From your ratings of our 100 movies, our CPSC 231 class believes that you might also like:', *recom_list,sep="\n ")
