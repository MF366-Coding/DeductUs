# constants

from colorama import Fore

# [*] Difficulty Constants
BEGINNER_DIFF = 1 # [i] Killer Recruit
SABOTEUR_DIFF = 2 # [i] Sneaky Saboteur
PRO_HITMAN_DIFF = 3 # [i] Professional Hitman
LEGEND_DIFF = 4 # [i] Legend of the Lies
RANDOM_DIFF = 5 # [i] Thrilling Surprise

# [*] Values per Difficulty
RECRUIT_VALUES: dict[str, tuple[int, int]] = {
    "NAME": "Begginer of the Killing",
    "IMPOSTOR_FIGHT_BACK": (99, 100),
    "CREW_FIGHT_BACK": (70, 75),
    "IMPOSTOR_GIVE_UP": (1, 5),
    "CREW_JESTER": (0, 0),
    "IMPOSTOR_ACCUSE_SUS": (20, 40),
    "IMPOSTOR_ACCUSE_CLEAR": (65, 85),
    "IMPOSTOR_ACCUSE_NEUTRAL": (10, 30),
    "SUS_ACCUSE_SUS": (10, 30),
    "SUS_ACCUSE_CLEAR": (40, 60),
    "SUS_ACCUSE_NEUTRAL": (5, 20),
    "CLEAR_ACCUSE_SUS": (10, 30),
    "CLEAR_ACCUSE_CLEAR": (50, 70),
    "CLEAR_ACCUSE_NEUTRAL": (5, 20),
    "NEUTRAL_ACCUSE_SUS": (5, 20),
    "NEUTRAL_ACCUSE_CLEAR": (65, 80),
    "NEUTRAL_ACCUSE_NEUTRAL": (10, 30),
    "IMPOSTOR_TALKS": (0, 30),
    "NUMBER_OF_TOOLS_1_IMPOSTOR": (0, 0),
    "NUMBER_OF_TOOLS_2+_IMPOSTORS": (1, 1),
    "FALSE_SCAN_CHANCE": (0, 10),
    "TRACK_CHANCE": (0, 0),
    "ARTIST_CHANCE": (0, 0),
    "PSYCHIC_CHANCE": (0, 0),
    "SCAN_CHANCE": (0, 0),
    "TEAM_CHANCE": (0, 0),
    "LOBBY_SIZE_1_IMPOSTOR": (6, 6),
    "LOBBY_SIZE_2+_IMPOSTORS": (7, 8)
}

SABOTEUR_VALUES: dict[str, tuple[int, int]] = {
    "NAME": "Sneaky Saboteur",
    "IMPOSTOR_FIGHT_BACK": (60, 80),
    "CREW_FIGHT_BACK": (80, 95),
    "IMPOSTOR_GIVE_UP": (0, 3),
    "CREW_JESTER": (0, 0),
    "IMPOSTOR_ACCUSE_SUS": (40, 60),
    "IMPOSTOR_ACCUSE_CLEAR": (25, 45),
    "IMPOSTOR_ACCUSE_NEUTRAL": (30, 50),
    "SUS_ACCUSE_SUS": (30, 50),
    "SUS_ACCUSE_CLEAR": (20, 40),
    "SUS_ACCUSE_NEUTRAL": (35, 55),
    "CLEAR_ACCUSE_SUS": (40, 60),
    "CLEAR_ACCUSE_CLEAR": (20, 30),
    "CLEAR_ACCUSE_NEUTRAL": (30, 50),
    "NEUTRAL_ACCUSE_SUS": (45, 65),
    "NEUTRAL_ACCUSE_CLEAR": (30, 40),
    "NEUTRAL_ACCUSE_NEUTRAL": (20, 40),
    "IMPOSTOR_TALKS": (40, 70),
    "NUMBER_OF_TOOLS_1_IMPOSTOR": (1, 1),
    "NUMBER_OF_TOOLS_2+_IMPOSTORS": (2, 2),
    "FALSE_SCAN_CHANCE": (0, 20),
    "LOBBY_SIZE_1_IMPOSTOR": (8, 8),
    "LOBBY_SIZE_2+_IMPOSTORS": (9, 10)
}

PRO_HITMAN_VALUES: dict[str, tuple[int, int]] = {
    "NAME": "Professional Hitman",
    "IMPOSTOR_FIGHT_BACK": (40, 60),
    "CREW_FIGHT_BACK": (50, 60),
    "IMPOSTOR_GIVE_UP": (0, 1),
    "CREW_JESTER": (0, 0),
    "IMPOSTOR_ACCUSE_SUS": (50, 60),
    "IMPOSTOR_ACCUSE_CLEAR": (35, 55),
    "IMPOSTOR_ACCUSE_NEUTRAL": (40, 60),
    "SUS_ACCUSE_SUS": (40, 50),
    "SUS_ACCUSE_CLEAR": (10, 30),
    "SUS_ACCUSE_NEUTRAL": (20, 40),
    "CLEAR_ACCUSE_SUS": (40, 60),
    "CLEAR_ACCUSE_CLEAR": (15, 25),
    "CLEAR_ACCUSE_NEUTRAL": (40, 70),
    "NEUTRAL_ACCUSE_SUS": (55, 75),
    "NEUTRAL_ACCUSE_CLEAR": (25, 35),
    "NEUTRAL_ACCUSE_NEUTRAL": (25, 40),
    "IMPOSTOR_TALKS": (80, 100),
    "NUMBER_OF_TOOLS_1_IMPOSTOR": (2, 2),
    "NUMBER_OF_TOOLS_2+_IMPOSTORS": (3, 3),
    "FALSE_SCAN_CHANCE": (0, 30),
    "LOBBY_SIZE_1_IMPOSTOR": (10, 10),
    "LOBBY_SIZE_2+_IMPOSTORS": (11, 13)
}

