import time
from Graph.partial_graph import minimax, alphabeta

defaultColor = '\033[0m'
titleColor = '\x1b[38;5;242m'
timeColor = '\x1b[38;5;181m'
nodeColor = '\x1b[38;5;229m'


class Game:
    def __init__(self, alg, score, root):
        self.root = root
        self.game_score = score
        self.alg = alg
        self._current_human_mult = None
        self.human_score = 0
        self.ai_score = 0

    def human_turn(self, value):
        before = self.game_score
        self._current_human_mult = value
        self.game_score = self.game_score * self._current_human_mult
        if self.game_score % 2 == 0:
            self.human_score += 1
        else:
            self.human_score -= 1

        print(
            f"\n\t\tHUMAN: X{self._current_human_mult}"
            f"\n\t\t\tDATA: {before} -> {self.game_score}"
            f"\n\n\t{titleColor}[ HUMAN: {self.human_score} | SCORE: {self.game_score} | AI: {self.ai_score} ]{defaultColor}"
        )

    def ai_turn(self):
        self.root.update()
        old_score = self.game_score
        # Алгоритм работает слишком быстро,
        # поэтому перед его выполнением мы делаем задержку в пол секунды,
        # чтобы GUI успел отобразить счёт игры перед ходом ИИ
        time.sleep(0.65)
        start_time = time.perf_counter()
        result = None
        if self.alg == "MINIMAX":
            result = minimax(self.game_score, self.ai_score, self.human_score)
        elif self.alg == "ALPHA-BETA":
            result = alphabeta(self.game_score, self.ai_score, self.human_score)
        end_time = time.perf_counter()
        self.game_score = result.number
        self.ai_score = result.p1_score
        print(
            f"\n\t\tAI: X{int(self.game_score / old_score)}"
            f"\t{timeColor}TIME: {round((end_time - start_time) * 1000, 5)} ms{defaultColor}"
            f"\n\t\t\tDATA: {old_score} -> {self.game_score}"
            f"\n\t\t{nodeColor}  NODES PASSED: {result.visited_nodes} pcs {defaultColor}"
            f"\n\n\t{titleColor}[ HUMAN: {result.p2_score} | SCORE: {result.number} | AI: {result.p1_score} ]{defaultColor}"
        )

    def get_data(self):
        return self.game_score, self.human_score, self.ai_score
