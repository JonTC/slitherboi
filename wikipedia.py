import discord
import asyncio
from discord.ext import commands

class wikipedia:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wikiSearch(self):
