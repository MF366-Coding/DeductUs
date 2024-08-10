from colorama import Fore
import random
from icecream import ic
import sys
from os import system
from requests import get
from requests import exceptions as ex_req
import time
import json

platform = sys.platform
force_sim_debug = False
version = "2.0.0"
# [i] Initial Release


def get_latest() -> str | None:
    """
    get_latest verifies for updates

    Returns:
        str | None: the latest version found on GitHub
    """
    latest_version = None
    
    try:
        response = get('https://api.github.com/repos/MF366-Coding/DeductUs/releases/latest', timeout=3.5)
        data = json.loads(response.text)
        latest_version = data['tag_name']

    except (ex_req.ConnectTimeout, ex_req.ConnectionError, TimeoutError, ex_req.ReadTimeout):
        latest_version = None
        
    return latest_version
        

# [!!] Things to uncomment on release and commit
ic.disable()

# [!!] This one is to stay commented lol 
# force_sim_debug = True


ic.configureOutput("debug statement | ")

def clear():
    """
    clear clears the screen/terminal

    It uses the correct command for each OS.
    """
    
    if platform == "win32":
        system("cls")
    else:
        system("clear")

clear()


