import discord
from discord.ext import commands
from config import Config
from dbcontrol import Memberdb
import random

con = Config()

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "botと友達になります")
    async def addme(self, ctx):
        db = Memberdb(str(ctx.guild.id))

        newface = db.addMember(ctx.author.name, ctx.author.id)

        if newface:
            await ctx.send("Hello, nice to meet you, {0}.".format(ctx.author.name))
        else:
            await ctx.send("I already know you, {0}.".format(ctx.author.name))
            await ctx.message.delete()

    @commands.command(hidden = True)
    async def showrating(self,ctx):
        if ctx.author.id == int(con.boss):
            db = Memberdb(str(ctx.guild.id))

            list = db.getRatingList()
            returninglines = "name | rating\n"

            for line in list:
                returninglines += line[0] + " | " + str(line[1]) + "\n "

            await ctx.author.send(returninglines)
            await ctx.message.delete()
