from collections import namedtuple

Levels = namedtuple("Levels", ["info", "debug", "warning", "error"])
LEVELS = Levels(info="INFO", debug="DEBUG", warning="WARNING", error="ERROR")
