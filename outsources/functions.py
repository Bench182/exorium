import discord
import config
import random
import gifs


async def interactions(ctx, members, reason, type, ending, typespecial):
    GIFlist = getattr(gifs, type)
    GIF = random.choice(GIFlist)
    if not (members):
        return await ctx.send(f"Please specify at least one cutie to {type}!")
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + f"**{typespecial}**" + " " + '**,** '.join(x.mention for x in members) + f"**, {ending}!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


async def logging(ctx, type, bot):
    print(f"Command \"{type}\" was used in {ctx.channel} (guild {ctx.guild}) by {ctx.message.author}")
    embed = discord.Embed(title="exorium command log", color=config.color)
    embed.add_field(name="Command", value=f"`\"{type}\"`", inline=True)
    embed.add_field(name="Author", value=f"`{ctx.message.author}`", inline=True)
    embed.add_field(name="Guild", value=f"`{ctx.guild}`", inline=True)
    embed.add_field(name="Channel", value=f"`{ctx.channel}`", inline=True)
    channel = bot.get_channel(755138117488345118)
    await channel.send(embed=embed)
