import discord
import re
import asyncio
import string
import datetime

from discord.ext import commands
from bot import weebsongs
from random import randint
from itertools import cycle

respect = 0

class Fun:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        currentDT = datetime.datetime.now()
        author = message.author
        content = message.content

        if content.lower() == 'hello pythonboi':
            await self.client.add_reaction(message, '🙂')
            await self.client.send_message(message.channel, 'fuck off')
        if content.lower() == 'hit or miss':
            await self.client.add_reaction(message, '👎')
            await self.client.send_message(message.channel, 'Sometimes, they do miss')
        #br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python)
        if re.match(r'(?i)(br[ia][aei]n|eug(ene)?|jon|meats|demitri|jawad|rishi|python) is g[ae][iy]', message.content):
            await self.client.add_reaction(message, '🍆')
            await self.client.send_message(message.channel, '😉')
        if content.lower() == ('rishi shut up'):
            await self.client.send_message(message.channel, 'Yeah Rishi, shut the fuck up')
        if content.lower() == 'give me a weeb song':
            await self.client.send_message(message.channel, weebsongs[randint(0,len(weebsongs))])
        if content.lower() == 'dance for me bitch':
            await self.client.send_message(message.channel, '<.<')
            await asyncio.sleep(2)

            await self.client.send_message(message.channel, '^.^')
            await asyncio.sleep(2)

            await self.client.send_message(message.channel, '>.>')
            await asyncio.sleep(2)

            await self.client.send_message(message.channel, '^.^')
        #Jon
        if(author.id == "193444178514935808" and currentDT.month == 10 and currentDT.day == 5):
            if(currentDT.hour > 16 and currentDT.hour < 20):
                await self.client.add_reaction(message, '🎂')
            if(currentDT.hour == 16 and currentDT.second == 1):
                await self.client.send_message(message.channel,'Happy Birthday, Jon!')
        #Meats and Brian
        if((author.id == "249373239619485696" or author.id == "364082568787656708") and currentDT.month == 3 and currentDT.day == 7):
            if(currentDT.hour > 16 and currentDT.hour < 20):
                await self.client.add_reaction(message, '🎂')
            if(currentDT.hour == 16 and currentDT.second == 1):
                await self.client.send_message(message.channel,'Happy Birthday, Meats and Brian!')
        #Rishi
        if(author.id == "176186873926909953" and currentDT.month == 7 and currentDT.day == 26):
            if(currentDT.hour > 16 and currentDT.hour < 20):
                await self.client.add_reaction(message, '🎂')
            if(currentDT.hour == 16 and currentDT.second == 1):
                await self.client.send_message(message.channel,'Happy Birthday, Rishi!')
        #Eugene
        if(author.id == "424414054740787200" and currentDT.month == 9 and currentDT.day == 12):
            if(currentDT.hour > 16 and currentDT.hour < 20):
                await self.client.add_reaction(message, '🎂')
            if(currentDT.hour == 16 and currentDT.second == 1):
                await self.client.send_message(message.channel,'Happy Birthday, Eug!')
        if content.lower() == 'f':
            global respect
            respect = respect + 1
            if(respect % 10 == 0):
                await self.client.send_message(message.channel, 'Respect has been paid {} times'.format(respect))

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
    async def coinflip(self):
        if(randint(0,1) == 0):
            await self.client.say('Heads')
        else:
            await self.client.say('Tails')

    @commands.command()
    async def ccipher(self,*args):
        message = ' '.join(args[:-1])
        shift = int(args[-1])
        alpha = string.ascii_lowercase
        await self.client.say(''.join(alpha[(alpha.index(letter)+int(shift))%26] if letter in alpha else letter for letter in message.lower()))





def setup(client):
    client.add_cog(Fun(client))
