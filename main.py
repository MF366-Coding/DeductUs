from colorama import Fore
import random
from icecream import ic
import sys
from os import system
import time

platform = sys.platform
force_sim_debug = False


# [!!] Things to uncomment on release and commit
# ic.disable()
# force_sim_debug = False


ic.configureOutput("debug statement | ")

def clear():
    if platform == "win32":
        system("cls")
    else:
        system("clear")

clear()
print(f"{Fore.YELLOW}[!] This is a BETA release.\nThanks to the people testing it!\n{Fore.RED}Deduct{Fore.CYAN}Us{Fore.RESET}\nBy MF366\n--\n\n")

crew = {
    1: False, # white
    2: False, # yellow
    3: False, # orange
    4: False, # red
    5: False, # pink
    6: False, # purple
    7: False, # blue
    8: False, # cyan
    9: False # lime
}

killer = []

x = random.randint(1, 9)

crew[x] = True
killer.append(x)

ic(crew)

print(f"{Fore.CYAN}Your role is... {Fore.YELLOW}Detective{Fore.CYAN} (Crewmate){Fore.RED}\nThere is 1 impostor among us.\n\n{Fore.RESET}")

dead = random.randint(1, 9)

while dead in killer:
    dead = random.randint(1, 9)

deaths = [dead]

reporter = random.randint(1, 9)

while reporter in deaths:
    reporter = random.randint(1, 9)

if ic.enabled and force_sim_debug:
    ic(dead)
    ic(crew)
    ic(deaths)
    ic(killer)
    ic(dead in killer)
    ic(reporter in deaths)
    ic(dead in deaths)

    if ic.enabled:
        with open("debug_file.txt", "a", encoding="utf-8") as _f:
            _f.write('\n\n\n--\n')
            # [!?] Not needed anymore
            # _f.write(f"dead: {str(dead)}\ncrew: {str(crew)}\ndeaths: {str(deaths)}\nkiller: {str(killer)}")
            _f.write(f"\n{dead in killer}\n{reporter in deaths}\n{dead in deaths}")

    raise SystemExit

print(f"{Fore.RED}DEAD BODY REPORTED!{Fore.RESET}\n{Fore.LIGHTRED_EX}Dead body: Player {dead}\n{Fore.MAGENTA}Player who reported: Player {reporter}\n\n{Fore.RESET}")

ic(dead)
ic(crew[dead])
ic(reporter)
ic(crew)

def who_is_it(indexer: int = 0) -> int:
    """
    who_is_it returns the ID of the Impostor

    Args:
        indexer (int, optional): what index to verify on the killer list. Defaults to 0 (first one).

    Returns:
        int: the ID of the indexed Impostor
    """
    
    return killer[indexer]

def make_better_crew() -> list:
    _bc = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None
    }

    for _id in range(10):
        if _id == 0 or _id == 10:
            pass

        elif crew[_id] == "dead":
            _bc[_id] = "Dead"

        else:
            _bc[_id] = "Alive"

    return _bc

better_crew = make_better_crew()


print(f"""{Fore.BLUE}Player List:
{Fore.YELLOW}0 - You!
{Fore.CYAN}1 - {better_crew[1]}
2 - {better_crew[2]}
3 - {better_crew[3]}
4 - {better_crew[4]}
5 - {better_crew[5]}
6 - {better_crew[6]}
7 - {better_crew[7]}
8 - {better_crew[8]}
9 - {better_crew[9]}

{Fore.BLUE}You can scroll up at any time to see all the information!

{Fore.YELLOW}Since you're a detective, you'll now "detect" I guess...

{Fore.GREEN}1. Team Verification
{Fore.CYAN}Type the ID of two players (example: 5 and 6).
With this, you'll discover if the 2 players are or are not in the same team.
{Fore.RED}Remember: there is only 1 impostor!
DON'T INSERT BOTH PLAYER IDS AT THE SAME TIME PLEASE!
DON'T INSERT IDS OF DEAD PLAYERS!
IDS MUST BE GREATER THAN 0 AND LOWER THAN 10!
{Fore.YELLOW}
""")

full_lobby = [i for i in range(1, 10)]

pl_1 = int(input("First Player ID: "))
pl_2 = int(input("Second Player ID: "))

ic(crew)
ic(better_crew)

if pl_1 == pl_2:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

elif pl_1 not in full_lobby or pl_2 not in full_lobby:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

elif pl_1 in deaths or pl_2 in deaths:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

print("\n\n")

if crew[pl_1] == crew[pl_2]:
    print(f"{Fore.GREEN}The Players {pl_1} and {pl_2} are in the same team!")

