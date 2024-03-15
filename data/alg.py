class UsingAlgorithm:
    def __init__(self):
        self._alg = None

    def change_alg(self, reset):
        if reset:
            self._alg = None
        else:
            if self._alg is None:
                self._alg = "Alfa-beta"
            elif self._alg == "Alfa-beta":
                self._alg = "Minimax"
            else:
                self._alg = "Alfa-beta"

    def current_alg(self):
        return self._alg

    # @property
    # def alg(self):
    #     return self._alg
    #
    # @alg.setter
    # def alg(self, value):
    #     self._alg = value
    #
    # @alg.getter
    # def get_alg(self):
    #     return self._alg
