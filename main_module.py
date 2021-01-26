import discord
from discord.ext.commands import Bot
from discord.ext import commands
from modules import webpage_module as web

BOT_PREFIX = ("!")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Variaveis iniciais
ligas = ['CBLOL','LCS','LPL','LEC','LCK']
command = ""

# Tabelas específicas de cada região (Só regiões Major e o CBLOL)
@client.command(name='table',
                pass_context=True)
async def table(ctx, *args):
    actualServer = ctx.message.guild

    for liga in ligas:
        if liga == args[0].upper():

            await ctx.message.channel.send(file=discord.File('images/'+liga.lower()+'.png'), content="Olha a tabela que tu pediu aí!")
            break

# Enviar todas as tabelas de uma vez
@client.command(name='all',
                pass_context=True)
async def all(ctx, *args):
    actualServer = ctx.message.guild

    await ctx.message.channel.send(content="Calma que tu pediu muita coisa, vou mandar agora! :cowboy: ")
        
    await ctx.message.channel.send(file=discord.File('images/lcs.png'))
    await ctx.message.channel.send(file=discord.File('images/lec.png'))
    await ctx.message.channel.send(file=discord.File('images/lck.png'))
    await ctx.message.channel.send(file=discord.File('images/lpl.png'))
    await ctx.message.channel.send(file=discord.File('images/cblol.png'))

# Atualizar os arquivos das tabelas
@client.command(name='update',
                pass_context=True)
async def update(ctx, *args):
    actualServer = ctx.message.guild
    
    await ctx.message.channel.send(content="Certo vou atualizar os arquivos.")
    await ctx.message.channel.send(content="Durante a atualização, não vou atender ninguém! :cowboy:")

    for x in ligas:

        web.pesquisaTabela(x)

    await ctx.message.channel.send(content="Beleza, tudo atualizado. Pode usar os comandos de novo.")

# Champion Stats
@client.command(name='CStats',
                pass_context=True)
async def cstats(ctx, *args):

    url = web.pesquisaCStats(args[0].upper())

    await ctx.message.channel.send(content="Beleza, pesquisado: "+url)

# Player Stats
@client.command(name='PStats',
                pass_context=True)
async def pstats(ctx, *args):

    url = web.pesquisaPStats(args[0].upper())

    await ctx.message.channel.send(content="Beleza, pesquisado: "+url)

@client.event
async def on_command_error(ctx, error):
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.message.channel.send(content="Não tenho esse comando aew não, man! :cowboy: ")
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.message.channel.send(content="O Comando ta fechado, Bronze apressado! :cowboy: ")
            return

client.run('XXXXXXXXXxxxxxxxxxxxXXXXXXXXXXXXxxxxxxxxx')
