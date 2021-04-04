import stddraw
import picture
import math
import random

class Taffy(object):

    def __init__(self,shape):
        self.shape = shape
    def settaf(self,shape):
        self.shape=shape

    def taffies(self,x,y):

        if self.shape == 1:
            stddraw.picture(picture.Picture('pic1.png'), x, y)

        elif self.shape == 2:
            stddraw.picture(picture.Picture('pic2.png'), x, y)

        elif self.shape == 3:
            stddraw.picture(picture.Picture('pic3.png'), x, y)

        elif self.shape == 4:
            stddraw.picture(picture.Picture('pic4.png'), x, y)

        elif self.shape == 5:
            stddraw.picture(picture.Picture('pic5.png'), x, y)

        elif self.shape == 6:
            stddraw.picture(picture.Picture('pic6.png'), x, y)

    def checker(board):
        for i in range(1,8):
            for j in range(1,6):
                if (board[i][j].shape == board[i+1][j].shape and board[i][j].shape==board[i-1][j].shape) or ((board[i][j].shape == board[i][j+1].shape and board[i][j].shape==board[i][j-1].shape)):
                    return False

        for j in range(1,6):
            if ((board[0][j].shape == board[0][j+1].shape and board[0][j].shape==board[0][j-1].shape)) or ((board[8][j].shape == board[8][j+1].shape and board[8][j].shape==board[8][j-1].shape)):
                return False

        for i in range(1,8):
            if ((board[i][0].shape == board[i+1][0].shape and board[i][0].shape==board[i-1][0].shape)) or ((board[i][6].shape == board[i+1][6].shape and board[i][6].shape==board[i-1][6].shape)):
                return False
        return True

class Board(object):

    def __init__(self):
        self.tafobj=[[Taffy(random.randint(1,6)) for i in range(7)] for j in range(9)]
        self.score_count=0


    def randomize(self):
        while not Taffy.checker(self.tafobj):
            self.tafobj=[[Taffy(random.randint(1,6)) for i in range(7)] for j in range(9)]

    def draw_board(self):
        for i in range(0,9):
            for j in range(0,7):
                self.tafobj[i][j].taffies(j+0.5,i+1.5)
        if self.score_count<50:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setFontSize(32)
            stddraw.text(3.5, 0.5, 'Score: ' + str(self.score_count))
        if self.score_count>= 500:
            stddraw.clear()
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.text(3.5, 0.5, 'Final Score: ' + str(self.score_count))
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.text(3.5, 2.5, "You Have Won!")
            stddraw.setFontSize(32)
            stddraw.setPenColor(stddraw.RED)
            stddraw.text(3.5,5.5,'GAME OVER')
            stddraw.show()

    def board_checker(self):
        for i in range (0, 9):
            for j in range (0, 7):
                if self.tafobj[i][j].shape==0:
                    counter=1
                    verticalincrement=1

                    while(self.tafobj[i+verticalincrement][j].shape==0):
                        counter+=1
                        verticalincrement+=1

                    for k in range(i, 9-counter):
                        self.tafobj[k][j].shape = self.tafobj[k+counter][j].shape
                    for k in range(9-counter,9):
                        self.tafobj[k][j].shape = random.randint(1,6)

    def score_counter(self,matchlen):
        self.score_count+=matchlen


    def match_handler(self):
        not_complete = True

        while(not_complete):
            sample.matchingsequencex=1
            sample.matchingsequencey=1
            for x in range (0, 9):
                for y in range (0, 7):
                     match_exist = self.match_checker(x, y)


                     if (match_exist):


                         # On horizontal match, shift down taffies
                         if (sample.matchingsequencex > 2):
                             print("HORIZONTAL MATCH")
                             sample.score_counter(sample.matchingsequencex)
                             for i in range(sample.starthx, 9):
                                 for j in range(sample.starthy, sample.endhy + 1):
                                     if (i < 8):
                                         temp = i + sample.endhx - sample.starthx + 1
                                         sample.tafobj[i][j].shape = sample.tafobj[temp][j].shape
                                         stddraw.show(50)

                                         # Print statement for debugging
                                         print("To change: ({0}, {1})\t Data: ({2}, {3})".format(i, j, temp, j))
                                     else:
                                         sample.tafobj[i][j].shape = random.randint(1, 6)
                                         stddraw.show(50)
                             sample.matchingsequencex = 1

                         # On vertical match, shift down taffies
                         if (sample.matchingsequencey > 2):
                             sample.score_counter(sample.matchingsequencey)

                             # Calculate the length of the vertical match
                             tempLen = abs(sample.startvx - sample.endvx) + 1
                             print("VERTICAL MATCH")

                             for i in range(sample.startvx, 9):
                                 if (i + tempLen >= 9):
                                     sample.tafobj[i][sample.startvy].shape = random.randint(1,6)
                                     stddraw.show(50)
                                 else:
                                     print("To change: ({0}, {1})\t Data: ({2}, {3})".format(i, sample.startvy, i + tempLen, sample.startvy))
                                     sample.tafobj[i][sample.startvy].shape = sample.tafobj[i + tempLen][sample.startvy].shape
                                     stddraw.show(50)

                             sample.matchingsequencey = 1

            not_complete = False


    def match_checker(self,x,y):
        self.matchingsequencex = 1
        self.matchingsequencey = 1

        self.starthx = x
        self.starthy = y
        self.endhx = x
        self.endhy = y

        self.startvx = x
        self.startvy = y
        self.endvx = x
        self.endvy = y

        # Print statements for debugging
        # print(self.matchingsequencex)
        # print(self.matchingsequencey)
        # print(self.starthx)
        # print(self.starthy)
        # print(self.endhx)
        # print(self.endhy)
        # print(self.startvx)
        # print(self.startvy)
        # print(self.endvx)
        # print(self.endvy)

        for j in range(y+1, 7):
            if self.tafobj[x][y].shape==self.tafobj[x][j].shape:
                self.matchingsequencex += 1
                self.endhx = x
                self.endhy = j
            else:
                break

        for j in range(1, y+1):
            if self.tafobj[x][y].shape==self.tafobj[x][y-j].shape:
                self.matchingsequencex+=1
                self.starthx = x
                self.starthy = y-j
            else:
                break

        for j in range(x+1,9):
            if self.tafobj[x][y].shape==self.tafobj[j][y].shape:
                self.matchingsequencey+=1
                self.endvx=j
                self.endvy=y
            else:
                break

        for j in range(1,x+1):
            if self.tafobj[x][y].shape==self.tafobj[x-j][y].shape:
                self.matchingsequencey += 1
                self.startvx = x-j
                self.startvy = y
            else:
                break

        if self.matchingsequencey<3 and self.matchingsequencex<3:
            return False
        else:
            return True


