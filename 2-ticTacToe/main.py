'''COSA DEVE FARE IL GIOCO:
    1. Creare la board
    2. Visualizzare la board
    3. Funzione che avvia il gioco
    4. Funzione che fa cambio dei turni
    5. Funzione che dice se qualcuno vince
        5.1 Controlla righe
        5.2 Controlla colonne
        5.3 Controlla diagonali
    6. Funzione che prenda gli input dell'utente
'''

#1: la board sarà composta semplicemente di 9 trattini che indicano che nessuno li ha toccati
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

game_is_still_going = True

winner = None


current_player = "X"


#2:fare display della board
def display_board ():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

#3:funzione principale che fa avviare gioco
def play_game():

    display_board()
    while game_is_still_going:
        handle_turn(current_player)
        check_if_game_is_over()
        flip_players()
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("tie")






#4:f che fa girare ruoli
def handle_turn (player):
    print (player + "'s turn")
    position = input("Choose a position between 1-9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position)] != "-":
            position = input("Invalid input. Choose a position between 1-9: ")
        position = int(position) - 1 #-1 perchè gli indici partono da zero

        if board[position] == "-":
            valid = True
        else:
            print("Position already occuped.1"
                  " ")
    board[position] = player
    display_board()


#5: controllo se qualcuno ha vinto/caselle piene
def check_if_game_is_over():
    check_if_win()
    check_if_tie()

def check_if_win():

    global winner  #in questo modo vado a modificare a var winner fuori

    row_winner = check_rows() #dice se qualcuno ha vinto e chi
    diagonal_winner = check_diagonals()
    columns_winner = check_columns()
    if row_winner:
        #qualcuno vince
        winner = row_winner
    elif diagonal_winner:
        # #qualcuno vince
        winner = diagonal_winner
    elif columns_winner:
        # qualcuno vince
        winner = columns_winner
    else:
        #nessuno vince
        winner = None
    return



#le funzioni di check row/colum/diagonal ritornano il giocatore che vince "X, O" oppure None
def check_rows():
    global game_is_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_is_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

def check_diagonals():
    global game_is_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        game_is_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None

def check_columns():
    global game_is_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_is_still_going = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_if_tie():
    global game_is_still_going
    #vedo se esiste ancora "-" nella lista: se si allora non è finito
    if "-" not in board:
        game_is_still_going = False
    return




def flip_players():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()