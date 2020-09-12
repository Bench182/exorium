import discord
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    prefixes = ['p/', 'pp ']
    
    return commands.when_mentioned_or(*prefixes)(bot, message)
