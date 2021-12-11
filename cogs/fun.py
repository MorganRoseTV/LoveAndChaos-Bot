import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @bot.command(aliases=['8ball'])
        async def _8ball(ctx, *, question='5'):
            responses = [ # The list of possible responses
              'It is certain.',
              'It is decidedly so.',
              'Without a doubt.',
              'Yes - definitely.',
              'You may rely on it.',
              'As I see it, yes.',
              'Most likely.',
              'Outlook good.',
              'Yes.',
              'Signs point to yes.',
              'Reply hazy, try again.',
              'Ask again later.',
              'Better not tell you now.',
              'Cannot predict now.',
              'Concentrate and ask again',
              'Don\'t count on it',
              'My reply is no.',
              'Outlook not so good.',
              'Very doubtful.'
              ]
            if question == '5':
              await ctx.send('Please input a question.') # Catches empty messages and requests additional args
            else:
              await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}') # Sends a randomized response to a question

def setup(bot):
    bot.add_cog(Fun(bot))