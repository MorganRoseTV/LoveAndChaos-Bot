import os
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        async def ping(ctx):
            await ctx.send(f'Pong! {round(bot.latency*1000)}ms') # Returns the bot's latency in ms
        
        @bot.command()
        async def makelist(ctx):
            str = ctx.message.content
            str = str.strip().replace(' ', '", "') 
            await ctx.send(f'[\"{str}\" ]') # Parses a message and makes it into a list
        
        @makelist.error
        async def makelist_error(ctx, error):
            await ctx.send(error)
            print(error) # Returns an error when the makelist command fails, both to the chat and the console

def setup(bot):
    bot.add_cog(Utilities(bot))