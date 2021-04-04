import stddraw
import math
import ticboard

x = [[0 for i in range(3)] for j in range(3)]
xoro=1
turn = 0

while turn < 9:
    if turn % 2 == 0:
        xoro = 1
    else:
        xoro = 2
    stddraw.clear()
    ticboard.drawboard(x,str(xoro))
    coord=ticboard.mouse_pressed(x)
    x[coord[0]][coord[1]]=xoro
    if ticboard.winChecker(x,1):
        ticboard.xwins()
        break
    elif ticboard.winChecker(x,2):
        ticboard.owins()
        break
    turn += 1
if turn == 9:
    ticboard.draw()
