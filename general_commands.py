import discord
from discord.ext import commands
from config import Config
import random

import os

con = Config()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = True)
    async def shutdown(self, ctx):
        if ctx.author.id == int(con.boss):
            await ctx.send("Shutting down...")
            await self.bot.close()
        else:
            await ctx.send("Whos's there?")

    @commands.command(help = '"!roll xDy"でDyをx個ロールします。省略で1D6をロール')
    async def roll(self, ctx, *args):

        if len(args) > 0:
            dices = args[0].split("D")
        else:
            await ctx.send("> D6 = **" + str(random.randint(1, 6)) + "**")
            return

        if len(args) == 1 and len(dices) == 2:
            # Dの前後が数字か確認
            if dices[0].isdigit() and dices[1].isdigit():

                #100D100制限
                if (int(dices[0]) > 100) or (int(dices[1]) > 100):
                    await ctx.send("100D100が最大値です")

                else:
                    rolls = 0
                    results = [0]

                    #roll, 数記憶
                    for i in range(int(dices[0]) - 1):
                        rolls = random.randint(1, int(dices[1]))
                        results[0] += rolls
                        results.append(str(rolls) + "+")
                        print(str(rolls) + "+",end="")

                    rolls = random.randint(1, int(dices[1]))
                    results[0] += rolls
                    results.append(str(rolls) + "= **" + str(results[0]) + "**")
                    print(str(rolls) + "= " + str(results[0]))

                    #ひとまとめにして出力
                    del results[0]
                    await ctx.send("> " + str(dices[0]) + "D" + str(dices[1]) + " =\n> " + "".join(results))

        else:
            await ctx.send("「!roll」でD6一つ、「!roll xDy」でDyをx個ロール")