LEGEND_VALUES: dict[str, tuple[int, int]] = {
    "NAME": "Legend of the Lies",
    "IMPOSTOR_FIGHT_BACK": (50, 60),
    "CREW_FIGHT_BACK": (45, 60),
    "IMPOSTOR_GIVE_UP": (0, 1),
    "CREW_JESTER": (0, 3),
    "IMPOSTOR_ACCUSE_SUS": (50, 60),
    "IMPOSTOR_ACCUSE_CLEAR": (10, 20),
    "IMPOSTOR_ACCUSE_NEUTRAL": (45, 55),
    "SUS_ACCUSE_SUS": (55, 65),
    "SUS_ACCUSE_CLEAR": (10, 20),
    "SUS_ACCUSE_NEUTRAL": (45, 60),
    "CLEAR_ACCUSE_SUS": (50, 65),
    "CLEAR_ACCUSE_CLEAR": (0, 10),
    "CLEAR_ACCUSE_NEUTRAL": (35, 55),
    "NEUTRAL_ACCUSE_SUS": (45, 55),
    "NEUTRAL_ACCUSE_CLEAR": (10, 25),
    "NEUTRAL_ACCUSE_NEUTRAL": (40, 50),
    "IMPOSTOR_TALKS": (70, 90),
    "NUMBER_OF_TOOLS_1_IMPOSTOR": (3, 3),
    "NUMBER_OF_TOOLS_2+_IMPOSTORS": (3, 3),
    "FALSE_SCAN_CHANCE": (0, 40),
    "LOBBY_SIZE_1_IMPOSTOR": (11, 12),
    "LOBBY_SIZE_2+_IMPOSTORS": (13, 15)
}

RANDOM_VALUES: dict[str, tuple[int, int]] = {
    "NAME": "Thrilling Surprise",
    "IMPOSTOR_FIGHT_BACK": (0, 100),
    "CREW_FIGHT_BACK": (0, 100),
    "IMPOSTOR_GIVE_UP": (0, 6),
    "CREW_JESTER": (0, 6),
    "IMPOSTOR_ACCUSE_SUS": (0, 100),
    "IMPOSTOR_ACCUSE_CLEAR": (0, 100),
    "IMPOSTOR_ACCUSE_NEUTRAL": (0, 100),
    "SUS_ACCUSE_SUS": (0, 100),
    "SUS_ACCUSE_CLEAR": (0, 100),
    "SUS_ACCUSE_NEUTRAL": (0, 100),
    "CLEAR_ACCUSE_SUS": (0, 100),
    "CLEAR_ACCUSE_CLEAR": (0, 100),
    "CLEAR_ACCUSE_NEUTRAL": (0, 100),
    "NEUTRAL_ACCUSE_SUS": (0, 100),
    "NEUTRAL_ACCUSE_CLEAR": (0, 100),
    "NEUTRAL_ACCUSE_NEUTRAL": (0, 100),
    "IMPOSTOR_TALKS": (0, 100),
    "NUMBER_OF_TOOLS_1_IMPOSTOR": (1, 3),
    "NUMBER_OF_TOOLS_2+_IMPOSTORS": (2, 4),
    "FALSE_SCAN_CHANCE": (0, 100),
    "LOBBY_SIZE_1_IMPOSTOR": (8, 12),
    "LOBBY_SIZE_2+_IMPOSTORS": (10, 15)
}

# [*] Colors
LIGHT_COLOR = 0
DARK_COLOR = 1
# --
WHITE_REAL = Fore.WHITE
YELLOW_REAL = Fore.YELLOW
ORANGE_REAL = Fore.LIGHTRED_EX
RED_REAL = Fore.RED
PINK_REAL = Fore.LIGHTMAGENTA_EX
PURPLE_REAL = Fore.MAGENTA
BLUE_REAL = Fore.BLUE
CYAN_REAL = Fore.CYAN
LIME_REAL = Fore.LIGHTGREEN_EX
GREEN_REAL = Fore.GREEN
# --
BANANA_REAL = Fore.LIGHTYELLOW_EX
LIGHT_BLUE_REAL = Fore.LIGHTBLUE_EX
BLACK_REAL = Fore.WHITE # [i] most terminals are black sooo
GREY_REAL = Fore.LIGHTBLACK_EX
LIGHT_CYAN_REAL = Fore.LIGHTCYAN_EX
# --
WHITE = 0 # [i] The detective will always have color set to White. I might make it customizable
YELLOW = 1
ORANGE = 2
RED = 3
PINK = 4
PURPLE = 5
BLUE = 6
CYAN = 7
LIME = 8
GREEN = 9
BANANA = 10
LIGHT_BLUE = 11
BLACK = 12
GREY = 13
LIGHT_CYAN = 14
# --
COLOR_TRANSLATION_DATABASE = [
    "White (You)",
    "Yellow",
    "Orange",
    "Red",
    "Pink",
    "Purple",
    "Blue",
    "Cyan",
    "Lime",
    "Green",
    "Banana",
    "Light Blue",
    "Black",
    "Grey",
    "Light Cyan"
]

# [*] Status Values
NO_SCAN = 0
BAD_SCAN = 1
GOOD_SCAN = 2
# --

