import discord
from discord.ext.commands import Bot
from discord.ext import commands
from modules import webpage_module as web

BOT_PREFIX = ("table ")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Variaveis iniciais
ligas = ['CBLOL','LCS','LPL','LEC','LCK']
command = ""

# Gerenciar os Comandos
def commandManager(nome: str, question:bool):
    command = client.get_command(nome)

    if question == False:

        command.update(enabled=False)
    else:
        
        command.update(enabled=True)

# Tabelas específicas de cada região (Só regiões Major e o CBLOL)
@client.command(name='cblol',
                pass_context=True)
async def cblol(ctx, *args):
    actualServer = ctx.message.guild

    await ctx.message.channel.send(file=discord.File('images/cblol.png'), content="Tá na mão, Tabela do CBLOL!")

@client.command(name='lck',
                pass_context=True)
async def lck(ctx, *args):
    actualServer = ctx.message.guild
    
    await ctx.message.channel.send(file=discord.File('images/lck.png'), content="Tá na mão, Tabela da LCK!")

@client.command(name='lpl',
                pass_context=True)
async def lpl(ctx, *args):
    actualServer = ctx.message.guild

    await ctx.message.channel.send(file=discord.File('images/lpl.png'), content="Tá na mão, Tabela da LPL!")

@client.command(name='lec',
                pass_context=True)
async def lec(ctx, *args):
    actualServer = ctx.message.guild

    await ctx.message.channel.send(file=discord.File('images/lec.png'), content="Tá na mão, Tabela da LEC!")

@client.command(name='lcs',
                pass_context=True)
async def lcs(ctx, *args):
    actualServer = ctx.message.guild

    await ctx.message.channel.send(file=discord.File('images/lcs.png'), content="Tá na mão, Tabela da LCS!")

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
    
    await ctx.message.channel.send(content="Certo vou atualizar os arquivos. :cowboy: ")
    await ctx.message.channel.send(content="Durante a atualização, não vou atender ninguém! :cowboy:")
    
    
    for x in ligas:
        commandManager(x.lower(), False)
        print("Comando"+client.get_command(x.lower())+": "+client.get_command(x.lower()).enabled)

    for x in ligas:

        await web.pesquisaTabela(x)

    for x in ligas:
        commandManager(x.lower(), True)
        print("Comando"+client.get_command(x.lower())+": "+client.get_command(x.lower()).enabled)

    await ctx.message.channel.send(content="Beleza, tudo atualizado. Pode usar os comandos de novo :cowboy:")

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


client.run('XXXXXXXXXXXXXXXXXXxxxxxxxxxxxXXXXXXXXXXXXXXXX')
