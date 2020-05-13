import discord
import configparser

import os
import errno

client = discord.Client()

#____________________________________
#config読み込み
#____________________________________
config = configparser.ConfigParser()
config_ini_path = 'settings.ini'
#configファイルがない場合のエラー
if not os.path.exists(config_ini_path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)

config.read(config_ini_path, encoding='utf-8')

#権限設定取得
boss = config['Boss']['BossID']

#______________________________________

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #shutdown command for BOSS
    if message.content.startswith('!shutdown'):
        if message.author.id == int(boss):
            await message.channel.send("boss' calling")
            await client.close()
        else:
            await message.channel.send('youre not boss')
            return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


    #diceroll
    #if message.content.startswith('!roll'):
        #if message.content[6:].split("d",1)

    #FF14マクロ変換
    if message.content.startswith('!henkan'):
        line = message.content.split(" ")
        await message.channel.send(line)

client.run('NzAzNTAxMDA2NjMzMzA0MDg1.XqPgsQ.XG9Qdz5QlrMEl2xo-3ZyxIwRQzo')
