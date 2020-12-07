import discord
from discord.ext import commands
import configparser
import random

import os
import errno
import logging

from general_commands import General
from config import Config
from sounds import Music

#logger-------------------------------------------
client = discord.Client()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
#--------------------------------------------------


"""
#____________________________________
#config読み込みと各種セットアップ
#____________________________________
config = configparser.ConfigParser()
config_ini_path = 'settings.ini'
#configファイルがない場合のエラー
if not os.path.exists(config_ini_path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)

config.read(config_ini_path, encoding='utf-8')


#権限設定取得
boss = config['Boss']['BossID']
"""

con = Config()

bot = commands.Bot(command_prefix='!', description="this is Partyfinderbot")


#bot.run(str(Config.boss))
bot.add_cog(General(bot))
bot.add_cog(Music(bot))
bot.run(con.token)
