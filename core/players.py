# Player related features


class Lobby:
    def __init__(self, number_of_players: int, number_of_impostors: int, player_color: tuple[str, str, str], ai_class):        
        self._AI = ai_class
        self._NUM_PLAYERS = number_of_players
        self._NUM_IMPOSTORS = number_of_impostors
        self._PLAYER_COLOR = player_color
        
        self._lobby = {
            # [i] color (name); color (Fore); light/dark; killed; no of accusations; no of defends; no of player accusations; no of player defends; vented (TRACK); sus (PSYCHIC); good/bad (SCAN); eliminated by vote; innocent voted out; impostor;
            "#000": [player_color[0], player_color[1], player_color[2], False, 0, 0, 0, 0, False, False, 0, False, False, False]
        }
        
    def add_ready_ai(self, ai):
        raise NotImplementedError('TODO') # TODO
    
    @property
    def lobby(self):
        return self._lobby
