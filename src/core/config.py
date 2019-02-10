import optparse


class Settings:
    __slots__ = (
        'token', 'pm_help', 'prefix', 'dry_run', 'owner_id', 'dev_ids', 'toggle_extensions', 'core_extensions'
    )

    def __init__(self):
        parser = optparse.OptionParser()

        parser.add_option("-t", "--token", dest="token", default="TOKEN")
        parser.add_option("-p", "--pm-help", dest="pm_help", default=0)
        parser.add_option("-c", "--command-prefix", dest="command_prefix", default="$")
        parser.add_option("-d", "--dry-run", dest="boot_only", default=0)

        (options, args) = parser.parse_args()

        self.token = options.token
        self.pm_help = bool(int(options.pm_help))
        self.prefix = options.command_prefix
        self.dry_run = bool(int(options.boot_only))
        self.owner_id = 180640710217826304
        self.dev_ids = [self.owner_id, ]
        self.toggle_extensions = [
            "economy.currency",
            "gambling.gambling",
            # "games.pokemon",
            "games.dnd",
            "games.rps",
            "general.general",
            # "general.goodbye",
            # "general.welcome",
            "leveling.level",
            # "moderation.moderation",
            "music.music",
            # "nsfw.nsfw",
            "utility.utility",
            # "utility.stats",
        ]
        self.core_extensions = [
            "src.core.ErrorHandler",
        ]
