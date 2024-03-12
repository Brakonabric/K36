class WhoPlayFirst:
    def __init__(self):
        self._player = None

    def change_player(self, reset):
        if reset:
            self._player = None
        else:
            if self._player is None:
                self._player = "human"
            elif self._player == "human":
                self._player = "ai"
            else:
                self._player = "human"

    def current_player(self):
        return self.get_player

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @player.getter
    def get_player(self):
        return self._player


