#create board, position, display, check if win, tie, gameover,

board = ["-","-","-","-","-","-","-","-","-"]
game_still_going = True
winner = None
current_player = "A"
def display_board():
    print(board[0]+ " | " + board[1]+ " | " + board[2]) 
    print(board[3]+ " | " + board[4]+ " | " + board[5]) 
    print(board[6]+ " | " + board[7]+ " | " + board[8]) 

def play_game():
    display_board() 
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player() 
    if winner == "A" or winner == "B":
        print(winner + " won")
    elif winner == None:
        print("Tie")
def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:
            position = input("Invalid number. Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("The position is occupied, please choose again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    #rows
    row_winner = check_rows()

    #columns
    column_winner = check_column()

    #diagonal
    diagonal_winner = check_diagonals()
    if row_winner :
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #no winner
        winner = None
    return
def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_column():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_diagonals():
    global game_still_going


    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0] 
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None
    
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False 
    return
def flip_player():
    global current_player
    if current_player == "A":
        current_player = "B"
    elif current_player == "B":
        current_player = "A"
    return

play_game()