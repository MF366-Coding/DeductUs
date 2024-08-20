# ai for DeductUs

# [!?] A lil' bit of Korn for y'all Swiftees out there
'''
This place inside my mind
A place I like to hide
You don't know the chances
What if I should die?

A place inside my brain
Another kind of pain
You don't know the chances

I'm so blind
Blind
Blind
'''

# [i] (Blind by Korn)

import random

# [*] anyways time to hit the code :sunglasses:


class ImpostorAI:
    def __init__(self, player_color: tuple[int, int, int]):
        self._status = [player_color[0], player_color[1], player_color[2], False, 0, 0, 0, 0, False, False, 0, False, False]
        
    def kill_crewmate(self, lobby_class):
        alive_crew = []
        
        for crew, statuses in lobby_class.lobby.items():
            if statuses[13] is True:
                continue
            
            if statuses[3] is False:
                alive_crew.append(crew)
                
            elif statuses[11] is False and statuses[12] is False:
                alive_crew.append(crew)
                
            else:
                continue
            
        who_to_kill = random.choice(alive_crew) # [i] bye bye lol
        
        
                