elif crew[pl_1] != crew[pl_2]:
    print(f"{Fore.RED}The Players {pl_1} and {pl_2} are NOT in the same team!")

print(f"{Fore.RESET}\n\n")

print(f"""{Fore.GREEN}2. CrewScan
{Fore.CYAN}Type the ID of one player (example: 3).
You'll find out if they are crew or not. Easy, right?
Well, not really!
There's a 70% chance the machine will output a totally random result.
DON'T INSERT THE ID OF DEAD PLAYERS!
THE ID MUST BE GREATER THAN 0 AND LOWER THAN 10!
{Fore.YELLOW}
""")

pl_unloc = int(input("Player ID: "))

if pl_unloc not in full_lobby:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

elif pl_unloc in deaths:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

print('\n\n')

if random.randint(0, 10) >= 8:
    if crew in killer:
        print(f"{Fore.RED}Player {pl_unloc} is an Impostor!")

    else:
        print(f"{Fore.GREEN}Player {pl_unloc} is not an Impostor!")

else:
    if random.randint(0, 1) == 0:
        print(f"{Fore.GREEN}Player {pl_unloc} is not an Impostor!")
        
    else:
        print(f"{Fore.RED}Player {pl_unloc} is an Impostor!")

print(f"{Fore.RESET}\n\n")

print(f"""{Fore.GREEN}3. Psychic
Talk to the Psychic and he'll tell you all the suspicious he has.
{Fore.YELLOW}
""")

input('\nHit ENTER to talk to the Psychic... ')

def psychic(_indexer: int = 0) -> list:
    players_list = []

    players_list.append(killer[_indexer])

    m = random.randint(1, 9)
    
    while m in killer or m in deaths:
        m = random.randint(1, 9)
        
    n = random.randint(1, 9)
    
    while n in killer or n in deaths:
        n = random.randint(1, 9)

    players_list.append(m)
    players_list.append(n)

    random.shuffle(players_list)

    return players_list

x_players = psychic()

ic(type(x_players))
ic(x_players)

print(f"""{Fore.RED}Current suspicious players:
{Fore.CYAN}Player {str(x_players[0])}
Player {str(x_players[1])}
Player {str(x_players[2])}

{Fore.RED}The Psychic told you that one of this guys MUST be an Impostor!

{Fore.BLUE}Can you guess who it is?

{Fore.YELLOW}
""")

print(f"""\n\nTIME TO VOTE!
{Fore.CYAN}First you must exclude a player from this elimination!
It's simple: type the ID of a player you think is safe...
If you exclude the Impostor, it's over!
DON'T INSERT THE ID OF DEAD PLAYERS!
THE ID MUST BE GREATER THAN 0 AND LOWER THAN 10!
{Fore.YELLOW}
""")

safe_pl = int(input("Player ID: "))

if safe_pl not in full_lobby:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

elif safe_pl in deaths:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

print('\n\n')

print(f"{Fore.CYAN}Player {safe_pl}...")

if safe_pl in killer:
    time.sleep(1.7)
    print(f"{Fore.RED}...is the Impostor!")
    print(f"\n\n{Fore.RED}GAME OVER!\nPlayer {who_is_it()} was the Impostor!")
    sys.exit()
    
else:
    time.sleep(1.5)
    print(f"{Fore.GREEN}...is indeed not an Impostor!")

print(f"""\n\n{Fore.CYAN}Now, you must vote the Impostor out!
It's simple: type the ID of the player you think is the killer...
If you vote out a Crewmate, it's over!
DON'T INSERT THE ID OF DEAD PLAYERS!
THE ID MUST BE GREATER THAN 0 AND LOWER THAN 10!
{Fore.YELLOW}
""")

maybe_the_killer = int(input("Player ID: "))

if maybe_the_killer not in full_lobby:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

elif maybe_the_killer in deaths:
    print(Fore.RED)
    clear()
    raise ValueError("Excuse me, but are you dumb?")

print('\n\n')

print(f"{Fore.CYAN}Player {maybe_the_killer}...")

if maybe_the_killer in killer:
    time.sleep(2.0)
    print(f"{Fore.GREEN}...was the Impostor!")
    print(f'\n\n{Fore.MAGENTA}GG! Crewmates win!')

else:
    time.sleep(1.8)
    print(f"{Fore.RED}...was not the Impostor!")
    print(f"\n\nGAME OVER!\nPlayer {who_is_it()} was the Impostor!")

print(f"\n\n{Fore.YELLOW}Thank you for playing the BETA release of this game! <3{Fore.RESET}")

