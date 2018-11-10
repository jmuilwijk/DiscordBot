import discord
from discord.ext import commands
from sys import argv

prefix = "/"
startup_extensions = [
    # "games.pokemon",
    # "games.rps",
    "general.general",
    # "general.goodbye",
    # "general.response",
    # "general.welcome",
    # "help.commands",
    # "help.help",
    "music.music",
    # "nsfw.nsfw",
    # "utility.stats",
]

KonekoBot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
KonekoBot.pm_help = False


# Function called when the bot is ready.
@KonekoBot.event
async def on_ready():
    game = prefix + "help for help"
    activity = discord.Game(name=game)
    await KonekoBot.change_presence(status=discord.Status.online, activity=activity)
    # Bot logged in.
    print('Logged in as {0.user}'.format(KonekoBot))

if __name__ == '__main__':
    for extension in startup_extensions:
        KonekoBot.load_extension("src.modules." + extension)
    KonekoBot.run(argv[1])