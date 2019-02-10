import discord
import asyncio
from discord.ext import commands

class Calculator:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def multiply(self, *args):
        product = 1
        for x in args:
            product = product * float(x)
        await self.client.say('The product is {}'.format(product))

    @commands.command()
    async def add(self, *args):
        sum = 0
        for x in args:
            sum = sum + float(x)
        await self.client.say('The sum is {}'.format(sum))

    #only works with 2 numbers rn
#    @commands.command()
#    async def subtract(self, *args):
#        total = 0
#        for x in args:
#            total = float(x) - total
#        await self.client.say('The total is {}'.format(total/-1))

    #dont work yet
#    @commands.command()
#    async def mod(self, value):
#        for x in args:
#            remainder = float(x)
#        await self.client.say('The remainder of {} % {} is {}'.format(a, b, remainder))

    @commands.command()
    async def timer(self, seconds):
        await asyncio.sleep(int(seconds));
        await self.client.say("Time's up")

def setup(client):
    client.add_cog(Calculator(client))
