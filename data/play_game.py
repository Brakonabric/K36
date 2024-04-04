import time
from data.partial_graph import minimax, alphabeta


class Game:
    def __init__(self, alg, score, root):
        self.root = root
        self.game_score = score
        self.alg = alg
        self._current_human_mult = None
        self.human_score = 0
        self.ai_score = 0
        self.defaultColor = '\033[0m'
        self.titleColor = '\x1b[38;5;242m'
        self.timeColor = '\x1b[38;5;181m'
        self.nodeColor = '\x1b[38;5;229m'

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
            f"\n\n\t{self.titleColor}[ HUMAN: {self.human_score} | SCORE: {self.game_score} | AI: {self.ai_score} ]{self.defaultColor}"
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
            f"\t{self.timeColor}TIME: {round((end_time - start_time) * 1000, 5)} ms{self.defaultColor}"
            f"\n\t\t\tDATA: {old_score} -> {self.game_score}"
            f"\n\t\t{self.nodeColor}  NODES PASSED: {result.visited_nodes} pcs {self.defaultColor}"
            f"\n\n\t{self.titleColor}[ HUMAN: {result.p2_score} | SCORE: {result.number} | AI: {result.p1_score} ]{self.defaultColor}"
        )

    def get_data(self):
        return self.game_score, self.human_score, self.ai_score
