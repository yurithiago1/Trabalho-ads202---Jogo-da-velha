def minimax(board, player):



    free = find_empty_cells(board)

    game_over, score = terminal_state(board, free)
    if game_over:
        result = {'index': None, 'score': score}
        return result

    moves = []
    for i in free:
        move = {"index": None, "score": None}
        move["index"] = i

        board[i] = player

        if player == AI_PLAYER:
            result = minimax(board, HUMAN_PLAYER)
        else:
            result = minimax(board, AI_PLAYER)
        move["score"] = result["score"]
        moves.append(move)

        board[i] = move["index"]

    if player == AI_PLAYER:
        best_score = -10000
        for i in moves:
            if i["score"] > best_score:
                best_score = i["score"]
                best_move = i
    else:
        best_score = 10000
        for i in moves:
            if i["score"] < best_score:
                best_score = i["score"]
                best_move = i
    return best_move


def terminal_state(board, free):


    game_over = False
    score = None

    if won(board, HUMAN_PLAYER):
        game_over = True
        score = -10

    elif won(board, AI_PLAYER):
        game_over = True
        score = 10

    elif not free:
        game_over = True
        score = 0

    return game_over, score


def won(board, player):


    cond1 = board[0] == player and board[1] == player and board[2] == player
    cond2 = board[3] == player and board[4] == player and board[5] == player
    cond3 = board[6] == player and board[7] == player and board[8] == player
    cond4 = board[0] == player and board[3] == player and board[6] == player
    cond5 = board[1] == player and board[4] == player and board[7] == player
    cond6 = board[2] == player and board[5] == player and board[8] == player
    cond7 = board[0] == player and board[4] == player and board[8] == player
    cond8 = board[2] == player and board[4] == player and board[6] == player

    if cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8:
        return True
    return False


def find_empty_cells(board):


    return [x for x in board if x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]


def check_game_status(board):


    cond1 = board[0] == board[1] and board[1] == board[2]
    cond2 = board[3] == board[4] and board[4] == board[5]
    cond3 = board[6] == board[7] and board[7] == board[8]
    cond4 = board[0] == board[3] and board[3] == board[6]
    cond5 = board[1] == board[4] and board[4] == board[7]
    cond6 = board[2] == board[5] and board[5] == board[8]
    cond7 = board[0] == board[4] and board[4] == board[8]
    cond8 = board[2] == board[4] and board[4] == board[6]

    if cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8:
        return True

    for i in board:
        if i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return False

    return True


def print_board(board):


    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("---------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("---------")
    print("{} | {} | {}".format(board[6], board[7], board[8]))
    # print("=========")
    # print("=========")
    # print("=========")


def human_turn(board):


    valid = False
    empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not valid:
        human_choice = int(input("Onde gostaria de jogar?\n"))
        if board[human_choice] in empty:
            valid = True
        else:
            print("A celula escolhida esta ocupada.\n")
    board[human_choice] = HUMAN_PLAYER

    print("=========")
    print("Humano Joga:")
    print("=========")
    print_board(board)

    return board


def ai_turn(board):

    ai_choice = minimax(board, AI_PLAYER)
    board[ai_choice["index"]] = AI_PLAYER

    print("=========")
    print("Computador Joga:")
    print("=========")
    print_board(board)

    return board


def main():


    global HUMAN_PLAYER
    global AI_PLAYER
    HUMAN_PLAYER = "a"
    while HUMAN_PLAYER.lower() not in ["x", "o"]:
        HUMAN_PLAYER = input("Escolha seu simbolo: \n")
    AI_PLAYER = "x"
    if HUMAN_PLAYER == AI_PLAYER:
        AI_PLAYER = "o"

    # Decide who starts first
    first = "a"
    while first.lower() not in ["Sim", "nao", "s", "n"]:
        first = input("Quer começar primeiro?\n")

    # Begin game
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    if first in ["sim", "s"]:
        game_over = check_game_status(board)
        board = human_turn(board)

        while not game_over:
            game_over = check_game_status(board)
            if game_over:
                break
            board = ai_turn(board)
            game_over = check_game_status(board)
            if game_over:
                break
            board = human_turn(board)
    else:
        game_over = check_game_status(board)
        board = ai_turn(board)

        while not game_over:
            game_over = check_game_status(board)
            if game_over:
                break
            board = human_turn(board)
            game_over = check_game_status(board)
            if game_over:
                break
            board = ai_turn(board)
    if won(board, AI_PLAYER):
        print("GAME OVER. Você perdeu!.")

    elif won(board, HUMAN_PLAYER):
        print("GAME OVER. Você ganhou!.")
    else:
        print("GAME OVER. Empate!.")


if __name__ == "__main__":
    main()