import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command('bonk') 
        async def bonk(ctx, member: discord.Member): #sets the command name as well as the member variable
            rolename= 'In Horny Jail uwu' # The name of the role the bot works with.
            role = discord.utils.get(member.guild.roles, name=rolename) # Sets the role, labeled in line 20. This took me 4 hours to get right :)
            await member.add_roles(role) # Gives the mentioned user the role set in line 20
            await ctx.send(f'{ctx.author.mention} sends {member.mention} to <#919306127903170650>. Naughty kitty!') #Notifies the chat that the user has been put in timeout
            await asyncio.sleep(300) # Waits 5 minutes before running the rest of the code
            await member.remove_roles(role) # Removes the role set in line 20 from the mentioned user
            await ctx.send(f'Welcome back, {member.mention}! Hope you\'ve learned your lesson!') #Notifies the user that their timeout has been lifted
        @bonk.error
        async def bonk_error(ctx, error):
            await ctx.send(error) #prints any errors in chat, may add user friendly error messages in the future.

def setup(bot):
    bot.add_cog(Moderation(bot))
