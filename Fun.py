import discord
import re
import asyncio
import string

from discord.ext import commands
from bot import weebsongs
from random import randint
from itertools import cycle


class Fun:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.content.lower() == 'hello pythonboi':
            await self.client.add_reaction(message, '🙂')
            await self.client.send_message(message.channel, 'fuck off')
        if message.content.lower() == 'hit or miss':
            await self.client.add_reaction(message, '👎')
            await self.client.send_message(message.channel, 'Sometimes, they do miss')
        #br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python)
        if re.match(r'(?i)(br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python) is g[ae][iy]', message.content):
            await self.client.add_reaction(message, '🍆')
            await self.client.send_message(message.channel, '😉')
        if (message.content.lower() == ('rishi shut up')):
            await self.client.send_message(message.channel, 'Yeah Rishi, shut the fuck up')
        if(message.content.lower() == 'give me a weeb song'):
            await self.client.send_message(message.channel, weebsongs[randint(0,len(weebsongs))])
    @commands.command()
    async def ping(self):
        #client.say can only be used in a command, while client.send_message can be used in commands and events
        #not passed in a channel, sends message to channel that it was called in
        await self.client.say('Pong!')
    @commands.command()
    async def weeb(self):
        await self.client.say(weebsongs[randint(0,len(weebsongs))])

    @commands.command()
    # *args lets you pass in an infinite amount of arguments into the command, returns tuple of all arguments passed into command
    async def echo(self,*args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await self.client.say(output)


    @commands.command(pass_context=True)
    async def clear(self,ctx,amount=5):
        channel = ctx.message.channel
        if(amount<0):
            await self.client.say("Can't bring messages back, srry")
        else:
            await self.client.purge_from(channel, limit=int(amount+1))
            await asyncio.sleep(1)
            await self.client.say('{} message(s) deleted'.format(amount))


    @commands.command()
    async def annoy(self,*, member : discord.Member):
        for n in range(5):
            await self.client.say("wake the fuck up <@{}>".format(member.id))
            await asyncio.sleep(1)

    @commands.command()
    async def ccipher(self,*args):
        message = ' '.join(args[:-1])
        shift = int(args[-1])
        alpha = string.ascii_lowercase
        await self.client.say(''.join(alpha[(alpha.index(letter)+int(shift))%26] if letter in alpha else letter for letter in message.lower()))





def setup(client):
    client.add_cog(Fun(client))
