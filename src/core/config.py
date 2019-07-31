# Builtins
import optparse
import logging

module_logger = logging.getLogger('koneko.Settings')


class Settings:
    __slots__ = 'dry_run', 'toggle_extensions', 'core_extensions'

    def __init__(self):
        parser = optparse.OptionParser()

        parser.add_option("-d", "--dry-run", dest="boot_only", default=0)

        (options, _) = parser.parse_args()

        self.dry_run = bool(int(options.boot_only))
        self.toggle_extensions = [
            "admin",
            # "adminstration",
            # "alert",
            "currency",
            "dnd",
            "gambling",
            "games",
            "general",
            # "goodbye",
            "help",
            "level",
            # "stats",
            "utility",
            # "welcome",
        ]
        self.core_extensions = [
            "DBL",
            "ErrorHandler",
            "EventListener"
        ]
