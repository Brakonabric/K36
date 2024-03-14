def play_game(num, player, alg, humanScore, compScore):
    if player == "human":
        num, humanScore = playAsHuman(num, humanScore)
    else:
        num, compScore = playAsComp(num, compScore, alg)
    return num, humanScore, compScore

def playAsHuman(num, humanScore):
    if button() == "x2":
        num *= 2
        if num % 2 == 0:
            humanScore += 1
        else:
            humanScore -= 1
    elif button() == "x3":
        num *= 3
        if num % 2 == 0:
            humanScore += 1
        else:
            humanScore -= 1
    return num, humanScore

def button():
    return "x3"
    # return "x2"

def playAsComp(num, compScore, alg):
    if alg == "minimax":
        minimax(num)
        # num, compScore =  minimax(num)
    else:
        alfaBeta(num)
        # num, compScore =  alfaBeta(num)
    return num, compScore

def alfaBeta(num):
    pass
def minimax(num):
    pass


# print(play_game(15, "human", "minimax", 0, 0))
