import random

def rulebased(board, turn):
    #global count_label, turn
    ####이 부분이 우리가 건드릴 핵심 영역입니다.

    ### AI 수비
    if(turn == 2):
        ### ↘방향
        for x in range(0, 17):
            for y in range(0, 17):
                if (board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and turn == 2):
                    try:
                        if (board[x + 3][y + 3] == 0):
                            board[x + 3][y + 3] = 2
                            turn = 1

                    except: # 이런식으로 예외 처리하면 오류 종류에 상관없이 발생하기만 하면 except 블록을 수행한다.
                        # 맨 밑줄에 3개 대각선 오른쪽 아래로 나열하게 될 경우에 대한 예외 처리
                        if (y > 0 and board[x - 1][y - 1] == 0):
                            board[x - 1][y - 1] = 2
                            turn = 1
        for x in range(0,16):
            for y in range(0,16):
                if(board[x][y]==1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1 and turn == 2):
                    try:
                        if(board[x+4][y+4] == 0 ):
                            board[x+4][y+4] = 2
                            turn = 1
                        elif(x>0 and board[x-1][y-1]==0):
                            board[x-1][y-1] = 2
                            turn = 1
                    except:
                        if(y>0 and board[x-1][y-1] ==0):
                            board[x-1][y-1] = 2
                            turn = 1
        ### -> 방향
        for x in range(0,17):
            for y in range(0,17):
                if(board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and turn == 2):
                    try:
                        if(board[x+3][y] == 0):
                            board[x+3][y] = 2
                            turn = 1
                    except:
                        if(x>0 and board[x-1][y] ==0):
                            board[x-1][y] = 2
                            turn = 1
        for x in range(0,16):
            for y in range(0,16):
                if(board[x][y]==1 and board[x+1][y] == 1 and board[x+2][y]==1 and board[x+3][y]==1 and turn == 2):
                    try:
                        if(board[x+4][y]==0):
                            board[x+4][y] = 2
                            turn = 1
                        elif(x>0 and board[x-1][y] == 0):
                            board[x-1][y] = 2
                            turn = 1
                    except:
                        if(y>0 and board[x-1][y]==0):
                            board[x-1][y]=2
                            turn = 1

        ### ↓방향
        for x in range(0,19):
            for y in range(0,17):
                if(board[x][y] == 1 and board[x][y+1] ==1 and board[x][y+2]==1 and turn == 2):
                    try:
                        if(board[x][y+3]==0):
                            board[x][y+3] = 2
                            turn = 1
                    except:
                        if(y>0 and board[x][y-1] == 0):
                            board[x][y-1] = 2
                            turn = 1

        for x in range(0,19):
            for y in range(0,16):
                if(board[x][y]==1 and board[x][y+1]==1 and board[x][y+2] == 1 and board[x][y+3] ==1 and turn == 2):
                    try:
                        if(board[x][y+4] == 0):
                            board[x][y+4] = 2
                            turn = 1
                        elif(x>0 and board[x][y-1]==0):
                            board[x][y-1] = 2
                            turn = 1
                    except:
                        if(y>0 and board[x][y-1]==0):
                            board[x][y-1] = 2
                            turn = 1

        #### ↙방향
        for x in range(0,19):
            for y in range(0,17):
                if(board[x][y] == 1 and board[x-1][y+1] ==1 and board[x-2][y+2] ==1 and turn == 2 ):
                    try:
                        if(board[x+1][y-1] == 0 ):
                            board[x+1][y-1] = 2
                            turn = 1
                    except:
                        if(y < 16 and board[x-3][y+3] == 0):
                            board[x-3][y+3] = 2
                            turn = 1

        for x in range(3,19):
            for y in range(0,16):
                if(board[x][y]==1 and board[x-1][y+1] == 1 and board[x-2][y+2] ==1 and board[x-3][y+3] == 1 and turn  == 2):
                    try:
                        if(board[x+1][y-1]==0):
                            board[x+1][y-1]=2
                            turn = 1
                        elif(x>0 and board[x-4][y+4]==0):
                            board[x-4][y+4]=2
                            turn = 1
                    except:
                        if(y>0 and y < 15 and board[x-4][y+4]==0):
                            board[x-4][y+4]=2
                            turn = 1
        # AI 공격
        # AI말이 3개 연속으로 있으면 두고, 4개 연속으로 있으면 두겠다.
        ### ↘방향 3개
        for x in range(0,17):
            for y in range(0,17):
                if(board[x][[y]==2 and board[x+1][y+1] ==2 and board[x+2][y+2]==2 and turn ==2]):
                    try:
                        if(board[x+3][y+3]==0):
                            board[x+3][y+3]=2
                            turn = 1
                    except:
                        if(y>0 and board[x-1][y-1]==0):
                            board[x-1][y-1]=2
                            turn = 1
        ### ↘방향 4개
        for x in range(0,16):
            for y in range(0,16):
                if(board[x][y]==2 and board[x+1][y+1]==2 and board[x+2][y+2]==2 and board[x+3][y+3]==2 and turn == 2):
                    try:
                        if(board[x+4][y+4]==0):
                            board[x+4][y+4]=2
                            turn = 1
                        elif(x>0 and board[x-1][y-1]==0):
                            board[x-1][y-1]=2
                            turn = 1
                    except:
                        if(y>0 and board[x-1][y-1]==0):
                            board[x-1][y-1]=2
                            turn = 1
        ### -> 방향 3개
        for x in range(0,17):
            for y in range(0,17):
                if(board[x][y]==2 and board[x+1][y] ==2 and board[x+2][y]==2 and turn ==2):
                    try:
                        if(board[x+3][y]==0):
                            board[x+3][y]=2
                            turn = 1

                    except:
                        if(x>0 and board[x-1][y]==0):
                            board[x-1][y-1]=2
                            turn = 1
        ### -> 방향 4개
        for x in range(0,16):
            for y in range(0,16):
                if(board[x][y]==2 and board[x+1][y+1]==2 and board[x+2][y+2] ==2 and board[x+3][y+3]==2 and turn == 2):
                    try:
                        if(board[x+4][y]==0):
                            board[x+4][y]=2
                            turn =1
                        elif(x>0 and board[x-1][y]==0):
                            board[x-1][y]=2
                            turn = 1
                    except:
                        if(y>0 and board[x-1][y]==0):
                            board[x-1][y]=2
                            turn = 1
        #### ↓방향 3개
        for x in range(0,19):
            for y in range(0,17):
                if(board[x][y]==2 and board[x][y+1]==2 and board[x][y+2]==2 and turn == 2):
                    try:
                        if(board[x][y+3]==0):
                            board[x][y+3]=2
                            turn = 1
                    except:
                        if(y>0 and board[x][y-1] ==0):
                            board[x][y-1]=2
                            turn = 1
        #### ↓방향 4개
        for x in range(0,19):
            for y in range(0,16):
                if(board[x][y]==2 and board[x][y+1]==2 and board[x][y+2] ==2 and board[x][y+3]==2 and turn == 2):
                    try:
                        if(board[x][y+4] ==0):
                            board[x][y+4]=2
                            turn = 1
                        elif(x>0 and board[x][y-1]==0):
                            board[x][y-1]=2
                            turn = 1
                    except:
                        if(y>0 and board[x][y-1]==0):
                            board[x][y-1]=2
                            turn = 1
        #### ↙방향 3개
        for x in range(2,19):
            for y in range(0,17):
                if(board[x][y]==2 and board[x-1][y+1]==2 and board[x-2][y+2]==2 and turn == 2):
                    try:
                        if(board[x+1][y-1]==0):
                            board[x+1][y-1]=2
                            turn = 1
                    except:
                        if(y > 16 and board[x-3][y+3]==0):
                            board[x-3][y+3]=2
                            turn = 1
        #### ↙방향 4개
        for x in range(3,19):
            for y in range(0,16):
                if(board[x][y]==2 and board[x-1][y+1]==2 and board[x-2][y+2]==2 and board[x-3][y+3] ==2 and turn ==2 ):
                    try:
                        if(board[x+1][y-1]==0):
                            board[x+1][y-1]=2
                            turn = 1
                        elif(x>0 and board[x-4][y+4]==0):
                            board[x-4][y+4]=2
                            turn = 1
                    except:
                        if(y> 0 and y < 15 and board[x-4][y+4]==0):
                            board[x-4][y+4]=2
                            turn = 1



        if(turn!=1):
            movelist = list()
            countlist = list()
            for a in range(1,18):
                for b in range(1,18):
                    count = 0
                    if(board[a][b]!=0):
                        pass # 아무것도 하지 않고 지나가겠다.
                    else:
                        if(board[a-1][b-1]==2):
                            count = count+1
                        if(board[a][b-1]==2):
                            count = count+1
                        if(board[a+1][b-1]==2):
                            count = count+1
                        if(board[a-1][b]==2):
                            count = count+1
                        if(board[a+1][b]==2):
                            count = count+1
                        if(board[a-1][b+1]==2):
                            count = count+1
                        if(board[a+1][b+1]==2):
                            count = count+1
                        xymove = str(a)+','+str(b)
                        movelist.append(xymove)
                        countlist.append(count)
            move = countlist.index(max(countlist))
            splitposition = movelist[move].split(',') # x,y좌표가 배열로 ['3','4']이런식으로 split되어 들어가게 된다.
            if(move == 0): # 경기 초반에는 둘려쌓여있는 말이 별로 없으므로
                indexx = 0
                indexy = 0
                for c in range(0,19):
                    for d in range(0,19):
                        if(board[c][d]==1):
                            indexx = c
                            indexy = d
                movepm = [-1,1,0]
                var1 = movepm[random.randint(0,2)]
                if(var1 == 0):
                    var2 = movepm[random.randint(0,1)]
                else:
                    var2 = movepm[random.randint(0,2)]
                indexx = indexx + var1
                indexy = indexy + var2
                if (indexx < 19 and indexy < 19):
                    splitposition[0] = str(indexx)
                    splitposition[1] = str(indexy)
                #count_label.set_text(splitposition[0])
            positionx = int(splitposition[0])
            positiony = int(splitposition[1])
            board[positionx][positiony] = 2
            turn = 1
            #count_label.set_text("your turn")
        else:
            pass


