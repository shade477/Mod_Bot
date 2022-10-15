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