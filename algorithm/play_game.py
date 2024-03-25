import random
import time


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
        print(f"    HUMAN:{self._current_human_mult}")

    def get_data(self, whose_turn):
        if whose_turn == "human":
            self.game_score = self.game_score * self._current_human_mult
            if self.game_score % 2 == 0:
                self._human_score += 1
            else:
                self._human_score -= 1
        elif whose_turn == "ai":
            # ВЫЗОВ класса для получения объекта вершины
            self.game_score = self.game_score * self._current_ai_mult # = счёт игры из вершины
            if self.game_score % 2 == 0: # УДАЛИТЬ ИФ
                self._ai_score += 1      # УДАЛИТЬ ИФ
            else:                        # УДАЛИТЬ ИФ
                self._ai_score -= 1 # = счёт ИИ из вершины

        print(f"    DATA: {self.game_score}")
        return self.game_score, self._human_score, self._ai_score

    def ai_turn(self):
        self.root.update()
        time.sleep(1)
        self._current_ai_mult = random.randint(2, 3)
        print(f"    AI:{self._current_ai_mult}")

# def play_game(num, player, alg, humanScore, compScore):
#     if player == "human":
#         num, humanScore = playAsHuman(num, humanScore)
#     else:
#         num, compScore = playAsComp(num, compScore, alg)
#     return num, humanScore, compScore
#
# def playAsHuman(num, humanScore):
#     if button() == "x2":
#         num *= 2
#         if num % 2 == 0:
#             humanScore += 1
#         else:
#             humanScore -= 1
#     elif button() == "x3":
#         num *= 3
#         if num % 2 == 0:
#             humanScore += 1
#         else:
#             humanScore -= 1
#     return num, humanScore
#
# def button():
#     return "x3"
#     # return "x2"
#
# def playAsComp(num, compScore, alg):
#     if alg == "minimax":
#         minimax(num)
#         # num, compScore =  minimax(num)
#     else:
#         alfaBeta(num)
#         # num, compScore =  alfaBeta(num)
#     return num, compScore
#
# def alfaBeta(num):
#     pass
# def minimax(num):
#     pass
#
#
# # print(play_game(15, "human", "minimax", 0, 0))
