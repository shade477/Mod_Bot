import discord 
import os 
import random
from discord.utils import get 
from discord.ext import commands
from dotenv import load_dotenv
import wavelink
load_dotenv()

client = commands.Bot(intents=discord.Intents.all(),command_prefix='/') 

# todo depression

depresssed_env = ["death","suicide","depression","sad","anxious","miserable"]

encourged_resp = [
    "Cheer up !! , you have a day to live ",
    "Dont be sad :sed: sending you hugs !!",
    " 'Just be happy , dont be sad ' - Shade ~ 15/10/22 ",
    "Just be happy atleast you are not a bihari"
]

race = ["bihari","chapri","marwari","gujrati","mulla","muslim","katwa","bihar","bihari","bikhari"]

class Scripting_x_player(wavelink.Player):
    
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()



@client.event 
async def on_ready():
    # print('login succeded in as {}'.format(client))
    client.loop.create_task(connect_nodes())

async def connect_nodes():
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(
        bot=client,host='127.0.0.1',port=2333,password='youshallnotpass'
    )
    

# @client.event 
# async def on_message(message):
    
#     # same
#     if message.author == client.user:
#         return 

#     ms = message.content
#     # diff
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello fellow user')
        
#     if message.content.startswith('developer'):
#         await message.channel.send('By Purbayan Majumder')
    
#     if any(wrd in ms for wrd in depresssed_env):
#         await message.channel.send(random.choice(encourged_resp))
        
# join the user's channel
@client.command()
async def connect(ctx):
    voice = ctx.voice_client
    try:
        channel = ctx.author.voice.channel
    except AttributeError:
        return await ctx.send("Yo bruhhh !!!  Join a channel first ")
    if not voice:
        await ctx.author.voice.channel.connect(cls=Scripting_x_player())
    else:
        await ctx.send("Idiot I am already in channel ---> {}".format(channel))
        
# play func
@client.command()
async def play(ctx, *, search: wavelink.YouTubeTrack):
    voice = ctx.voice_client
    if not voice :
        script_player = Scripting_x_player()
        voice: script_player =  await ctx.author.voice.channel.connect(cls=Scripting_x_player)
    
    if voice.is_playing():
        voice.queue.put(item=search)
        
        await ctx.send(embed=discord.Embed(
            title=search.title,
            url=search.uri,
            author=ctx.author,
            description=f"{search.title} has been queued in {voice.channel}"
        ))
        
    else:
        await voice.play(search)
        
        await ctx.send(embed=discord.Embed(
            title=voice.source.title,
            url=voice.source.uri,
            author=ctx.author,
            description=f"{voice.source.title} is playing in {voice.channel}"
        ))
    

    
@client.command()
async def resume(ctx):
    voice = ctx.voice_client
    if voice:
        if voice.is_paused():
            await voice.resume()
        else:
            await ctx.send("Idiot nothing is paused ")
    else:
        await ctx.send("Moron I am not even connected to a channel")
    
    
    
@client.command()
async def pause(ctx):
    voice = ctx.voice_client
    if voice :
        if voice.is_playing() and not voice.is_paused():
            await voice.pause()
        else:
            await ctx.send("Nothing is playing now idiot !! ")
    else:
        await ctx.send('Moron I am not even connected to a channel')
     
    
@client.command()
async def stop(ctx):
    voice = ctx.voice_client
    if voice:
        if voice.is_playing():
            await voice.stop()
            await ctx.send('Stopping..... the music Bruhh  !!! ')
        
@client.command()
async def skip(ctx):
    voice = ctx.voice_client
    if voice:
        if not voice.is_playing():
            return await ctx.send("Nothing is playing moron!!")
        if voice.queue.is_empty:
            return await voice.stop()
        
        await voice.seek(voice.track.length * 1000)
        if voice.is_paused():
            await voice.resume()
    else:
        await ctx.send("moron connect me to a channel first")
        
@play.error
async def play_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Jeez couldnt find the track")
    else:
        await ctx.send("yO !!! JOIN A CHANNEL FIRST")
            

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Hold on !! clearing all message logs")    
    

        
client.run('MTAzMDg3NjQzNjU2NDgxOTk2OA.GjJVO_.pf0bI3lysdUzZ7JaO0RdediIU48mw3wbf5YToA')