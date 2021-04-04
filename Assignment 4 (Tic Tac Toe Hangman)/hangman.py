import stddraw
import math


def drawhangman(count,wrong,word,xwrong,ywrong,xword,yword):
    stddraw.clear()

    stddraw.setXscale(-5.5,5.5)
    stddraw.setYscale(-5.5,5.5)
    stddraw.setPenRadius(0.02)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(-1,-3,2,-3)
    stddraw.line(-0.5,-3,-0.5,-2.5)
    stddraw.line(-0.5,-2.5,1.5,-2.5)
    stddraw.line(1.5,-2.5,1.5,-3)

    if count<=8:
        stddraw.setFontSize(16)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.text(xword,yword,word)
    if count<=7:
        #wrongguesses
        stddraw.setFontSize(16)
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(xwrong,ywrong,wrong)
        #head
        stddraw.setPenRadius(0.001)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.circle(0.5,0.5,0.5)
    if count<=6:
        #torso
        stddraw.setPenRadius(0.02)
        stddraw.line(0.5, -1.5, 0.5, 0)
    if count <=5:
        #left arm
        stddraw.line(0.5, -0.5, 0, -1)
    if count <=4:
        #right arm
        stddraw.line(0.5, -0.5, 1, -1)
    if count <=3:
        #left leg
        stddraw.line(0.5, -1.5, 0, -2)
    if count <=2:
        #right leg
        stddraw.line(0.5, -1.5, 1, -2)
    if count <=1:
        #gallows
        stddraw.line(1.4, -2.5, 1.4, 1.5)
        stddraw.line(1.4, 1.5, 0.5, 1.5)
        stddraw.line(0.5, 1.5, 0.5, 1)
    if count <=0:
        #face
        stddraw.setFontSize(12)
        stddraw.text(0.35,0.65,'x')
        stddraw.text(0.65,0.65,'x')
        stddraw.text(0.5,0.4,'__')
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(36)
        stddraw.text(0.5,3,'GAME OVER')
    stddraw.show(1)

def winning():
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setFontSize(36)
    stddraw.text(0.5,3,'WINNER')
    stddraw.show(1)

def gallow(xword,yword,word):
    stddraw.clear()

    stddraw.setXscale(-5.5,5.5)
    stddraw.setYscale(-5.5,5.5)
    stddraw.setPenRadius(0.02)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(-1,-3,2,-3)
    stddraw.line(-0.5,-3,-0.5,-2.5)
    stddraw.line(-0.5,-2.5,1.5,-2.5)
    stddraw.line(1.5,-2.5,1.5,-3)

    stddraw.setFontSize(16)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(xword,yword,word)
    stddraw.show(1)
