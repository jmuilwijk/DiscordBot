from discord.ext import commands

import config

prefix = "!"
startup_extensions = [
    "modules.general",
    "modules.response.response"
]

bot = commands.Bot(command_prefix=prefix)
bot.pm_help = False


# Function called when the bot is ready.
@bot.event
async def on_ready():
    # Bot logged in.
    print('Logged in as {0.user}'.format(bot))

if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)
    bot.run(config.token)
