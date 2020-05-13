import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
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
