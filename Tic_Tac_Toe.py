def constBoard(board):
    print("Current board\n\n");
    for i in range(0,9):
        if((i>0) and (i%3==0)):
            print("\n");
        if(board[i]==0):
            print("_",end=" ");
        if(board[i]==-1):
            print("X",end=" ");
        if(board[i]==1):
            print("O",end=" ");
    print("\n\n");

def minmax(board,player):
    x=analyzeBoard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minmax(board,(player*(-1)));
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
        
    if(pos==-1):
        return 0;
    return value;
            

def compTurn(board):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minmax(board,-1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
    board[pos]=1;

def user2Turn(board):
    pos=input("Enter O's position from 1..9:");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong move");
        exit(0);
    board[pos-1]=1;

def user1Turn(board):
    pos=input("Enter X's position from 1..9:");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong move");
        exit(0);
    board[pos-1]=-1;

def analyzeBoard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
    for i in range(0,8):
        if(board[cb[i][0]]!=0 and
           board[cb[i][0]]==board[cb[i][1]] and
           board[cb[i][0]]==board[cb[i][2]]):
            return board[cb[i][0]];        
    return 0;

def main():
    print("Welcome to Tic tac toe");
    board=[0,0,0,0,0,0,0,0,0];
    print("1 for Single player,2 for multiplayer");
    choice=input("Enter your choice:");
    choice=int(choice);
    if(choice==1):
        print("Computer:O vs You:X");
        player=input("Enter 1 for 1st chance and 2 for 2nd chance:");
        player=int(player);
        for i in range(0,9):
            if(analyzeBoard(board)!=0):
                break;
            if((i+player)%2==0):
                compTurn(board);
            else:
                constBoard(board);
                user1Turn(board);
    else:
        print("Player 1:X vs Player 2:O");
        for i in range(0,9):
            if(analyzeBoard(board)!=0):
                break;
            if(i%2==0):
                constBoard(board);
                user1Turn(board);
                
            else:
                constBoard(board);
                user2Turn(board);
               
    x=analyzeBoard(board);
    if(x==0):
        constBoard(board);
        print("It's a Draw");
        
    if(x==1):
        constBoard(board);
        print("X looses!! O won");
        
    if(x==-1):
        constBoard(board);
        print("X won!! O looses");
    
main();
