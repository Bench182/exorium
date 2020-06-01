import discord

from discord.ext import commands
bot = commands.Bot(command_prefix=["p!", "proto ", "tpkp ", "?"], description='TPK protogen is a work-in-progress bot for The Paw Kingdom. Its currently not 24/7 as we are still looking for a (free) host which allows that.\nPrefixes: p!, proto , tpkp , ?')

@bot.event
async def on_ready():
    activity = discord.Game(name="with other protogens | p!help", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Toothless is ready ^-^")
    print(f"Toothless is currently in {len(bot.guilds)} guilds")
    print('Bot has started successfully')

@bot.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")
async def latency(ctx):
  embed=discord.Embed(title="TPKP latency", color=0x00ff00)
  embed.add_field(name="ping", value=f'**{bot.latency:.2f}**s')
  await ctx.send(embed=embed)

@bot.command(name="invite", aliases=["inv", "oauth"], brief="Shows the bot ouath link")
async def invite(ctx):
  embed=discord.Embed(title="TPKP invite link", color=0x00ff00)
  embed.add_field(name="Invite toothless here", value="https://bit.ly/Toothlessbot")
  await ctx.send(embed=embed)

@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def statistics(ctx):
	embed=discord.Embed(title="Statistics TPKP:", description="Global Bot Statistics", color=0x00ff00)
	embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
	embed.add_field(name="Total users", value=len(bot.users), inline=False)
	embed.add_field(name="More:", value="Coming soon...", inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def get_id(ctx, member: discord.Member):
  user_id = member.id
  await ctx.send('The user id is %d.' % user_id)

@bot.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member=None):
    if user is None:
      user = ctx.author
    else:
      user = user
      
      eA = discord.Embed(title='Avatar', 
      color=discord.Color.green())
      eA.set_author(name=user, icon_url=user.avatar_url)
      eA.set_image(url=user.avatar_url)
      await ctx.send(embed=eA)

@bot.command(name="links", aliases=["link", "disc", "discord"], brief="discord related links.")
async def link(ctx):
	embed=discord.Embed(title="Discord links", description="Links related to discord&TPK.", color=config.color)
	embed.add_field(name="Discord server:", value="Permanent invite links:\n`-` https://discord.gg/bcjdqyn\n`-` https://discord.gg/xpt9qtk", inline=False)
  
	await ctx.send(embed=embed)

@bot.command(name='link1', brief='Discord related links')
async def variables(ctx):
  embed=discord.Embed(title='The Paw Kingdom Links', color=config.color)
  embed.add_field(name='Discord Server:', value="https://discord.gg/k64tAer\nhttps://discord.gg/bcjdqyn\nhttps://discord.me/thepawkingdom", inline=True)
  embed.add_field(name="Contact", value="ChosenFate#5108\nBluewydahoosk#2923")
#2923", inline=True)
  embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  embed.set_footer(text="Thank you for being a part of The Paw Kingdom!")
  await ctx.send(embed=embed)

@bot.command(name='variable', brief='test variables')
async def variables(ctx):
  embed=discord.Embed(title='variable tests', color=config.color)
  embed.add_field(name='test:', value=(config.thumbnail), inline=False)
  embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  embed.set_author(name="**The Paw Kingdom Links**", url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1", icon_url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  await ctx.send(embed=embed)

import config

print(discord.__version__)

bot.run(config.token)
