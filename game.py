def finishcheck(board, turn):
    # ↘방향 check
    for x in range(0,15):
        for y in range(0,15):
            if(board[x][y]==1 and board[x+1][y+1]==1 and board[x+2][y+2]==1 and board[x+3][y+3]==1 and board[x+4][y+4]==1):
                turn = 3
            elif(board[x][y]==2 and board[x+1][y+1]==2 and board[x+2][y+2]==2 and board[x+3][y+3]==2 and board[x+4][y+4]==2):
                turn = 4
    # -> 방향 check
    for x in range(0,15):
        for y in range(0,19):
            if(board[x][y]==1 and board[x+1][y]==1 and board[x+2][y]==1 and board[x+3][y]==1 and board[x+4][y]==1):
                turn = 3
            elif(board[x][y]==2 and board[x+1][y]==2 and board[x+2][y]==2 and board[x+3][y]==2 and board[x+4][y]==2):
                turn = 4
    # ↓ 방향 check
    for x in range(0,19):
        for y in range(0,15):
            if(board[x][y]==1 and board[x][y+1]==1 and board[x][y+2]==1 and board[x][y+3]==1 and board[x][y+4]==1):
                turn = 3
            elif(board[x][y]==2 and board[x][y+1]==2 and board[x][y+2]==2 and board[x][y+3]==2 and board[x][y+4]==2 ):
                turn = 4


    # ↙ 방향 check
    for x in range(4,19):
        for y in range(0,15):
            if(board[x][y]==1 and board[x-1][y+1]==1 and board[x-2][y+2]==1 and board[x-3][y+3]==1 and board[x-4][y+4]==1):
                turn = 3
            elif(board[x][y]==2 and board[x-1][y+1]==2 and board[x-2][y+2]==2 and board[x-3][y+3]==2 and board[x-4][y+4]==2):
                turn = 4
    return turn