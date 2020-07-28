import gifs
import config
import discord
import random
import logging
import discord.ext
from discord.ext import commands

logger = logging.getLogger('discord')


logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix=["p!", "?"])
bot.remove_command('help')


@bot.event
async def on_ready():
    activity = discord.Game(name="in TPK | p!help", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")
async def latency(ctx):
    embed = discord.Embed(title="ProtoPaw latency", color=config.color)
    embed.add_field(name="ping", value=f'**{bot.latency:.2f}**s')
    await ctx.send(embed=embed)


@bot.command()
async def help2(ctx):
    embed = discord.Embed(title='Help menu - Prefixes `p!` | `?`', color=config.color)
    embed.add_field(name="**commands**", value="\n`help`\n`ping`\n`invite`\n`stats`\n`get_id`\n`av`\n`links`\n`snuggle`\n`hug`\n`pat`\n`boop`\n`kiss\ncuddle`\n`random`\n`info`\n`honk`\n`askprotopaw`\n`ban`\n`unban\nkick\nsoftban\npoll\ndecide\nserverinfo`", inline=True)
    embed.add_field(name="**Description**", value="`shows help menu\nshows bot latency\nbot invite link\nglobal bot stats\nget user ID\nget user avatar\nrelated links\nsnuggle someone\nhug someone\npat someone\nboop someone\nsmooch someone\ncuddle someone\nrandom selection\nshows command info\nHONKS\nask ProtoPaw a question\nban a member\nunban a member\nkick a member\nsoftban a member\ncast a poll\nask a yes/no question\nget server info`", inline=True)
    embed.add_field(name="developers:", value="`-` ChosenFate#5108\n`-` BluewytheRenegade#2923", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='commands | `?`, `p!`', color=config.color)
    embed.add_field(name="**🔨 moderation**", value="`ban` `unban` `kick` `softban`", inline=True)
    embed.add_field(name="**🤖 bot related**", value="`help` `ping` `invite` `stats` `links` `info`", inline=True)
    embed.add_field(name="**🏗️ Utils**", value="`get_id` `avatar` `serverinfo` `random` `poll` `decide`", inline=True)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)

@bot.command(name="invite", aliases=["inv", "oauth"], brief="Shows the bot ouath link")
async def invite(ctx):
    embed = discord.Embed(title="ProtoPaw invite link", color=config.color)
    embed.add_field(name="Invite ProtoPaw here", value="https://bit.ly/pawbotinv")
    await ctx.send(embed=embed)


