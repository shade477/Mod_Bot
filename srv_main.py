import discord 
import os 


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents) 


@client.event 
async def on_ready():
    print('login succeded in as {}'.format(client))


@client.event 
async def on_message(message):
    # same
    if message.author == client.user:
        return 

    # diff
    if message.content.startswith('$hello'):
        await message.channel.send('Hello fellow user')
        
client.run('MTAzMDg3NjQzNjU2NDgxOTk2OA.GrgHzJ.hgb-6a6SEkSpqdnL-hKe-X5BUATqtp5I5wWiIc')

@client.event
async def tic_tac():
    #Displaying the current state of the board
    def ConstBoard(board):
        print("Current State Of Board : \n\n");
        for i in range (0,9):
            if((i>0) and (i%3)==0):
                print("\n")
            if(board[i]==0):
                print("- ",end=" ")
            if (board[i]==1):
                print("O ",end=" ")
            if(board[i]==-1):    
                print("X ",end=" ")
        print("\n\n")
        
    #This function takes the user move as input and make the required changes on the board.
    def User1Turn(board):
        pos=int(input("Enter X's position from [1...9]: "))
        if(board[pos-1] != 0):
            print("Wrong move!!! Enter again ")
            UserTurn(board)
        board[pos-1]=-1
        
    def User2Turn(board):
        pos=int(input("Enter O's position from [1...9]: "))
        if(board[pos-1]!=0):
            print("Wrong Move!!! Enter again")
            User2Turn(board)
        board[pos-1]=1
    #Minimax function
    def minimax(board, player):
        x=analyzeboard(board)
        if(x!=0):
            return (x*player)
        pos=-1
        value=-2
        for i in range(0,9):
            if(board[i]==0):
                board[i]=player
                score=-minimax(board,(player*-1))
                if(score>value):
                    value=score
                    pos=i
                board[i]=0
        if(pos==-1):
            return 0
        return value    


    def CompTurn(board):
        pos=-1;
        value=-2;
        for i in range(0,9):
            if(board[i]==0):
                board[i]=1
                score=-minimax(board, -1)
                board[i]=0
                if(score>value):
                    value=score;
                    pos=i;
    
        board[pos]=1;


    #This function is used to analyze a game.
    def analyzeboard(board):
        cb=[[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]];

        for i in range(0,8):
            if(board[cb[i][0]] != 0 and
            board[cb[i][0]] == board[cb[i][1]] and
            board[cb[i][0]] == board[cb[i][2]]):
                return board[cb[i][2]];
        return 0;

    # main
    choice=int(input("Enter 1 for single player, 2 for multiplayer: "))
        #initializing the board position values to zero
        #Taking X as -1 and O as 1
        board=[0,0,0,0,0,0,0,0,0]
        if(choice==1):
            print("Computer: O vs Player: X")
            player=int(input("Enter to play 1(st) or 2(nd) : "))
            for i in range(0,9):
                if(analyzeboard(board)!=0):
                    break
                if((i+player)%2==0):
                    CompTurn(board)
                else:
                    ConstBoard(board)
                    User1Turn(board)
        
        
        else:
            for i in range(0,9):
                if(analyzeboard(board)!=0):
                    break
                if(i%2==0):
                    ConstBoard(board)
                    User1Turn(board)
                else:
                    ConstBoard(board)
                    User2Turn(board)
        
        
        x=analyzeboard(board)
        if(x==0):
            ConstBoard(board)
            print("Draw!!!")
        if(x==-1):
            ConstBoard(board)
            print("X Wins!!! O Loose !!!")
        if(x==1):
            ConstBoard(board)
            print("O Wins!!! X Loose !!!")