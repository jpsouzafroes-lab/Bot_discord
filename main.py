import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

"""Comando para legal"""
@bot.group()
async def legal(ctx):

    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@legal.command(name='João')
async def _bot(ctx):
    await ctx.send('Sim, João é legal')

@legal.command(name='Guto')
async def _bot(ctx):

    await ctx.send('Não, Guto não é legal')

@legal.command(name='Aline')
async def _bot(ctx):

    await ctx.send('Não, Aline não é legal')

""""Repetir palavras"""
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

bot.run("")
