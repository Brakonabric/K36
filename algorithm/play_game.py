import time
from Graph.partial_graph import minimax, alphabeta

defaultColor = '\033[0m'
timeColor = '\x1b[38;5;181m'

class Game:
    def __init__(self, turn, alg, score, root):
        self.root = root
        self.game_score = score
        self.play_now = turn
        self.alg = alg
        self._current_human_mult = None
        self._human_score = 0
        self._ai_score = 0

    def human_turn(self, value):
        self._current_human_mult = value
        print(f"    HUMAN: X{self._current_human_mult}")

    def get_data(self, whose_turn):
        before = self.game_score
        if whose_turn == "human":
            self.game_score = self.game_score * self._current_human_mult
            if self.game_score % 2 == 0:
                self._human_score += 1
            else:
                self._human_score -= 1
            print(f"        DATA: {before} -> {self.game_score}")
        return self.game_score, self._human_score, self._ai_score

    def ai_turn(self):
        old_score = self.game_score
        self.root.update()
        # Алгоритм работает слишком быстро,
        # поэтому перед его выполнением мы делаем задержку в пол секунды,
        # чтобы GUI успел отобразить счёт игры перед ходом ИИ
        # time.sleep(0.6)
        result = None
        if self.play_now == "human":
            if self.alg == "Minimax":
                start_time = time.perf_counter()
                result = minimax(self.game_score, self._human_score, self._ai_score)
                end_time = time.perf_counter()
                print(f"{timeColor}Minimax time: {(end_time - start_time) * 1000} ms{defaultColor}")
            elif self.alg == "Alfa-beta":
                start_time = time.perf_counter()
                result = alphabeta(self.game_score, self._human_score, self._ai_score)
                end_time = time.perf_counter()
                print(f"{timeColor}AlphaBeta time: {(end_time - start_time) * 1000} ms{defaultColor}")

            self.game_score = result.number
            self._human_score = result.p1_score
            self._ai_score = result.p2_score
        else:
            if self.alg == "Minimax":
                start_time = time.perf_counter()
                result = minimax(self.game_score, self._ai_score, self._human_score)
                end_time = time.perf_counter()
                print(f"{timeColor}Minimax time: {(end_time - start_time) * 1000} ms{defaultColor}")
            elif self.alg == "Alfa-beta":
                start_time = time.perf_counter()
                result = alphabeta(self.game_score, self._ai_score, self._human_score)
                end_time = time.perf_counter()
                print(f"{timeColor}AlphaBeta time: {(end_time - start_time) * 1000} ms{defaultColor}")

            self.game_score = result.number
            self._human_score = result.p2_score
            self._ai_score = result.p1_score
        self.root.update()

        ai_mult = int(self.game_score / old_score)
        print(f"    AI: X{ai_mult}")
        print(f"        DATA: {old_score} -> {self.game_score}")
