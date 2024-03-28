class UsingAlgorithm:
    def __init__(self):
        self._alg = None

    def change_alg(self, reset):
        if reset:
            self._alg = None
        else:
            if self._alg is None:
                self._alg = "ALPHA-BETA"
            elif self._alg == "ALPHA-BETA":
                self._alg = "MINIMAX"
            else:
                self._alg = "ALPHA-BETA"

    def current_alg(self):
        return self._alg
