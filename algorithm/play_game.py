import random
import time

from Graph.partial_graph import minimax, alphabeta


class Game:
    def __init__(self, turn, alg, score, root):
        self.root = root
        self.game_score = score
        self.play_now = turn
        self.alg = alg
        self._current_ai_mult = 3
        self._current_human_mult = None
        self._human_score = 0
        self._ai_score = 0
        self._iter = 0

    def get_iter(self):
        self._iter += 1
        return self._iter

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
        elif whose_turn == "ai":
            if self.play_now == "human":
                player1 = self._human_score
                player2 = self._ai_score
                self._human_score,  = self.ai_turn(player1, player2)

            else:
                player2 = self._human_score
                player1 = self._ai_score
                self.ai_turn(player1, player2)


            # # ВЫЗОВ класса для получения объекта вершины
            # self.game_score = self.game_score * self._current_ai_mult # = счёт игры из вершины
            # if self.game_score % 2 == 0: # УДАЛИТЬ ИФ
            #     self._ai_score += 1      # УДАЛИТЬ ИФ
            # else:                        # УДАЛИТЬ ИФ
            #     self._ai_score -= 1 # = счёт ИИ из вершины

        print(f"        DATA: {before} -> {self.game_score}")
        return self.game_score, self._human_score, self._ai_score

    def ai_turn(self, player1, player2):
        self.root.update()
        if self.alg == "Minimax":
            return minimax(self.game_score, player1, player2)

        elif self.alg == "Alfa-beta":
            return alphabeta(self.game_score, player1, player2)


        # time.sleep(0.5)
        # self._current_ai_mult = random.randint(2, 3)
        # print(f"    AI: X{self._current_ai_mult}")