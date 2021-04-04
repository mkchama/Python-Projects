



for i in range(9):
    for x in range(1,6):
         if (rows[i][x + 1] + rows[i][x] + rows[i][x - 1]) == (3 * rows[i][x]):
                  rows[i][x - 1] = 0
                  rows[i][x] = 0
                  rows[i][x + 1] = 0


trueboard = True
while trueboard:
    #draw initial board
    found_match = False
    for i in range(len(board) - 2):
        for j in range(len(board[i]) - 2):
            if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]:
                found_match = True
            elif board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]:
                found_match = True
            else:
                # don't set found_match to False!
                pass

    if not found_match: # no matches found, end the loop
        trueboard = False
mouseclick=0
game=True

while game:
    if stddraw.mousePressed():
        mouseclick+=1
        if mouseclick == 1:
            firstx= stddraw.mouseX()
            firsty= stddraw.mouseY()
        if mouseclick ==2:
            secondx= stddraw.mouseX()
            secondy= stddraw.mouseY()
            if #4 conditions difference in x 0, y1, diff in x 0, diff in y -1, diff in x 1, y 1 , -1, and y0


while game is running:
	mouse clicked?
		is this the first or second click?
			first -> store location of first click
			second -> store location of second click
				are the first and second clicks to adjacent grid tiles?
					yes -> swap their values using a 3rd temporary variable
						match found?
							while there are matches
								remove the matching tiles
								update the board by filling the holes appropriately
						match not found?
							swap them back
					no  -> don't do anything
				reset the values of first and second
