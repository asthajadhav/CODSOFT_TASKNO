# Tic-Tac-Toe AI using Minimax

board = [" "] * 9

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def minimax(is_ai):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    scores = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_ai else "X"
            score = minimax(not is_ai)
            board[i] = " "
            scores.append(score)

    return max(scores) if is_ai else min(scores)


def ai_move():
    best_score = -10

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


print("===== TIC-TAC-TOE AI =====")
print("You = X")
print("AI  = O")
print("Choose positions from 1 to 9.")

while True:
    show_board()

    try:
        move = int(input("Enter your position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid position. Try again.")
            continue

        board[move] = "X"

    except ValueError:
        print("Please enter a number.")
        continue

    if winner("X"):
        show_board()
        print("🎉 You won!")
        break

    if " " not in board:
        show_board()
        print("It's a draw!")
        break

    ai_move()

    if winner("O"):
        show_board()
        print("🤖 AI won!")
        break

    if " " not in board:
        show_board()
        print("It's a draw!")
        break