import discord
import random
import logging
import asyncio
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

from discord.ext import commands
bot = commands.Bot(command_prefix=["p!", "?"])
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Game(name="with other protogens | p!help", type=1)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Toothless is ready ^-^")
    print(f"Toothless is currently in {len(bot.guilds)} guilds")
    print('Bot has started successfully')

async def on_error(self, ctx, error):
        if self.logger is None:
            self.logger = await self.setupLogger(self.webhookId)

        error = getattr(error, 'original', error)
        
        emb = discord.Embed(title="Error", color=0xffff00)
        emb.description = str(error)
        chan = "`Direct Message`"
        gui = "Guild: [None]"
        if isinstance(ctx.channel, discord.TextChannel):
            chan = ctx.channel.name
            gui = f"Guild: {ctx.guild.name} (ID:{ctx.guild.id})"
        emb.add_field(name="Error Context", 
            value="".join([f"Message: `{ctx.message.content}` (ID: {ctx.message.id})\n",
                f"User: {ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}\n",
                f"Channel: #{chan} (ID: {ctx.channel.id})\n", 
                gui
            ])
        ) 

@bot.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")
async def latency(ctx):
  embed=discord.Embed(title="TPKP latency", color=config.color)
  embed.add_field(name="ping", value=f'**{bot.latency:.2f}**s')
  await ctx.send(embed=embed)

@bot.command(name='help')
async def links(ctx):
  embed=discord.Embed(title='Help menu - Prefixes `p!` | `?`', color=config.color)
  embed.add_field(name="**commands**", value="\n`help`\n`ping`\n`invite`\n`stats`\n`get_id`\n`av`\n`links`\n`snuggle`\n`hug`\n`pat`\n`boop`\n`kiss`\n`random`\n`info`\n`honk`\n`askreggie`\n`ban`\n`unban`", inline=True)
  embed.add_field(name="**Description**", value="`shows help menu\nshows bot latency\nbot invite link\nglobal bot stats\nget user ID\nget user avatar\nrelated links\nsnuggle someone\nhug someone\npat someone\nboop someone\nsmooch someone\nrandom selection\nshows command info\nHONKS\nAsk Reggie a question\nban a member\nunban a member`", inline=True)
  embed.add_field(name="developers:", value="`-` ChosenFate#5108\n`-` Bluewydahoosk#2923", inline=False)
  embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for being a part of The Paw Kingdom!")
  await ctx.send(embed=embed)

@bot.command(name="invite", aliases=["inv", "oauth"], brief="Shows the bot ouath link")
async def invite(ctx):
  embed=discord.Embed(title="TPKP invite link", color=config.color)
  embed.add_field(name="Invite toothless here", value="https://bit.ly/Toothlessbot")
  await ctx.send(embed=embed)

@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def statistics(ctx):
	embed=discord.Embed(title="Statistics TPKP:", description="Global Bot Statistics", color=config.color)
	embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
	embed.add_field(name="Total users", value=len(bot.users), inline=False)
	embed.add_field(name="More:", value="Coming soon...", inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def get_id(ctx, member: discord.Member):
  user_id = member.id
  await ctx.send('The user ID is %d.' % user_id)

@bot.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member=None):
    if user is None:
      user = ctx.author
    else:
      user = user
      eA = discord.Embed(title='Avatar', 
      color=config.color)
      eA.set_author(name=user, icon_url=user.avatar_url)
      eA.set_image(url=user.avatar_url)
      await ctx.send(embed=eA)

@bot.command(name='links', brief='Discord related links')
async def links(ctx):
  embed=discord.Embed(title='The Paw Kingdom Links', color=config.color)
  embed.add_field(name='Discord Server:', value="https://discord.gg/k64tAer\nhttps://discord.gg/bcjdqyn\nhttps://discord.me/thepawkingdom\nhttps://discord.st/thepawkingdom", inline=True)
  embed.add_field(name="Contact", value="ChosenFate#5108\nBluewydahoosk#2923")
#2923", inline=True)
  embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for being a part of The Paw Kingdom!")
  await ctx.send(embed=embed)

@bot.command(name="serverinfo", aliases=["servinfo", "sinfo"])
async def serverinfo(ctx):
  embed=discord.Embed(title="Server information", color=config.color)
  embed.add_field(name = "Info:", value = "Membercount:\nBots:\nRegion:\n" , inline = True)
  embed.add_field(name = "Value", value=str(len(ctx.guild.members)) + "\n7\n" + str(ctx.guild.region) + "\n", inline=True)
  embed.set_author(name = ctx.guild.name + " Statistics", url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024", icon_url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024")
  await ctx.send(embed=embed)

@bot.command(name='variable', brief='test variables')
async def variables(ctx):
  embed=discord.Embed(title='variable tests', color=config.color)
  embed.add_field(name='test:', value=str(len(ctx.guild.bots)), inline=False)
  embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  embed.set_author(name="The Paw Kingdom Links", url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1", icon_url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
  await ctx.send(embed=embed)

@bot.command(name='snuggle', brief='Snuggling, how sweet')
async def snuggle(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**snuggled**" + " " +  '**,** '.join(args) + "**, how cute!**"))
  GIFlist = gifs.SnuggleList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name='hug', brief='Fandom hug!')
async def hug(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**hugged**" + " " + '**,** '.join(args) + "**, how lovely!**"))
  GIFlist = gifs.HugList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name='pat', brief='Pats, wholesome!')
async def pat(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**pat**" + " " +  '**,** '.join(args) + "**, how beautiful!**"))
  GIFlist = gifs.PatList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name='boop', brief='Boop!')
async def boop(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " "+ "**booped**" + " " + '**,** '.join(args) + "**, so soft!**"))
  GIFlist = gifs.BoopList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name='kiss', brief='Smooch!')
