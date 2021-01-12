import discord
from discord.ext import commands
from config import Config
from dbcontrol import Memberdb
import random

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addme(self, ctx):
        db = Memberdb(str(ctx.guild.id))

        newface = db.addMember(ctx.author.name, ctx.author.id)

        if newface:
            await ctx.send("Hello, nice to meet you, {0}.".format(ctx.author.name))

        else:
            await ctx.send("I already know you, {0}.".format(ctx.author.name))