@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def statistics(ctx):
    embed = discord.Embed(title="Statistics ProtoPaw:", description="Global Bot Statistics", color=config.color)
    embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
    embed.add_field(name="Total users", value=len(bot.users), inline=False)
    embed.add_field(name="More:", value="Coming soon...", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def get_id(ctx, member: discord.Member):
    user_id = member.id
    await ctx.send('The user ID is %d.' % user_id)


@bot.command(aliases=['av'])
async def avatar(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    else:
        user = user
        eA = discord.Embed(title='Avatar', color=config.color)
        eA.set_author(name=user, icon_url=user.avatar_url)
        eA.set_image(url=user.avatar_url)
        await ctx.send(embed=eA)


@bot.command(name='links', brief='Discord related links')
async def links(ctx):
    embed = discord.Embed(title='Protopaw Links', color=config.color)
    embed.add_field(name='Support/community discord Server:', value="https://discord.gg/k64tAer\nhttps://discord.gg/bcjdqyn\nhttps://discord.me/thepawkingdom\nhttps://discord.st/thepawkingdom", inline=True)
    embed.add_field(name="Contact", value="ChosenFate#5108\nBluewytheRenegade#2923")
    embed.add_field(name="Social media:", value="Twitter | https://twitter.com/furrycontentuvs", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)


@bot.command(name="serverinfo", aliases=["servinfo", "sinfo"])
async def serverinfo(ctx):
    embed = discord.Embed(title="Server information", color=config.color)
    embed.add_field(name="Info:", value="Membercount:\nRegion:\n", inline=True)
    embed.add_field(name="Value", value=str(len(ctx.guild.members)) + "\n" + str(ctx.guild.region) + "\n", inline=True)
    embed.set_author(name=ctx.guild.name + " Statistics", url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024", icon_url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024")
    await ctx.send(embed=embed)


@bot.command(name='variable', brief='test variables')
async def variables(ctx):
    embed = discord.Embed(title='variable tests', color=config.color)
    embed.add_field(name='test:', value=str(len(ctx.guild.bots)), inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_author(name="The Paw Kingdom Links", url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1", icon_url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    await ctx.send(embed=embed)


@bot.command(name='snuggle', brief='Snuggling, how sweet')
async def snuggle(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**snuggled**" + " " + '**,** '.join(args) + "**, how cute!**"))
    GIFlist = gifs.SnuggleList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='hug', brief='Fandom hug!')
async def hug(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**hugged**" + " " + '**,** '.join(args) + "**, how lovely!**"))
    GIFlist = gifs.HugList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='pat', brief='Pats, wholesome!')
async def pat(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**pat**" + " " + '**,** '.join(args) + "**, how beautiful!**"))
    GIFlist = gifs.PatList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='boop', aliases=['bp'], brief='Boop!')
async def boop(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**booped**" + " " + '**,** '.join(args) + "**, so soft!**"))
    GIFlist = gifs.BoopList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='kiss', aliases=['smooch'], brief='Smooch!')
async def kiss(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**smooched**" + " " + '**,** '.join(args) + "**, lovely!**"))
    GIFlist = gifs.KissList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="lick", brief='Licking, lol')
async def lick(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**licked**" + " " + '**,** '.join(args) + "**, tasty!**"))
    GIFlist = gifs.LickList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="cuddle")
async def cuddle(ctx, *args):
    if (len(args) == 0):
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**cuddled**" + " " + '**,** '.join(args) + "**, heartwarming!**"))
    GIFlist = gifs.CuddleList
    GIF = random.choice(GIFlist)
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='random', brief='Randomness!')
async def randomchoice(ctx, arg1, arg2):
    Arglist = [arg1, arg2]
    await ctx.send(random.choice(Arglist))


@bot.command(name="info")
async def info(ctx, arg):
    embed = discord.Embed(title='Help menu - Prefixes `p!` | `?`', color=config.color)
    embed.add_field(name=arg, value=getattr(cmds, arg), inline=True)
    embed.add_field(name="Syntax of " + arg, value=getattr(syntax, arg), inline=True)
    embed.add_field(name="Developers:", value="`-` ChosenFate#5108\n`-` BluewytheRenegade#2923", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please fill in all the required arguments.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the sufficient permissions.")


@bot.command(name="askprotopaw", aliases=["askpp", "askproto"])
async def askprotopaw(ctx, *, arg):
    answers = gifs.AskProtopaw
    answer = random.choice(answers)
    embed = discord.Embed(title=f"{arg} - Proto says {answer}", color=config.color)
    await ctx.send(embed=embed)


@bot.command(name="honk")
async def honk(ctx):
    embed = discord.Embed(title=f"{ctx.author.name.upper()} HONKED", color=config.color)
    embed.set_image(url="https://media1.tenor.com/images/31b7344a138dac565a1c31fe4a1dce78/tenor.gif?itemid=16237480")
    await ctx.send(embed=embed)


@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't ban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been banned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been casted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    clearname = str(user).split("#")
    embed = discord.Embed(title=f"Unbanned {clearname[0]}", color=config.color)
    embed.set_footer(text=user)
    await ctx.send(embed=embed)


@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't kick yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been kicked from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.kick(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been kicked from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name="softban")
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't softban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been softbanned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        await member.unban()
        embed = discord.Embed(title=f"{member} has been softcasted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name="poll")
async def poll(ctx, *, arg):
    await ctx.message.delete()
    choice = str(arg).split(",")
    n = 1
    reactionlist = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    embed = discord.Embed(title="Poll", color=config.color)
    for x in choice:
        embed.add_field(name="Option " + reactionlist[n-1], value=f"{x}", inline=False)
        n = n+1
    embed.set_footer(text=f"Poll cast by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    en = 1
    for emoji in reactionlist:
        await botmsg.add_reaction(emoji)
        en = en+1
        if en >= n:
            break


@bot.command(name="decide")
async def decide(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(title=arg, color=config.color)
    embed.set_footer(text=f"Asked by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("✅")
    await botmsg.add_reaction("❌")


@bot.event
async def on_message(message):
    if message.channel.id in gifs.votechannels:
        if message.attachments:
            await message.add_reaction("👍")
    await bot.process_commands(message)

 @bot.event
async def on_message(message):

    if "kyoot" in message.content:
        await message.channel.send("no u")

    if "cute" in message.content:
        await message.channel.send("no u")
    await bot.process_commands(message)

class cmds:
    hug = "Hugs the pinged person, kyoot!"
    snuggle = "Snuggles the pinged persons, kyoot!"
    boop = "Boops the pinged persons, boop!"
    kiss = "Smooches the pinged persons :*"
    pat = "Pats the pinged persons, good boy!"
    ping = "Displays the latency of the bo -connection lost"
    invite = "Displays the invite link to invite TPKP to your server"
    stats = "Shows some neat stats about TPKP"
    get_id = "Gets a users Discord ID"
    av = "Gets and posts avatar of the pinged person / ID works too"
    links = "Displays some links to get to The Paw Kingdom, this bots home!"
    random = "Can't make a choice? Use the random command! Only 2 options possible at this point"
    info = "You already know what this does, derp"
    honk = "HONK"
    askprotopaw = "Ask ProtoPaw, and he shall give you an answer"
    unban = "Unbans the given user"
    lick = "Licks the pinged persons, yum!"
    ban = "Bans the mentioned person"
    kick = "Kicks the specified person"
    softban = "Softbans (bans and unbans) the specified"
    poll = "Cast a poll if you can't agree about something!"
    decide = "Casts a simple yes / no poll"
    cuddle = "Cuddle the pinged persons"


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
    ban = "`?ban @user | ID Reason`"
    kick = "`?kick @user | ID reason`"
    softban = "`?softban @user | ID reason"
    poll = "`?poll choice1, choice2, choice3 [...]`"
    decide = "`?decide <question>"
    cuddle = "?cuddle @user1 @user2...`"


print(discord.__version__)

bot.run(config.token)
