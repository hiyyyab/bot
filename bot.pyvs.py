import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!",intents=intents)

@client.event
async def on_ready():
        print(f'Logged on as {client.user}!')

async def on_message(message):
        print(f'Message from {message.author}: {message.content}')



#gifs
#punch gif
punch_gifs = ['https://media1.tenor.com/m/DznZysOV8tIAAAAd/kick-anime.gif']
punch_names = ['Punches You!']

@client.command()
async def punch(ctx):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(punch_names))}"

    )
    embed.set_image(url=(random.choice(punch_gifs)))
    await ctx.send(embed = embed)

#anya crying gif
cry_gifs = ['https://media1.tenor.com/m/0qj0aqZ0nucAAAAd/anya-spy-x-family-anime-anya-crying.gif']
cry_names = ['cry!']

@client.command()
async def cry(ctx):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(cry_names))}"

    )
    embed.set_image(url=(random.choice(cry_gifs)))
    await ctx.send(embed = embed)
#yay gif 
yay_gifs = ['https://media.tenor.com/Fi5H8EfqtFAAAAAM/yay-yeah.gif']
yay_names = ['yay!']

@client.command()
async def yay(ctx):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(yay_names))}"

    )
    embed.set_image(url=(random.choice(yay_gifs)))
    await ctx.send(embed = embed)

#titan run
run_gifs = ['https://media1.tenor.com/m/Aznjkw6cS0MAAAAd/attack-on-titan-shingeki-no-kyojin.gif']
run_names = ['run!']

@client.command()
async def run(ctx):
    embed = discord.Embed(
        colour = (discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(run_names))}"

    )
    embed.set_image(url=(random.choice(run_gifs)))
    await ctx.send(embed = embed)    

client.run('discord bot token')

