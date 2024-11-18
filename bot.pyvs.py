import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix="!",intents=intents)

@client.event
async def on_ready(self):
        print(f'Logged on as {self.user}!')

async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')




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



client.run('discord token')

