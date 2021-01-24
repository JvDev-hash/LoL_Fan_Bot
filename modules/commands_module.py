import discord
from discord.ext.commands import Bot
from discord.ext import commands
from modules import webpage_module

BOT_PREFIX = ("table ")
client = Bot(command_prefix=BOT_PREFIX)

def commandManager(nome):
    command = client.get_command(nome)

    if command.enabled == False:

        command.update(enabled=True)
    else:
        
        command.update(enabled=False)