board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

# Function to print the game board
def print_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])
    
# Function to handle player's turn
def take_turn(player):
    print(player,"'s turn:")
    position=input("Enter the position from 1-9:")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position=input("Invalid position! Enter position from 1-9:")
    position=int(position)-1
    while board[position] != "_":
        position=int(input("Position already marked,enter new position:"))-1
    board[position]=player
    print_board()


def check_game_over():
    # Winning conditions
    if (board[0] == board[1] == board[2] != "_")or \
       (board[3] == board[4] == board[5] != "_")or \
       (board[6] == board[7] == board[8] != "_")or \
       (board[0] == board[3] == board[6] != "_")or \
       (board[1] == board[4] == board[7] != "_")or \
       (board[2] == board[5] == board[8] != "_")or \
       (board[0] == board[4] == board[8] != "_")or \
       (board[2] == board[4] == board[6] !="_") :
        return "win"
    elif "_" not in board:
        return "tie"
    else:
        return "play"

def play_game():
    print_board()
    current_player="X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        result=check_game_over()
        if result=="win":
            print(current_player," wins!")
            game_over=True
        elif result=="tie":
            print("It's Tie!!")
            game_over=True
        else:
            current_player="O" if current_player=="X" else "X"

# Start the game
play_game()

# OUTPUT
# PS C:\Users\Sanika\OneDrive\Desktop\IT\.vscode\AI\TIC_TAC_TOE> python tic-tac-toe.py
# _ | _ | _
# _ | _ | _
# _ | _ | _
# X 's turn:
# Enter the position from 1-9:1
# X | _ | _
# _ | _ | _
# _ | _ | _
# O 's turn:
# Enter the position from 1-9:2
# X | O | _
# _ | _ | _
# _ | _ | _
# X 's turn:
# Enter the position from 1-9:5
# X | O | _
# _ | X | _
# _ | _ | _
# O 's turn:
# Enter the position from 1-9:9
# X | O | _
# _ | X | _
# _ | _ | O
# X 's turn:
# Enter the position from 1-9:7
# X | O | _
# _ | X | _
# X | _ | O
# O 's turn:
# Enter the position from 1-9:3
# X | O | O
# _ | X | _
# X | _ | O
# X 's turn:
# Enter the position from 1-9:4
# X | O | O
# X | X | _
# X | _ | O
# X  wins!