async def boop(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " "+ "**smooched**" + " " + '**,** '.join(args) + "**, lovely!**"))
  GIFlist = gifs.KissList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name="lick", brief='Licking, lol')
async def boop(ctx, *args):
  author = ctx.message.author
  user_name = author.name
  if (len(args) == 0):
   return
  embed=discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " "+ "**licked**" + " " + '**,** '.join(args) + "**, tasty!**"))
  GIFlist = gifs.LickList
  GIF = random.choice(GIFlist)
  embed.set_image(url=GIF)
  await ctx.send(embed=embed)

@bot.command(name='random', brief='Randomness!')
async def randomchoice(ctx, arg1, arg2):
 Arglist = [arg1, arg2]
 await ctx.send(random.choice(Arglist))

@bot.command(name="info")
async def info(ctx, arg):
 embed=discord.Embed(title='Help menu - Prefixes `p!` | `?`', color=config.color)
 embed.add_field(name=arg, value= getattr(cmds, arg), inline=True)
 embed.add_field(name="Syntax of " + arg, value= getattr(syntax, arg), inline=True)
 embed.add_field(name="Developers:", value="`-` ChosenFate#5108\n`-` Bluewydahoosk#2923", inline=False)
 embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
 embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for being a part of The Paw Kingdom!")
 await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please fill in all the required arguments.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the sufficient permissions.")

#The below code bans
@bot.command(name = "ban")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
  if member == ctx.message.author:
   await ctx.send("You can't ban yourself, derp!")
   return
  if reason == None:
    await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
    return
  else:
   messageok = f"You have been banned from **{ctx.guild.name}** | Reason: `{reason}`"
   await member.send(messageok)
   await member.ban(reason=reason)
   embed=discord.Embed(title=f"{member} has been casted from {ctx.guild.name}!", color=config.color)
   embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
   await ctx.send(embed=embed)

@bot.command(name = "askreggie", aliases = ["ask136"])
async def askreggie(ctx, *, arg):
 answers = gifs.Askreggie
 answer = random.choice(answers)
 embed=discord.Embed(title=f"{arg} - Reggie says {answer}", color=config.color)
 await ctx.send(embed=embed)

@bot.command(name = "honk")
async def honk(ctx):
  embed=discord.Embed(title=f"{ctx.author.name.upper()} HONKED", color=config.color)
  embed.set_image(url="https://media1.tenor.com/images/31b7344a138dac565a1c31fe4a1dce78/tenor.gif?itemid=16237480")
  await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command(name = "search")
async def search(ctx, *, arg):
 data=json.loads(urllib.request.urlopen(f"https://api.giphy.com/v1/gifs/search?api_key=LobyMqIMQkNLHSsJdpeFXlIGLI96uxQ3&q={arg}&limit=25&offset=0&rating=G&lang=en").read())
 print("request")
 await ctx.send(response.content + "test")

class cmds: 
    hug = "Hugs the pinged person, kyoot!"
    snuggle = "Snuggles the pinged person, kyoot!"
    boop = "Boops the pinged person, boop!"
    kiss = "Smooches the pinged person :*"
    pat = "Pats the pinged person, good boy!"
    ping = "Displays the latency of the bo -connection lost"
    invite = "Displays the invite link to invite TPKP to your server"
    stats = "Shows some neat stats about TPKP"
    get_id = "Gets a users Discord ID"
    av = "Gets and posts avatar of the pinged person / ID works too"
    links = "Displays some links to get to The Paw Kingdom, this bots home!"
    random = "Can't make a choice? Use the random command! Only 2 options possible at this point"
    info = "You already know what this does, derp"
    honk = "HONK"
    askreggie = "Ask Reggie the almighty, and he shall give you an answer"
    unban = "Unbans the given user"
    lick = "Licks the pinged person, yum!"
    ban = "Bans the mentioned person"

class syntax: 
    hug = "`?hug @user1 @user2...`"
    snuggle = "`?snuggle @user1 @user2...`"
    boop = "`?boop @user1 @user2...`"
    kiss = "`?kiss  @user1 @user2...`"
    pat = "`?pat  @user1 @user2...!`"
    ping = "`?ping`"
    invite = "`?invite`"
    stats = "`?stats`"
    get_id = "`?get_id @user`"
    av = "`?av @user / ID`"
    links = "`links`"
    random = "`?random choice1 choice2` if spaces, use \"these\"."
    info = "`?info`"
    honk = "`?honk`"
    askreggie = "`?askreggie <Question>`"
    unban = "`?unban user#1234`"
    lick = "`?lick @user1 @user2..."
    ban = "`?ban @user1 Reason`"

import config
import gifs
import cmdinfo
 
print(discord.__version__)

bot.run(config.token)
