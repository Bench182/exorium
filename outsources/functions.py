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


async def logging(ctx, type):
    print(f"Command \"{type}\" was used in {ctx.channel}!")
