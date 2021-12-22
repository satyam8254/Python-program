def chessPlay(n,i,j,board):
    if i<0 or i>9 or j<0 or j>9:
        return 0
    if n==0:
        if board[i][j]==0:
            board[i][j]=1
            return 1
        else:
            return 0
    return chessPlay(n-1,i+2,j+1,board)+chessPlay(n-1,i+2,j-1,board)+chessPlay(n-1,i+1,j+2,board)+chessPlay(n-1,i+1,j-2,board)+chessPlay(n-1,i-1,j+2,board)+chessPlay(n-1,i-1,j-2,board)+chessPlay(n-1,i-2,j+1,board)+chessPlay(n-1,i-2,j-1,board)
i,j,n=map(int,input().split()) 
chess=[[0 for x in range(10)] for j in range(10)] 
print(chessPlay(n,i-1,j-1,chess))