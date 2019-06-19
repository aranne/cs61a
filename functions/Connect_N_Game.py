"""
You've probably heard of Connect 4, a two-player game where the players take turns dropping a colored piece from the top of a column in a grid.
The piece ends at the last empty spot in this column - that is, as close to the bottom as possible. A player can only put pieces in columns with open spaces.

The winner is the first player who gets N of their pieces next to each other - either horizontally, vertically or diagonally.
The game ends at this point, or as soon as the board is full.

We can generalize this game so that the goal is to connect N pieces instead of just 4.
Now, we will be implementing a command line version of Connect N!
"""
"""
##################################
### Build Connect N Game #########
##################################

Let's build the combat field for players 'X' and 'O'.
In this lab, we will represent the playing board as a list of lists.We call such a list two-dimensional because we can visualize it as a rectangle.
For instance, this list: [['-', '-', '-', '-'], ['O', 'O', 'O', 'X'], ['X', 'X', 'X', 'O']]
would represent the following board:
- - - -
O O O X
X X X O
Notice that just like lists are zero-indexed, our board is zero-indexed.
This means that the columns and rows in the above board would be numbered like this:
0  - - - -
1  O O O X
2  X X X O
   0 1 2 3
"""
"""
#####################################################################################################################
You will implemente the constructor and selectors as well as ways to modify the attributes of your abstract data type.
The function of the constructor is to create a empty board.
The function of the selectors is get a piece and put a piece on the specifically row and column.
Now, Lets implemente constructor and selectors for our Game!
#####################################################################################################################
"""

"""
#####################################
#### Create a empty board ###########
#####################################

We will represent an empty spot by the string '-'.
First, implement the function create_row, which returns one empty row in our board according to our abstraction
"""
def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    s = []
    for _ in range(size):
        s += ['-']
    return s

'''Then, use create_row to implement create_board, which returns a board with the specified dimensions.'''
def create_board(rows, columns):
    """Returns a board with the given dimensions.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    s = []
    for _ in range(rows):
        s += [create_row(columns)]
    return s
"""
##########################################
###### Update the board ##################
##########################################

Over the course of a game, the board will change and we will need to keep our representation of the board up-to-date.
To do so, we will be creating a new board that represents the new state of the game every time a piece is played.
Implement replace_elem, which takes a list, an index, and an element to be placed at that index in the returned new list.
"""
def replace_elem(lst, index, elem):
    """Create and return a new list whose elements are the same as those in
    LST except at index INDEX, which should contain element ELEM instead.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old   # check that replace_elem outputs a new list
    False
    """
    assert index >= 0 and index < len(lst), 'Index is out of bounds'
    s = lst[:]
    s[index] = elem
    return s
"""
##################################
####### Manipulate Pieces ########
##################################

Now that we have the board ready, let's make our selectors!
First, we need a way to find out which piece ('-', 'X' or 'O') is at a given position(row, column). Implement get_piece so it does this.
"""
def get_piece(board, row, column):
    """Returns the piece at location (row, column) in the board.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1] # Puts piece "X" in column 0 of board and updates board
    >>> board = put_piece(board, rows, 0, 'O')[1] # Puts piece "O" in column 0 of board and updates board
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    return board[row][column]
"""
implement put_piece, which places the given player's piece in the given column.
put_piece should return a 2-element tuple that contains (<row index>, <new board>).
The first element is the index of the row the piece ends up in, or -1 if the column is already full.
The second element is the new board after the piece has been placed. If the column was full then just return the original board.
"""
def put_piece(board, max_rows, column, player):
    """Puts PLAYER's piece in the bottommost empty spot in the given column of
    the board. Returns a tuple of two elements:

        1. The index of the row the piece ends up in, or -1 if the column
           is full.
        2. The new board
    max_rows: the boundary of the rows
    column: the column which player choose to put a piece in.
    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    row = max_rows - 1
    while row >= 0:
        if get_piece(board, row, column) == '-':
            board[row] = replace_elem(board[row], column, player)
            return [row, board]    # get out of the loop.
        row -= 1
    return [row, board]

"""
#####################################################################################################################################
!!!!!!! Now You are now crossing the abstraction barrier !!!!!!!!
You have now implemented the constructor and selectors as well as ways to modify the attributes of your abstract data type, the board.
From now on, you should never need to treat the board as if it were a list.
Instead, trust your abstraction barrier and use the functions you have written so far.
######################################################################################################################################

###########################
#### Make a move ##########
###########################
Let's first write a function for players to make a move in the game.
make_move should only place the piece on the board if the given column is actually on the board. It returns a 2-element tuple (row index, board).
If the move is valid, put a piece in the column and return the index of the row the piece ends up in as well as the new board.
If the move is invalid, make_move should return -1 and the original board, unchanged.
The arguments max_rows and max_cols describe the dimensions of the board and may be useful in determining whether or not a move is valid.
"""
def make_move(board, max_rows, max_cols, col, player):
    """Put player's piece in column COL of the board, if it is a valid move.
    Return a tuple of two values:

        1. If the move is valid, make_move returns the index of the row the
           piece is placed in. Otherwise, it returns -1.
        2. The updated board
    max_rows, max_cols: the boundary of the board
    col: the column which player choose to put a piece in.
    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    1
    >>> get_piece(board, 1, 0)
    'X'
    >>> row, board = make_move(board, rows, columns, 0, 'O')
    >>> row
    0
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    -1
    >>> row, board = make_move(board, rows, columns, -4, '0')
    >>> row
    -1
    """
    if col < 0 or col >= max_cols:
        return [-1, board]
    else:
        return put_piece(board, max_rows, col, player)
"""
######################################
#### Print and View the board ########
######################################

