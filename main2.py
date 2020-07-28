import discord
import config
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    prefixes = ['?', 'p!']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)

#initial_extensions = ['cogs.BotRelated', 'cogs.GifCommands', 'cogs.Moderation', 'cogs.Utils']

bot = commands.Bot(command_prefix=get_prefix, description='an in progress cog version of ProtoPaw')
#bot.remove_command("help")

#if __name__ == '__main__':
#    for extension in initial_extensions:
#        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}')
    await bot.change_presence(activity=discord.Game(name='Listener #e482ab4d', type=1))
    print(f"\n{bot.user.name} sucessfully booted. listener #e482ab4d")

@bot.event
async def on_message(message):

    if "kyoot" in message.content:
        await message.channel.send("no u")

    if "cute" in message.content:
        await message.channel.send("no u")
    await bot.process_commands(message)
		
bot.run(config.token, bot=True, reconnect=True)
