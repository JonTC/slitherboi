import discord
from discord.ext import commands

class Fun:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.content.lower() == ('hello pythonboi'):
            await self.client.add_reaction(message, '🙂')
            await self.client.send_message(message.channel, 'fuck off')
        if message.content.lower() == ('hit or miss'):
            await self.client.add_reaction(message, '👎')
            await self.client.send_message(message.channel, 'Sometimes, they do miss, human')
        if (message.content.lower() == ('brian is gey')):
            await self.client.add_reaction(message, '🍆')
            await self.client.send_message(message.channel, '😉')
        if (message.content.lower() == ('brian is gay')):
            await self.client.add_reaction(message, '🍆')
            await self.client.send_message(message.channel, '😉')

def setup(client):
    client.add_cog(Fun(client))
