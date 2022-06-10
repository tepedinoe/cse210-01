# Edson MR Tepedino - CSE 210 -Tic-Tac-Toe game 
import array
winning = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]

def main():
    board_dimension = 3
    print("******** Tic-Tac-Toe game ********")

    board_spaces = array.array('i', [1,2,3,4,5,6,7,8,9])
    player1_spaces = initialize_spaces(board_dimension)
    player2_spaces = initialize_spaces(board_dimension)
    winner = 0

    print_board(board_spaces, board_dimension, player1_spaces, player2_spaces)

    for turn in range(board_dimension * board_dimension):
        player_turn = (turn % 2) + 1
        
        position = 0
        while position == 0 or  position == 'o' :
            entered_position = input("Player " + get_player_character(player_turn) + " is your turn, please enter a position number: ")
            position = get_numeric_value(entered_position)         

            if position == 0:
                print("\nInvalid position number!\n")

            elif position > (board_dimension * board_dimension):
                print("\nInvalid position number!\n")
                position = 0

            elif player2_spaces[position-1] != "" or player1_spaces[position-1] != "":
                print("\nPostion is already taken!\n")
                position = 0            

        if player_turn == 1:
            player1_spaces[position-1] = "x"
        else:
            player2_spaces[position-1] = "o"

        winner = check_for_winner(player1_spaces, player2_spaces)        
        print_board(board_spaces, board_dimension, player1_spaces, player2_spaces)

        if winner > 0:
            print(f"\nPlayer {get_player_character(player_turn)} wins!. End of the match.\n")
            break


    if winner == 0:
        print("\nNobody wins :), You both are awesome players!\n")


def initialize_spaces(dim):
    new_spaces = []
    for i in range(dim * dim):
        new_spaces.append('')
    return new_spaces
    
def print_board(spaces, dim, player1, player2):
    print()
    for s in spaces:
        
        if player1[s-1] != '':
            print('x', end = "")
        elif player2[s-1] != '':
            print('o', end = "")
        else:
            print(s, end = "")
        if s % dim == 0:
            print("\n-+-+-")
        else:
            print("|", end = "")
    print()

def check_for_winner(player1, player2):
    winner = 0
    for win_case in winning:
        wins = True
        for val in win_case:
            wins = wins and player1[val-1] != ""
        
        if wins == True:
            winner = 1
            break
    return winner


def get_numeric_value(text_value):
    if text_value.strip().isnumeric():
        return int(text_value)
    return 0

def get_player_character(player_numer):
    if player_numer == 1:
        return "x"
    else:
        return "o"

if __name__ == "__main__":
    main()