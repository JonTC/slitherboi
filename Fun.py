import discord
import re
import asyncio

from discord.ext import commands
from bot import weebsongs
from random import randint
from itertools import cycle


class Fun:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        #strmsg = str(message)
        #result = strmsg.index('is gay')
        if message.content.lower() == ('hello pythonboi'):
            await self.client.add_reaction(message, '🙂')
            await self.client.send_message(message.channel, 'fuck off')
        if message.content.lower() == ('hit or miss'):
            await self.client.add_reaction(message, '👎')
            await self.client.send_message(message.channel, 'Sometimes, they do miss, human')
        #br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python)
        if re.match(r'(?i)(br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python) is g[ae][iy]', message.content):
            await self.client.add_reaction(message, '🍆')
            await self.client.send_message(message.channel, '😉')
        #basically just trying to check if it says 'is gay'
        #if message.content.lower() == ('{} is gay'.format(strmsg[0:result])):
        #    await self.client.add_reaction(message, '🍆')
        #    await self.client.send_message(message.channel, '😉')
        if (message.content.lower() == ('rishi shut up')):
            await self.client.send_message(message.channel, 'Yeah Rishi, shut the fuck up')
        if(message.content.lower() == 'bot give me a weeb song'):
            await self.client.send_message(message.channel, weebsongs[randint(0,4)])


    @commands.command(pass_context=True)
    async def annoy(self,ctx, member : discord.Member):
        for n in range(5):
            await self.client.say("wake the fuck up <@{}>".format(member.id))
            asyncio.sleep(2)
def setup(client):
    client.add_cog(Fun(client))
