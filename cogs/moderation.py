import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command('bonk') 
        async def bonk(ctx, member: discord.Member): #sets the command name as well as the member variable
            # rolename = 'In Horny Jail uwu' # The name of the role the bot works with.
            role = discord.utils.get(member.guild.roles, id=919305834192859156) # Sets the role, labeled in line 11. This took me 4 hours to get right :)
            role18 = discord.utils.get(member.guild.roles, id=917626017969999903)
            if role18 in member.roles:
                await member.remove_roles(role18),
                member18 = 18
            else:
                member18 = 0
            await member.add_roles(role) # Gives the mentioned user the role set in line 11
            await ctx.send(f'{ctx.author.mention} sends {member.mention} to <#919306127903170650>. Naughty kitty!') #Notifies the chat that the user has been put in timeout
            await asyncio.sleep(300) # Waits 5 minutes before running the rest of the code
            await member.remove_roles(role) # Removes the role set in line 11 from the mentioned user
            if member18 == 18:
                await member.add_roles(role18)
            else:
                return
            await ctx.send(f'Welcome back, {member.mention}! Hope you\'ve learned your lesson!') #Notifies the user that their timeout has been lifted
        @bonk.error
        async def bonk_error(ctx, error):
            await ctx.send(error) #prints any errors in chat, may add user friendly error messages in the future.

        @bot.command(name='createrole',aliases=['newrole','add_role','create_role','new_role']) #Allows moderators to use aliases to run the command
        @commands.has_permissions(manage_roles=True) #Ensures only moderators can run the command 
        async def createrole(ctx, *, name):
            guild = ctx.guild #sets the guild
            await guild.create_role(name=name) #Creates the role with the designated name set in the command
            await ctx.send(f'Role `{name}` has been created.') #Lets the user know that the role was created.
        @createrole.error
        async def createrole_error(ctx, error):
            await ctx.send(error)

        @bot.command(name='free',aliases=['unbonk'])
        @commands.has_permissions(manage_roles=True)
        async def free(ctx,member: discord.Member, args1): # /////////////////////////////
            role = discord.utils.get(member.guild.roles, name=919305834192859156)
            role18 = discord.utils.get(member.guild.roles, id=917626017969999903)
            await member.remove_roles(role)
            if args1 == 18: #//////////////////////////////
                await member.add_roles(role18)
            else:
                return
            await ctx.send(f'Welcome back, {member.mention}! Hope you\'ve learned your lesson!')
        @free.error
        async def free_error(ctx,error):
            await ctx.send(error)

        @bot.command(name='deleterole',aliases=['delete_role']) 
        @commands.has_permissions(manage_roles=True) 
        async def deleterole(ctx, *, rolename): 
            role_object= discord.utils.get(ctx.message.guild.roles, name=rolename) 
            await role_object.delete() 
            await ctx.send(f'Role `{rolename}` has been deleted.') 
        @deleterole.error 
        async def deleterole_error(ctx, error): 
            await ctx.send(error) 
def setup(bot): 
    bot.add_cog(Moderation(bot))