The function print_board takes in a board (as defined by our abstraction) and the dimensions of the board, and it prints out the current state of the board.
We would like our board to look good, and for this, strings do a better job than lists.
Thus, we would like the row ['X', 'X', 'O', '-'] to be printed as 'X X O -' where the pieces are separated by a single blank space.
A function that might come in handy is strip(), which removes leading and trailing whitespace from a string. For example:
>>> s = '   hello '
>>> s.strip()
'hello'
"""
def print_board(board, max_rows, max_cols):
    """Prints the board. Row 0 is at the top, and column 0 at the far left.
    max_rows, max_cols: the boundary of the board.
    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> print_board(board, rows, columns)
    - -
    - -
    >>> new_board = make_move(board, rows, columns, 0, 'X')[1]
    >>> print_board(new_board, rows, columns)
    - -
    X -
    """
    str = ''
    i = 0
    while i <= (max_rows - 1):
        str = ''
        j = 0   # when we use whlie loop, don't forget to reset j to 0.
        while j <= (max_cols - 1):
            str = str + ' ' + get_piece(board, i, j)
            j += 1
        str = str.strip()
        print(str)
        i += 1
"""
#############################
#### Check for winning ######
#############################

The last thing we need for our Connect N game to be fully functioning is the ability to detect a win.
let's implement two helper functions check_win_row, check_win_col, check_win_diagonal that check for horizontal, vertical and diagoanl wins for the given player.
the argument num_connect tells you how many adjacent pieces are needed for a win.
The arguments max_rows and max_cols describe the dimensions of the game board.
"""
def check_win_row(board, max_rows, max_cols, num_connect, row, player):
    """ Returns True if the given player has a horizontal win
    in the given row, and otherwise False.

    >>> rows, columns, num_connect = 4, 4, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    True
    >>> check_win_row(board, rows, columns, 4, 3, 'X')    # A win depends on the value of num_connect
    False
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')   # We only detect wins for the given player
    False
    """
    adjacent = 0
    row_left = 0
    while row_left < max_rows:
        piece = get_piece(board, row, row_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_left += 1
    return False

def check_win_column(board, max_rows, max_cols, num_connect, col, player):
    """ Returns True if the given player has a vertical win in the given column,
    and otherwise False.

    >>> rows, columns, num_connect = 5, 5, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 0, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    True
    >>> check_win_column(board, rows, columns, 4, 1, 'O')
    False
    >>> check_win_column(board, rows, columns, num_connect, 1, 'X')
    False
    """
    adjacent = 0
    col_top = 0
    while col_top < max_cols:
        piece = get_piece(board, col_top, col)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        col_top += 1
    return False

def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ Returns True if the given player has a diagonal win passing the spot
    (row, column), and False otherwise.
    """
    # Find top left of diagonal passing through (row, col).
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Loop through top left to bottom right diagonal and check for win.
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Find top right of diagonal passing through (row, col).
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Loop through top right to bottom left diagonal and check for win.
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False
"""
#################################
######### Winning !!! ###########
#################################

Finally, let's implement a way to check for any wins. Implement check_win so that it returns True if there is a win in any direction
that is, horizontally, vertically or diagonally.
"""
def check_win(board, max_rows, max_cols, num_connect, row, col, player):
    """Returns True if the given player has any kind of win passing through
    (row, col), and False otherwise.

    >>> rows, columns, num_connect = 2, 2, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'O')
    False
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    True

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    """
    diagonal_win = check_win_diagonal(board, max_rows, max_cols, num_connect,
                                      row, col, player)
    horizontal_win = check_win_row(board, max_rows, max_cols, num_connect, row, player)
    vertical_win = check_win_column(board, max_rows, max_cols, num_connect, col, player)
    if diagonal_win or horizontal_win or vertical_win:
        return True
    else:
        return False
"""
##################################################################################################################################
Congratulations, you just built your own Connect N game!
Next step is to build a play function!
That means to build a system, more like a real game, which contains the player, the playing process and the tells us who wins!
##################################################################################################################################

thanks to the layers of data abstraction, the play function is actually very simple.
Notice how we use your make_move, print_board, and check_win to play the game without even knowing how the board and pieces are implemented.
"""

import sys    # This is a system!

def other(player):
    """ Returns the given player's opponent.
    """
    if player == 'X':
        return 'O'
    return 'X'

def play(board, max_rows, max_cols, num_connect):
    max_turns = max_rows * max_cols
    playing = True
    print("Player 'X' starts")
    who = 'X'
    turns = 0

    while True:
        turns += 1
        if turns > max_turns:
            print("No more moves. It's a tie!")
            sys.exit()

        while True:
            try:
                col_index = int(input('Which column, player {}? '.format(who)))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue

            row_index, board = make_move(board, max_rows, max_cols, col_index, who)

            if row_index != -1:
                break

            print("Oops, you can't put a piece there")

        print_board(board, max_rows, max_cols)

        if check_win(board, max_rows, max_cols, num_connect, row_index, col_index, who):
            print("Player {} wins!".format(who))
            sys.exit()

        who = other(who)

def start_game():
    # Get all parameters for the game from user.
    while True:
        # Get num_connect from user.
        while True:
            try:
                num_connect = int(input('How many to connect (e.g. 4 for Connect 4)? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of rows for board from user.
        while True:
            try:
                 max_rows = int(input('How many rows? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of columns for board from user.
        while True:
            try:
                max_cols = int(input('How many columns? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        if max_rows >= num_connect or max_cols >= num_connect:
            break
        print("Invalid dimensions for connect {0}. Please try again.".format(num_connect))

    board = create_board(max_rows, max_cols)
    play(board, max_rows, max_cols, num_connect)     # Begin the Game!
