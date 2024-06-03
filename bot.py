import discord
import os

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready ():
    print(f'Você está logado como {client.user})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Olá!')

client.run(os.getenv('TOKEN'))





