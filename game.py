from email import message
from http import client


class tic_tac:
    
    def __init__():
        board = board=[0,0,0,0,0,0,0,0,0]
    
    # Displaying the current state of the board
    @client.command()
    async def display(self, ctx, board):
        message = 'Current State of Board:'
        for i in range(0,9):
            if ((i > 0) and (i%3) == 0):
                message = message + '\n'
            match(board[i]):
                case  0  : message += '- '
                case  1  : message += 'O '
                case -1  : message += 'X '
            message += '\n\n'
        await ctx.send(message)
    #This function takes the user move as input and make the required changes on the board.    
    @client.command()
    async def User1Turn(self, ctx ,board):
        await ctx.send('Enter X\'s position from [1...9]:')
        if(board[ctx-1] != 0):
            await ctx.send('Wrong move!!! Enter again ')
            self.User1Turn(board)
        board[ctx-1] = -1
    
    def analyzeboard(board):
        def analyzeboard(board):
        cb=[[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

        for i in range(0,8):
            if(board[cb[i][0]] != 0 and
            board[cb[i][0]] == board[cb[i][1]] and
            board[cb[i][0]] == board[cb[i][2]]):
                return board[cb[i][2]];
        return 0

    #minmax
    def minimax(self, board, player):
        x = analyzeboard(board)
        if(x != 0):
            return (x * player)
        pos = -1
        value = -2
        for i in range(0,9):
            if(board[i] == 0):
                board[i] = player
                score = -(self.minimax(board,(player*-1)))
                if(score > value):
                    value = score
                    pos = i
                board[i] = 0
        if(pos == -1):
            return 0
        return value

    def CompTurn(board):
        pos = -1
        value = -2
        for i in range(0,9):
            if(board[i] == 0):
                board[i] = 1
                score = -minimax(board, -1)
                board[i] = 0
                if(score > value):
                    value = score
                    pos = i
    
        board[pos] = 1

    async def play_game(self):
        for i in range(0,9):
            if(analyzeboard(board) != 0):
                break
            if((i + 1) % 2 == 0):
                CompTurn(board)
            else:
                self.display(board)
                self.User1Turn(board)
        
        x=analyzeboard(board)
        if(x==0):
            self.display(board)
            print("Draw!!!")
        if(x==-1):
            self.display(board)
            print("X Wins!!! O Loose !!!")
        if(x==1):
            self.display(board)
            print("O Wins!!! X Loose !!!")
