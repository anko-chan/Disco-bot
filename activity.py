import discord
from discord.ext import commands
from config import Config
from dbcontrol import Memberdb
import random

class Activity (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addme(self, ctx):
        
