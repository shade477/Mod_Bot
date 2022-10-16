import discord 
import os 
import random
from discord.utils import get 
from discord.ext import commands
from dotenv import load_dotenv
import wavelink
from cogs import tictactoe
import asyncio
load_dotenv()

client = commands.Bot(intents=discord.Intents.all(),command_prefix='/') 

@client.event 
async def on_ready():
    print('login succeded in as {}'.format(client))
    

def playing_embed(board, challenger, opponent):
    embedPlay = discord.Embed(title="Tic Tac Toe by Purbayan", color=0xc01111)
    embedPlay.set_thumbnail(url='https://image.flaticon.com/icons/png/512/566/566294.png')
    embedPlay.add_field(name='Challenger', value=f'{challenger}', inline=True)
    embedPlay.add_field(name='Opposition', value=f'{opponent}', inline=True)
    embedPlay.add_field(name='Board', value=tictactoe.print_board(board), inline=False)
    embedPlay.set_footer(text = 'Type \n[position]\n[position] should be replaced by 2 digit number like 11 or, 23 or, 31 where first number is the row number and second is the column number')
    return embedPlay

def intro_embed():
    embedIn = discord.Embed(title="Welcome To The Game Of Tic Tac Toe", description="**Commands:**", color=0x00eeff)
    embedIn.set_author(name="Tic Tac Toe", icon_url="https://image.flaticon.com/icons/png/512/566/566294.png")
    embedIn.set_thumbnail(url="https://cdn.discordapp.com/emojis/754600266288070806.png?v=1")
    embedIn.add_field(name="1) 'tictac'", value="Get help regarding commands of bot", inline=False)
    embedIn.add_field(name="2) 'tictac [mention]'", value="Challenge the [mention] to a game of Tic Tac Toe", inline=False)
    embedIn.set_footer(text="Do not include the quotes while using the commands \nRemove the [] while mentioning someone")
    return embedIn


@client.event
async def on_message(message):

    playing = list()

    if message.author == client.user:
        return

    if message.content.startswith('hello'):
      await message.channel.send(f'Hello {message.author.mention} bihari')

    #Checks if the command has been executed
    if message.content.startswith('tictac'):

        message_parts = message.content.split(' ')


        if len(message_parts) == 1 and message_parts[0] == 'tictac':
            embedIntro = intro_embed()
            await message.channel.send(embed=embedIntro)
        
        try:
            if len(message_parts) == 2 and message_parts[1][0] == '<' and message_parts[1][-1] == '>' and  message.author.mention not in playing and message_parts[1] not in playing:
                board = tictactoe.initialize_board()
                players = tictactoe.initialize_players()
                challenger = message.author.mention
                opponent = message_parts[1]
                playing.append(challenger)
                playing.append(opponent)
                counter = 1
                validPositions = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
                embedP = playing_embed(board, challenger, opponent)
                await message.channel.send(embed=embedP)
                
                while tictactoe.validation(board, players) == 'None':
                    turn = 1 if counter % 2 != 0 else 2
                    player = challenger if turn == 1 else opponent
                    await message.channel.send(f"{player}'s Turn")
                    inpValid = False
                    while not inpValid:
                        try:
                            
                            inp = await client.wait_for('message', timeout=60.00)
                           
                            if len(inp.content) == 2 and isinstance(int(inp.content), int) and inp.content in validPositions:
                                inpValid = True

                                inp = str(inp.content)+('1' if player == challenger else '2')
                                validPositions.remove(inp[0:2])
                        except asyncio.TimeoutError:

                            await message.channel.send(f'{player} sala itna time laga diya randi chal nikal ab :*(')
                            await message.channel.send(f' Chal ei toh ajka {challenger if player == opponent else opponent} winner')
                            await message.channel.send(f':)))')
                            await message.channel.send(f'{player} Chal ei bhikari gaya !!')

                            return
                        except ValueError:

                            await message.channel.send(f'{player} unfortunately the position you gave was invalid\nAbe randi valid input dal sala !!!')

                    board = tictactoe.update_board(inp, players, board)
                    embedP = playing_embed(board, challenger, opponent)
                    await message.channel.send(embed=embedP)

                    counter += 1

                if tictactoe.validation(board, players) != 'Draw': 
                    await message.channel.send(f"{challenger if tictactoe.validation(board, players) == 'X' else opponent} is the winner")
                else:
                    await message.channel.send("Damn bihari kab se itna smart ????\nGG")

                playing.remove(challenger)
                playing.remove(opponent)

                return   
            elif message.author.mention in playing:
                await message.channel.send(f'{message.author.mention}  abe bihari phele se ei khel raha hai be\nSala isko phele khatam kar')
                return
            elif message_parts[1] in playing:
                await message.channel.send(f'Rukh randi rukhhhh tera bap abhi bhi  \n{message_parts[1]}  currently in a game')
        except IndexError:
            pass
        if len(message_parts) >= 3:
            await message.channel.send("Gawar sahi command dal sala !!!")
            
client.run('your token')