import discord
from discord.ext.commands import Bot
from discord.ext import commands
from modules import webpage_module

BOT_PREFIX = ("tabela ")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='cblol',
                pass_context=True)
async def cblol(ctx, *args):
    actualServer = ctx.message.guild
    
    webpage_module.printaTabela("CBLOL")

    await ctx.message.channel.send(file=discord.File('cortado.png'), content="Tá na mão, Tabela do CBLOL!")

@client.command(name='lck',
                pass_context=True)
async def lck(ctx, *args):
    actualServer = ctx.message.guild
    
    webpage_module.printaTabela("LCK")

    await ctx.message.channel.send(file=discord.File('cortado.png'), content="Tá na mão, Tabela da LCK!")

@client.command(name='lpl',
                pass_context=True)
async def lpl(ctx, *args):
    actualServer = ctx.message.guild
    
    webpage_module.printaTabela("LPL")

    await ctx.message.channel.send(file=discord.File('cortado.png'), content="Tá na mão, Tabela da LPL!")

@client.command(name='lec',
                pass_context=True)
async def lec(ctx, *args):
    actualServer = ctx.message.guild
    
    webpage_module.printaTabela("LEC")

    await ctx.message.channel.send(file=discord.File('cortado.png'), content="Tá na mão, Tabela da LEC!")

@client.command(name='lcs',
                pass_context=True)
async def lcs(ctx, *args):
    actualServer = ctx.message.guild
    
    webpage_module.printaTabela("LCS")

    await ctx.message.channel.send(file=discord.File('cortado.png'), content="Tá na mão, Tabela da LCS!")

client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
