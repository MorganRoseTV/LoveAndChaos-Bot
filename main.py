import os
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

client = discord.Client()
bot = commands.Bot(command_prefix='!') # Sets the prefix
status = cycle(['>help', 'Mess around and find out.']) # List of presence indicators

@bot.event
async def on_ready():
    channel = bot.get_channel(917635324983783435) # Sets the channel to send bot updates
    await channel.send(f'{bot.user.mention} is now online.') # Sends update, notifying that the bot is online
    status_update.start()
    print('{0.user} is now logged in.'.format(bot)) # Sends a message to the console, confirming a successful bootup

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is not recognized. Please check your command and try again.') # Catches errors and returns a response, informing the user that their command did not work

@bot.command(aliases=['l'])
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension loaded!') # Loads unloaded extensions
@load.error
async def load_error(ctx, error):
    await ctx.send('Please specify an extension to load!') # Catches errors and returns a response, informing the user that their command did not work

@bot.command(aliases=['ul'])
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded!') # Unloads loaded extensions
@unload.error
async def unload_error(ctx, error):
    await ctx.send('Please specify an extension to unload!') # Catches errors and returns a response, informing the user that their command did not work

@bot.command(aliases=['rl'])
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded!') # Unloads then re-loads extensions, this is particularly useful after making an update to one of them
@reload.error
async def reload_error(ctx, error):
    await ctx.send('Please specify an extension to reload!') # Catches errors and returns a response, informing the user that their command did not work

@tasks.loop(seconds=30)
async def status_update():
    await bot.change_presence(activity=discord.Game(next(status))) # Sets the bot's status, cycling it through the list every 30 seconds

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') # Makes it so that users do not have to add .py to the extension name in their message to make the command work

@bot.command()
async def stop(ctx):
    await ctx.send('Stopping bot.') # Shuts the bot down
    print('Stopping bot.')
    await bot.close()

load_dotenv(override=True)
bot.run(os.getenv('token')) # Allows the bot to log in as its user counterpart on Discord. 'token' is taken from a hidden file named .env