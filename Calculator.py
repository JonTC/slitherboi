import discord
import asyncio
import math


from math import exp, expm1
from math import e
from discord.ext import commands

class Calculator:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, *args):
        sum = 0.0
        for x in args:
            sum = sum + float(x)
        await self.client.say('The sum is: {}'.format(sum))

    #only works with 2 numbers rn
    @commands.command()
    async def subt(self,*args):
        total = 0.0
        for i in range(len(args)):
            if(i == 0):
                total = float(args[i])
            else:
                total -= float(args[i])
        await self.client.say('The difference is: ' + str(total))

    @commands.command()
    async def mult(self, *args):
        product = 1.0
        for x in args:
            product = product * float(x)
        await self.client.say('The product is: {}'.format(product))
    @commands.command()
    async def divi(self, *args):
        for i in range(len(args)):
            if(i == 0):
                quotient = float(args[i])
            else:
                quotient /= float(args[i])
        await self.client.say('The quotient is: {}'.format(quotient))

    @commands.command()
    async def modo(self, *args):
        total = 0.0
        for i in range(len(args)):
            if(i == 0):
                total = float(args[i])
            else:
                total %= float(args[i])
        await self.client.say('The total is: ' + str(total))
    """
    @commands.command()
    await def exp(self, base, exp, *therest):
        product = float(base)**float(self)
        await self.client.say('{} raised to the power of {} is: {}'.format(base, exp, product))
        if(therest):
            await self.client.say('{} is not valid'.format(therest))
    """
    @commands.command()
    async def ln(self, arg):
        total = 0.0
        if(str(arg) == 'e'):
            total = math.log1p(e - 1)
            await self.client.say('The natural log of {} is: {}'.format(arg, total))
        elif(int(arg) == 0):
            await self.client.say('Undefined')
        elif(int(arg) < 0):
            await self.client.say('Non-real number')
        else:
            total = math.log1p(float(arg) -1)
            await self.client.say('The natural log of {} is: {}'.format(arg, total))

    #@commands.command()
    #async def deriv(self, arg):

    @commands.command()
    async def timer(self, seconds):
        await asyncio.sleep(int(seconds));
        await self.client.say("Time's up")

def setup(client):
    client.add_cog(Calculator(client))
