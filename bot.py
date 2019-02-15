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
'https://www.youtube.com/watch?v=-Q--ZqWOZrw: Blend S OP',
'https://www.youtube.com/watch?v=0YF8vecQWYs: Domestic na Kanojo OP',
'https://www.youtube.com/watch?v=3dLqUADUNZ0: Attack on Titan OP',
'https://www.youtube.com/watch?v=CaksNlNniis: No Game No Life OP',
'https://www.youtube.com/watch?v=5_iuNaULT5k: Hikaru Nara',
'https://www.youtube.com/watch?v=-hA4na_3jT0: Angel Beats OP',
'https://www.youtube.com/watch?v=PkVx2XYalzQ: Kekkai Sensen ED',
'https://www.youtube.com/watch?v=armte0mUnDw: BunnyGirl OP',
'https://www.youtube.com/watch?v=_GB7rZfjrxw: Peace Sign',
'https://www.youtube.com/watch?v=F5OJPUXJvHk: 99',
'https://www.youtube.com/watch?v=DjS58kpTcuw: Hitorigoto',
'https://www.youtube.com/watch?v=ObQd7Co7Q_I: Fiction',
'https://www.youtube.com/watch?v=DpCfhRVqJWU: 99.9',
'https://www.youtube.com/watch?v=OsLY7DXWsF4: Crossing Field'
]
gamestatus = ['with Myself', 'with Your Heart', 'You Like a Fiddle', 'HuniePop', 'OSU!', 'the Game of Life', 'My Cat', 'all by Myself','Tota - Africa, for hours on end',
'Overwatch', 'CS:GO', 'Team Fortress 2']

extensions = ['Music', 'Calculator', 'Fun', 'TTT']
#this just changes the little 'playing with' thing underneath the bot name every 50 seconds
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(gamestatus)

    while not client.is_closed:
        current_gamestatus = next(msgs)
        await client.change_presence(game=discord.Game(name=current_gamestatus))
        #asyncio just pauses this function while allowing all other code to run, time.sleep pauses entire bot
        await asyncio.sleep(600)
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
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
    color = discord.Color.green()
    )
    embed.set_footer(text='Help')
    embed.add_field(name='.ping', value = 'Pong!', inline=False)
    embed.add_field(name='.echo [words]', value = 'Echoes the words that you input', inline=False)
    embed.add_field(name='.clear [amount]', value = 'Clears the specified amount of messages', inline=False)
    embed.add_field(name='.timer [seconds]', value = 'Gives a message once [seconds] have passed', inline=False)

    embed.add_field(name='.mult[num] [num] [num] etc..', value = 'Multiplies multiple numbers', inline=False)
    embed.add_field(name='.add [num] [num] [num] etc..', value = 'Adds multiple numbers', inline=False)
    embed.add_field(name='.subt [num] [num] [num] etc..', value = 'Subtracts numbers', inline=False)
    embed.add_field(name='.modo [num] [num] [num] etc..', value = 'Take the modulo of numbers', inline=False)
    embed.add_field(name='.divi [num] [num] [num] etc..', value = 'Divide multiple numbers', inline=False)
    embed.add_field(name='.ln [num]', value = 'Take the natural log of a number', inline=False)

    embed.add_field(name='.ttt', value = 'TicTacToe!', inline=False)
    embed.add_field(name='.annoy[user]', value = "You're an ass if you use this but I made it so idk", inline=False)
    embed.add_field(name='.ccipher[# to shift][message to shift]', value = 'Caeser cipher', inline=False)

    embed.add_field(name='.play [URL]', value = 'Plays song at URL', inline=False)
    embed.add_field(name='.pause', value = 'Pauses current song playing', inline=False)
    embed.add_field(name='.stop', value = 'Stops current song playing', inline=False)
    embed.add_field(name='.resume', value = 'Resumes playing paused song', inline=False)

    embed.add_field(name='.weeb', value = 'Gives a random anime song from a list.', inline=False)

    await client.send_message(author, embed=embed)

@client.command()
async def abort():
    await client.logout()

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