def game_text():

    stddraw.setFontSize(32)
    stddraw.text(3.5, 5.5, ('Welcome to Taffy Tangle'))

    stddraw.setFontSize(18)
    stddraw.text(3.5, 3.5, ('Reach a score of at least 50 to win'))

    stddraw.show(1000)




def red_square(x,y,z):
    stddraw.setPenColor(stddraw.RED)
    stddraw.square(x,y,z)
    stddraw.show(500)


rows = 10
columns = 7
width = columns * 64
height = rows * 64
stddraw.setCanvasSize(width, height)
stddraw.setXscale(0, columns)
stddraw.setYscale(0, rows)

Game = True
mouseclick=0
sample=Board()
sample.randomize()

game_text()
while Game:
    stddraw.clear()
    sample.draw_board()
    stddraw.show(100)

    if stddraw.mousePressed():

        mouseclick+=1

        if mouseclick == 1:
            firsty= math.floor(stddraw.mouseX())
            firstx= math.floor(stddraw.mouseY())-1
            stddraw.setPenColor(stddraw.RED)
            red_square(firsty+0.5, firstx+1.5, 0.5)

        if mouseclick ==2:
            secondy= math.floor(stddraw.mouseX())
            secondx= math.floor(stddraw.mouseY())-1
            red_square(secondy+0.5, secondx+1.5, 0.5)


            if (abs(secondx-firstx)==1 and (secondy-firsty)==0) or (abs(secondy-firsty)==1 and (secondx-firstx)==0):

                temp = sample.tafobj[firstx][firsty]
                sample.tafobj[firstx][firsty]=sample.tafobj[secondx][secondy]
                sample.tafobj[secondx][secondy]=temp
                stddraw.clear()
                sample.draw_board()
                stddraw.show(500)
                matching1 = sample.match_checker(secondx,secondy)

                if (matching1 != True):
                    matching2 = sample.match_checker(firstx, firsty)

                if (matching1 or matching2):
                    matching1 = False
                    matching2 = False

                    if sample.matchingsequencey>=3:
                        for i in range(sample.startvx,sample.endvx+1):
                            for j in range(sample.startvy,sample.endvy+1):
                                sample.tafobj[i][j].shape=0
                            stddraw.clear()
                            sample.draw_board()
                            stddraw.show(200)
                        sample.score_counter(sample.matchingsequencey)

                    if sample.matchingsequencex>=3:
                        for i in range(sample.starthx,sample.endhx+1):
                            for j in range(sample.starthy,sample.endhy+1):
                                sample.tafobj[i][j].shape=0
                            stddraw.clear()
                            sample.draw_board()
                            stddraw.show(200)
                        sample.score_counter(sample.matchingsequencex)

                    if ((sample.matchingsequencex > 2) and (sample.matchingsequencey >2)):
                        print("HORIZONTAL MATCH")
                        tempLen = abs(sample.startvx - sample.endvx) + 1
                        print("VERTICAL MATCH")

                        for i in range(sample.startvx, 9):
                            if (i + tempLen >= 9):
                                sample.tafobj[i][sample.startvy].shape = random.randint(1,6)
                                stddraw.clear()
                                sample.draw_board()
                                stddraw.show(200)
                            else:

                                sample.tafobj[i][sample.startvy].shape = sample.tafobj[i + tempLen][sample.startvy].shape
                        for i in range(sample.starthx, 9):
                            for j in range(sample.starthy, sample.endhy):
                                if (i < 8):
                                    temp = i + sample.endhx - sample.starthx
                                    sample.tafobj[i][j].shape = sample.tafobj[temp][j].shape
                                    stddraw.clear()
                                    sample.draw_board()
                                    stddraw.show(200)

                                    # Print statement for debugging
                                    # print("To change: ({0}, {1})\t Data: ({2}, {3})".format(i, j, temp, j))
                                else:
                                    sample.tafobj[i][j].shape = random.randint(1, 6)
                    # On vertical match, shift down taffies
                    sample.matchingsequencey = 1
                    elif (sample.matchingsequencey > 2):

                        # Calculate the length of the vertical match
                        tempLen = abs(sample.startvx - sample.endvx) + 1
                        print("VERTICAL MATCH")

                        for i in range(sample.startvx, 9):
                            if (i + tempLen >= 9):
                                sample.tafobj[i][sample.startvy].shape = random.randint(1,6)
                                stddraw.clear()
                                sample.draw_board()
                                stddraw.show(200)
                            else:
                                print("To change: ({0}, {1})\t Data: ({2}, {3})".format(i, sample.startvy, i + tempLen, sample.startvy))
                                sample.tafobj[i][sample.startvy].shape = sample.tafobj[i + tempLen][sample.startvy].shape
                                stddraw.clear()
                                sample.draw_board()
                                stddraw.show(200)

                    # On horizontal match, shift down taffies
                    sample.matchingsequencex = 1
                    elif (sample.matchingsequencex > 2):
                        print("HORIZONTAL MATCH")
                        for i in range(sample.starthx, 9):
                            for j in range(sample.starthy, sample.endhy + 1):
                                if (i < 8):
                                    temp = i + sample.endhx - sample.starthx + 1
                                    sample.tafobj[i][j].shape = sample.tafobj[temp][j].shape
                                    stddraw.clear()
                                    sample.draw_board()
                                    stddraw.show(200)

                                    # Print statement for debugging
                                    # print("To change: ({0}, {1})\t Data: ({2}, {3})".format(i, j, temp, j))
                                else:
                                    sample.tafobj[i][j].shape = random.randint(1, 6)
                            stddraw.clear()
                            sample.draw_board()
                            stddraw.show(200)
                        sample.match_handler()
                        stddraw.clear()
                        sample.draw_board()
                        stddraw.show(200)



                    sample.match_handler()
                    stddraw.clear()
                    sample.draw_board()
                    stddraw.show(200)
                    sample.board_checker()
                    stddraw.clear()
                    sample.draw_board()
                    stddraw.show(200)
                    sample.match_handler()
                    stddraw.clear()
                    sample.draw_board()
                    stddraw.show(200)

                else:

                        temp= sample.tafobj[firstx][firsty]
                        sample.tafobj[firstx][firsty]=sample.tafobj[secondx][secondy]
                        sample.tafobj[secondx][secondy]=temp
                        stddraw.clear()
                        sample.draw_board()
                        stddraw.show(300)
                if sample.score_count >= 500:
                    Game = False




            mouseclick = 0
