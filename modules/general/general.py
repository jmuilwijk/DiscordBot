from discord.ext import commands


class General:
    def __init__(self, bot):
        self.bot = bot

    # Command hello, listen to !hello
    @commands.command()
    async def hello(self, message):
        # TODO: add command description.
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    # Command ping, listen to !ping
    @commands.command(pass_context=True, description='Get the latency of the bot.')
    async def ping(self, ctx):
        """Get the latency of the bot."""
        # Get the latency of the bot
        latency = str(round(self.bot.latency * 1000)) + " ms"  # Included in the Discord.py library
        # Send it to the user
        await ctx.send(latency)


def setup(bot):
    bot.add_cog(General(bot))