import discord
from discord.ext import commands

class commandlist:
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
        color = discord.Color.orange()
        )
        embed.set_author(name='Help')
        embed.add_field(name='.ping', value = 'Pong!', inline=False)
        embed.add_field(name='.echo [words]', value = 'Echoes the words that you input', inline=False)
        embed.add_field(name='.clear [amount]', value = 'Clears the specified amount of messages', inline=False)
        embed.add_field(name='.timer [seconds]', value = 'Gives a message once [seconds] have passed', inline=False)

        embed.add_field(name='.multiply[num] [num] [num] etc..', value = 'Multiplies multiple numbers', inline=False)
        embed.add_field(name='.add [num] [num] [num] etc..', value = 'Adds multiple numbers', inline=False)
        embed.add_field(name='.subtract [num] [num] [num] etc..', value = '(Only works with 2 numbers right now)Subtracts numbers', inline=False)

        embed.add_field(name='.ttt', value = 'TicTacToe!', inline=False)

        embed.add_field(name='.load [extension]', value = 'Loads extension', inline=False)
        embed.add_field(name='.unload [extension]', value = 'Unloads extension', inline=False)

        embed.add_field(name='.play [URL]', value = 'Plays song at URL', inline=False)
        embed.add_field(name='.queue [URL]', value = 'Adds song at URL to queue', inline=False)
        embed.add_field(name='.pause', value = 'Pauses current song playing', inline=False)
        embed.add_field(name='.stop', value = 'Stops current song playing', inline=False)
        embed.add_field(name='.resume', value = 'Resumes playing paused song', inline=False)

        await self.client.send_message(author, embed=embed)

def setup(self.client):
    self.client.add_cog(commandsList(self.client))
