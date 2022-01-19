'''
Assignment: Tic-Tac-Toe
Christopher Higham
January 10, 2022
'''

def change_xo(x_o):
    '''
    Switch turns. If x just went, switch to o. If o just went, switch 
    back to x. Takes a string char, returns a string char.
    Parameters:
        x_o: The last player to make a move.
    Returns: Updated turn
    '''
    if x_o == 'x':
        x_o = 'o'
    elif x_o == 'o':
        x_o = 'x'
    
    return x_o

def replace_number(x_o, tic_tac_toe, int_list):
    '''
    Asks the user which space to occupy with an x or o. Returns an 
    updated tic-tac-toe table.
    Parameters:
        x_o: The player to make the next move.
        tic_tac_toe: The string tic_tac_toe table containing 1-9 and/
            or x's and o's.
        int_list: a list of digits in string format 1-9 representing
            all possible available spaces.
    Returns: An updated tic_tac_toe table as a string.
    '''
    escape = 0
    
    while escape == 0:
        first_choice = input(f'{x_o.upper()}\'s turn. Pick a number (1-9): ')
        
        if first_choice in list(tic_tac_toe):
            tic_tac_toe_new = tic_tac_toe.replace(first_choice, x_o)
            int_list.remove(f'{first_choice}')
            escape = 1
        else:
            print('try again')
    
    return tic_tac_toe_new

def check_for_cats_game(short_ttt, winner):
    '''
    If all possible moves have been made and there still is no winner, 
    declare the winner to be a "cats game". This works best if the rest 
    of the program has been run and there is still no winner.
    Parameters:
        short_ttt: A short list representation of the tic_tac_toe board
            with a length of 9, containing string characters 1-9 and/or
            x's and o's.
        winner: A string value that should be x, o or blank.
    Returns: the game winner (cats game if no more moves)
    '''
    l = []
    for space in short_ttt:
        if space in ('x', 'o'):
            pass
        else:
            l.append('not done yet')
            break
    if len(l) == 0:
        winner = 'cats game'
    return winner

def check_for_winner(tic_tac_toe):
    '''
    Check for 3 in a row in any direction, or for a cats game
    Parameters:
        tic_tac_toe: The string tic_tac_toe table containing 1-9 and/
            or x's and o's.
    Returns: Status of the winner (should be blank, x, o, or cats game).
    '''
    short_ttt = tic_tac_toe.replace('\n', '').replace('-', '').replace('+', '').replace('|', '')
    winner = ''
    
    # Check for vertical 3-in-a-row (3R) (3 instances)
    #print(list(short_ttt))
    if (short_ttt[0] == 'x') and (short_ttt[3] == 'x') and (short_ttt[6] == 'x'):
        winner = 'x'
    elif (short_ttt[0] == 'o') and (short_ttt[3] == 'o') and (short_ttt[6] == 'o'):
        winner = 'o'
    if (short_ttt[1] == 'x') and (short_ttt[4] == 'x') and (short_ttt[7] == 'x'):
        winner = 'x'
    elif (short_ttt[1] == 'o') and (short_ttt[4] == 'o') and (short_ttt[7] == 'o'):
        winner = 'o'
    if (short_ttt[2] == 'x') and (short_ttt[5] == 'x') and (short_ttt[8] == 'x'):
        winner = 'x'
    elif (short_ttt[2] == 'o') and (short_ttt[5] == 'o') and (short_ttt[8] == 'o'):
        winner = 'o'

    # Check for horizontal 3R (3 instances)
    if (short_ttt[0] == 'x') and (short_ttt[1] == 'x') and (short_ttt[2] == 'x'):
        winner = 'x'
    elif (short_ttt[0] == 'o') and (short_ttt[1] == 'o') and (short_ttt[2] == 'o'):
        winner = 'o'
    if (short_ttt[3] == 'x') and (short_ttt[4] == 'x') and (short_ttt[5] == 'x'):
        winner = 'x'
    elif (short_ttt[3] == 'o') and (short_ttt[4] == 'o') and (short_ttt[5] == 'o'):
        winner = 'o'
    if (short_ttt[6] == 'x') and (short_ttt[7] == 'x') and (short_ttt[8] == 'x'):
        winner = 'x'
    elif (short_ttt[6] == 'o') and (short_ttt[7] == 'o') and (short_ttt[8] == 'o'):
        winner = 'o'

    # Check for diagonal 3R (2 instances)
    if (short_ttt[0] == 'x') and (short_ttt[4] == 'x') and (short_ttt[8] == 'x'):
        winner = 'x'
    elif (short_ttt[0] == 'o') and (short_ttt[4] == 'o') and (short_ttt[8] == 'o'):
        winner = 'o'
    if (short_ttt[2] == 'x') and (short_ttt[4] == 'x') and (short_ttt[6] == 'x'):
        winner = 'x'
    elif (short_ttt[2] == 'o') and (short_ttt[4] == 'o') and (short_ttt[6] == 'o'):
        winner = 'o'
    
    # Check for cats game
    if winner == '':
        winner = check_for_cats_game(short_ttt, winner)
    
    # return the winning player
    return winner



def main():
    # Set up game
    tic_tac_toe = '\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n'
    int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    x_o = 'x'
    winner = ''
    print(tic_tac_toe)

    # Iterate, taking turns, until game over
    while winner == '':
        tic_tac_toe = replace_number(x_o, tic_tac_toe, int_list)
        x_o = change_xo(x_o)
        winner = check_for_winner(tic_tac_toe)
        print(tic_tac_toe)
    
    # Undo extra turn switch
    x_o = change_xo(x_o)

    # Declare the results
    if winner in ('x', 'o'):
        print(f'{x_o.upper()} wins! great game!')
    else:
        print(f'{winner.title()}! It\'s a tie! Great game!')

if __name__ == '__main__':
    main()
