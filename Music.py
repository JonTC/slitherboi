import discord

from discord.ext import commands
from bot import players
from bot import queues
class Music:
    def __init__(self, client):
        self.client = client


    def check_queues(id):
        if queues[id] != []:
            player = queues[id].pop(0)
            players[id] = player
            player.start()

    @commands.command(pass_context=True)
    async def join(self, ctx):
        author = ctx.message.author
        channel = ctx.message.author.voice.voice_channel
        try:
            await self.client.join_voice_channel(channel)
        except:
            await self.client.say(str(author.mention) + ' fuck you, join a voice channel'.format(str(author)))

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        author = ctx.message.author
        channel = ctx.message.server
        voice_client = self.client.voice_client_in(channel)
        try:
            await voice_client.disconnect()
        except:
            await self.client.say(str(author.mention)+' join a voice channel bitch')

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        players[server.id] = player
        player.start()

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        id = ctx.message.server.id
        players[id].pause()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        id = ctx.message.server.id
        players[id].stop()

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        players[id].resume()

    @commands.command(pass_context=True)
    async def queue(self, ctx, url):
        author = ctx.message.author
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        if server.id in queues:
            queues[server.id].append(player)
            queues[server.id] = [player]
        await self.client.say(str(author.mention()) + 'Added to queue')

def setup(client):
    client.add_cog(Music(client))
