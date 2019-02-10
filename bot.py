import discord
import asyncio
import youtube_dl
import re

from discord.ext import commands
from itertools import cycle

TOKEN = 'NTEwNjQyMDQ3NTQ4NjUzNTY4.Dzda2g.lmto6SX9hskBSimX4jfR8-Ya7tE'

#command prefix
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

players = {}
queues = {}
weebsongs = [
'https://www.youtube.com/watch?v=-Q--ZqWOZrw',
'https://www.youtube.com/watch?v=0YF8vecQWYs',
'https://www.youtube.com/watch?v=3dLqUADUNZ0',
'https://www.youtube.com/watch?v=CaksNlNniis',
'https://www.youtube.com/watch?v=5_iuNaULT5k',
'https://www.youtube.com/watch?v=R7uF09yI4YA',
'https://www.youtube.com/watch?v=-hA4na_3jT0',
]

gamestatus = ['with Myself', 'with Your Heart', 'You Like a Fiddle', 'HuniePop', 'OSU!', 'the Game of Life', 'My Cat']
extensions = ['Music', 'Calculator', 'Fun', 'TTT','Help']


#this just changes the little 'playing with' thing underneath the bot name every 50 seconds
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(gamestatus)

    while not client.is_closed:
        current_gamestatus = next(msgs)
        await client.change_presence(game=discord.Game(name=current_gamestatus))
        #asyncio just pauses this function while allowing all other code to run, time.sleep pauses entire bot
        await asyncio.sleep(3600)

@client.event
async def on_ready():
    print('Slithering on')


#logs person's id and message
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    await client.process_commands(message)
#ping pong
@client.command()
async def ping():
    #client.say can only be used in a command, while client.send_message can be used in commands and events
    #not passed in a channel, sends message to channel that it was called in
    await client.say('Pong!')

@client.command()
# *args lets you pass in an infinite amount of arguments into the command, returns tuple of all arguments passed into command
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

#clears text with amount specified
@client.command(pass_context=True)
async def clear(ctx, amount=5):
    channel = ctx.message.channel
    await client.purge_from(channel, limit=int(amount) + 1)
    await client.say('{} messages deleted'.format(amount))

#turns bot off
@client.command()
async def logout():
    await client.say('Slithering away!')
    await client.logout()

#loads cogs
@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

#unloads cogs
@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    client.loop.create_task(change_status())
    client.run(TOKEN)

#these are embed stuffs, not sure what to use it for so its here but not active
#@client.command()
#async def displayEmbed():
#    embed = discord.Embed(
#        title = 'Title',
#        description = 'This is a description',
#        color = discord.Color.blue()
#    )
#    embed.set_footer(text='This is a footer.')
#    embed.set_image(url='https://i.redd.it/nr5g2zug5pgy.png')
#    embed.set_thumbnail(url='https://i.redd.it/nr5g2zug5pgy.png')
#    embed.set_author(name='Author Name', icon_url='https://i.redd.it/nr5g2zug5pgy.png')
#    embed.add_field(name = 'Field Name', value='Field Value', inline=False)
#    embed.add_field(name = 'Field Name', value='Field Value', inline=True)
#    embed.add_field(name = 'Field Name', value='Field Value', inline=True)
#    await client.say(embed=embed)
