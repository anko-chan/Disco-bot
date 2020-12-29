import asyncio

import discord
import youtube_dl
#import ffmpeg

from discord.ext import commands

from config import Config

con = Config()


# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}


ffmpeg_options = {
    'options': '-vn'
}


ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            if channel is not None:
                return await ctx.voice_client.move_to(channel)
            else:
                return await ctx.voice_client.move_to(ctx.author.voice.channel)

        else:
            await ctx.author.voice.channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query + ".mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(query))

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("音声チャンネルに接続してください")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    @commands.command()
    async def vol(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("通話に接続していません")

        ctx.voice_client.source.volume = volume / 10
        vol_out_txt = "volume:"
        for i in range(volume):
            vol_out_txt += "■"
        for i in range(10 - volume):
            vol_out_txt += "□"
        await ctx.send(vol_out_txt)
