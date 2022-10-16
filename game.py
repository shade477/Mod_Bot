import discord
import os 
import random
from discord.utils import get 
from discord.ext import commands


client = commands.Bot(intents=discord.Intents.all(),command_prefix='/') 

board=[0,0,0,0,0,0,0,0,0]
    
# Displaying the current state of the board
@client.command()
async def display(ctx):
    message = 'Current State of Board:'
    for i in range(0,9):
        if ((i > 0) and (i%3) == 0):
            message = message + '\n'
        if(board[i] == 0):
            message += ('- ')
        if (board[i] == 1):
            message += 'O '
        if(board[i] == -1):    
            message += 'X '
        message += '\n\n'
    await ctx.send(message)
    
    
#This function takes the user move as input and make the required changes on the board.    
@client.command()
async def p1turn(ctx, message):
    
    await ctx.send('Enter X\'s position from [1...9]:')
    p_moves = message.content
    if(board[p_moves-1] != 0):
        await ctx.send('Wrong move!!! Enter again ')
        p1turn(ctx,board)
    board[p_moves-1] = -1
    
# def analyzeboard(self):
def analyzeboard():
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
def minimax(player):
    x = analyzeboard()
    if(x != 0):
        return (x * player)
    pos = -1
    value = -2
    for i in range(0,9):
        if(board[i] == 0):
            board[i] = player
            score = -(minimax((player*-1)))
            if(score > value):
                value = score
                pos = i
            board[i] = 0
    if(pos == -1):
        return 0
    return value

def CompTurn():
    pos = -1
    value = -2
    for i in range(0,9):
        if(board[i] == 0):
            board[i] = 1
            score = -(minimax(-1))
            board[i] = 0
            if(score > value):
                value = score
                pos = i

    board[pos] = 1

@client.command()
async def play_game(ctx):
    for i in range(0,9):
        if(analyzeboard() != 0):
            break
        if((i + 1) % 2 == 0):
            CompTurn()
        else:
            display()
            p1turn()
    
    x=analyzeboard()
    if(x==0):
        display()
        print("Draw!!!")
    if(x==-1):
        display()
        print("X Wins!!! O Loose !!!")
    if(x==1):
        display()
        print("O Wins!!! X Loose !!!")

client.run('MTAzMDg3NjQzNjU2NDgxOTk2OA.GlwBGj.uvNKFBAhfB5R4R_GwADJpsxr2-SX2QfNa_uiME')