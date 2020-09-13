import discord
from discord.ext import commands
import sys
import traceback
import config


def get_prefix(bot, message):
    prefixes = ['p/', 'pp ']
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.bot']

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}, {e}', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    activity = discord.Game(name=f'with {len(bot.users)} furs', type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('ProtoPaw has started successfully')
    print('-----------')
    print('guilds:')
    print(len(bot.guilds))
    print('-----------')
    print('users:')
    print(len(bot.users))
    print('-----------')
    print('version:')
    print(discord.__version__)
    print('-----------')

bot.run(config.token)
