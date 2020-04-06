# Builtins
import logging
import random

# Pip
import discord
from discord.ext import commands

module_logger = logging.getLogger('koneko.Games')


class Games(commands.Cog):
    """Some fun games."""

    __slots__ = 'bot'

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, choice: str = ""):
        """Play a game of rock paper scissors."""
        player = choice.lower()
        options = {
            "r": "rock",
            "p": "paper",
            "s": "scissors"
        }

        if player in options:
            module_logger.info("p in o")
            player = options.get(player)
        elif player not in options.values():
            embed = discord.Embed(title='Please choose from: rock, paper, scissors',
                                  color=discord.Color.red())
            await ctx.channel.send(embed=embed)
            return

        bot = random.choice(list(options.values()))

        if player == bot:
            color = discord.Color.dark_grey()
            message = "Tie!"
        elif player == "rock":
            if bot == "paper":
                color = discord.Color.red()
                message = f"You lose! {bot} covers {player}"
            else:
                color = discord.Color.green()
                message = f"You win! {player} smashes {bot}"
        elif player == "paper":
            if bot == "Scissors":
                color = discord.Color.red()
                message = f"You lose! {bot} cut {player}"
            else:
                color = discord.Color.green()
                message = f"You win! {player} covers {bot}"
        elif player == "scissors":
            if bot == "rock":
                color = discord.Color.red()
                message = f"You lose! {bot} smashes {player}"
            else:
                color = discord.Color.green()
                message = f"You win! {player} cut {bot}"
        else:
            color = discord.Color.red()
            message = "Oops something went wrong"

        embed = discord.Embed(title=message,
                              color=color)
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Games(bot))
