import discord
from discord.ext import commands
import config
from outsources import functions


class Botrelated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Commands | `p/`, `p?`', color=config.color)
        embed.add_field(name="**<a:yoshiban:753151857852940309> Moderation**", value="`ban` `unban` `kick`\n`softban` `warn` `warnings`", inline=True)
        embed.add_field(name="**<a:TPKProtogenDance:728615119910862898> Bot Related**", value="`help` `ping` `invite` `stats` `links` `info`", inline=True)
        embed.add_field(name="**<a:pikaxe:753164460184830013> Utils**", value="`get_id` `avatar` `serverinfo` `random` `poll` `decide` `say` `say2`", inline=True)
        embed.add_field(name="**<a:tacklehug:753169705862430772> Social**", value="`hug` `snuggle` `boop`\n `kiss` `pat` `cuddle`\n `askproto` `lick` `blush`\n`feed` `glomp` `happy`\n`highfive` `wag`", inline=True)
        embed.add_field(name="**<a:Toothlessuhmwhat:753170277915164672> NSFW**", value="`e621`", inline=True)
        embed.add_field(name="**<a:TPK_ProtoBoop:740828362045653073> Developers**", value="[NeoGames#5108](https://github.com/FireGamingYT/)\n[ChosenFate#5108](https://github.com/Chosen-Fate)", inline=True)
        embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
        embed.set_footer(text="Do ?info {command} for command info/usage")
        await ctx.send(embed=embed)
        await functions.logging(ctx, "help", self)


    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(color=config.color)
        embed.add_field(name="<a:loadingbounce:753173725263822858> ping", value=f'**{bot.latency:.2f}**s', inline=True)
        await ctx.send(embed=embed)
        await functions.logging(ctx, "ping", bot)

def setup(bot):
    bot.add_cog(Botrelated(bot))
