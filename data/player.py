class WhoPlayFirst:
    def __init__(self):
        self._player = None

    def change_player(self, reset):
        if reset:
            self._player = None
        else:
            if self._player is None:
                self._player = "HUMAN"
            elif self._player == "HUMAN":
                self._player = "AI"
            else:
                self._player = "HUMAN"

    def current_player(self):
        return self._player
