import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, sign):
    for row in board:
        if row.count(sign) == 3:
            return True
    for col in range(3):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(sign) == 3:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def computer_move(board, sign):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = sign
            if check_win(board, sign):
                return True
            board[row][col] = " "
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    sign = input("Choose X or O: ")
    if sign not in ["X", "O"]:
        sign = "X"
    comp_sign = "O" if sign == "X" else "X"
    print(f"You chose {sign}, computer is {comp_sign}")
    toss = random.randint(0, 1)
    if toss:
        print("Computer wins the toss")
        if not computer_move(board, comp_sign):
            while True:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter col (1-3): ")) - 1
                if board[row][col] == " ":
                    board[row][col] = sign
                    print_board(board)
                    if check_win(board, sign):
                        print("You win!")
                        break
                    if not computer_move(board, comp_sign):
                        print("Draw!")
                        break
    else:
        print("You win the toss")
        while True:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter col (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = sign
                print_board(board)
                if check_win(board, sign):
                    print("You win!")
                    break
                if not computer_move(board, comp_sign):
                    print("Draw!")
                    break

if __name__ == "__main__":
    main()