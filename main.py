import os
import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

client = discord.Client
bot = commands.Bot(command_prefix='>')
status = cycle(['>help', 'Mess around and find out.'])

@bot.event
async def on_ready():
    channel = bot.get_channel(917635324983783435)
    await channel.send(f'{bot.user.mention} is now online.')
    status_update.start()
    print('{0.user} is now logged in.'.format(client))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is not recognized. Please check your command and try ag ain.')

@bot.command(aliases=['l'])
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension loaded!')
@load.error
async def load_error(ctx, error):
    await ctx.send('Please specify an extension to load!')

@bot.command(aliases=['ul'])
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded!')
@unload.error
async def unload_error(ctx, error):
    await ctx.send('Please specify an extension to unload!')

@bot.command(aliases=['rl'])
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded!')
@reload.error
async def reload_error(ctx, error):
    await ctx.send('Please specify an extension to reload!')

@tasks.loop(seconds=30)
async def status_update():
    await bot.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def stop(ctx):
    await ctx.send('Stopping bot.')
    print('Stopping bot.')
    await bot.close()

load_dotenv(override=True)
token = os.getenv('token')
bot.run(os.getenv('token'))