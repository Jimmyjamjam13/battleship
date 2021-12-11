from random import randint


class Board:

    """Board Class."""

    score = 0

    def __init__(self, name, size, ship_nums, person):
        self.name = name
        self.size = size
        self.ship_nums = ship_nums
        self.person = person
        self.board = [['|  ' for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        """
        Adds and prints player and computer board.
        """
        for row in self.board:
            print(' '.join(row))

    def add_ships(self, row, col):
        """
        adds ships to board.
        """
        if (row, col) not in self.ships:
            self.ships.append((row, col))
        else:
            self.ships.append((row, col))
            if self.person == "player":
                self.board[row][col] = "@"


def random_number(size):
    """
    Returns random integer
    """
    return randint(0, (size) - 1)


def get_name():
    """Enter name entered"""
    name = input('Please enter your name here:\n')
    while name == '':
        print('You need to enter name.\n')
        name = input('Please enter your name here:\n')
        return name
    return name


def get_user_data():
    """
    Collects information from user to set up the game
    """
    while True:
        print('Numbers must be between 5 and 10\n')
        size = input('Size of your square board:\n')
        print('Validating input...\n')

        new_size = validate_user_data(size, 5, 10)

        if new_size:

            ships = input('Number of ships on each board:\n')
            print('Validating input...\n')

            new_ships = validate_user_data(ships, 5, 10)

            if new_ships:
                break

    return [size, ships]


def validate_user_data(values, value_one, value_two):
    """
    Checks if "values" is an integer
    """
    try:
        if values.isnumeric() is False:
            raise ValueError(
                f'You must enter a number.. you entered "{values}"\n'
            )
        elif int(values) < value_one or int(values) > value_two:
            print(f'Invalid Input: Number entered {values} is not in range\n')
            print('Please try again...')
            return False
    except ValueError as error:
        print(f'Invalid input: {error}\nPlease try again...\n')
        return False

    return True


def populate_game_board(board):
    """
    Then populates game board.
    """
    print('~' * 60)
    print(f"{board.name}'s board:\n")

    size = board.size

    while len(board.ships) != board.ship_nums:
        row = random_number(size)
        col = random_number(size)
        board.add_ships(row, col)

    board.print_board()


def make_guess(board):
    """
    guess for computer and player.
    """
    size = board.size
    while True:
        if board.person == 'computer':
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            print('~' * 60)
            row_guess = input('Enter row num:\n')
            col_guess = input('Enter column num:\n')
            print('~' * 60)

        row = validate_user_data(str(row_guess), 0, (size - 1))
        col = validate_user_data(str(col_guess), 0, (size - 1))

        if row and col:
            break

    return [int(row_guess), int(col_guess)]


def validate_guess(board, other_board, row, col):
    """
    Validates player input.
    """
    if (row, col) in board.guesses:
        print(f'{board.name}, you already guessed {(row, col)}.')
        print('Please try again...')
        return False

    if (row, col) in other_board.ships:
        board.guesses.append((row, col))
        other_board.board[row][col] = '| O'
        print(f"{board.name}'s coordinates {(row, col)}")
        print('A Battleship has been hit!')
        print('~' * 60)
        return True
    else:
        board.guesses.append((row, col))
        other_board.board[row][col] = '| X'
        print(f"{board.name}'s coordinates {(row, col)}")
        print('Missed target...')
        print('~' * 60)


def play_game(board, other_board, ships):
    """
    Runs the game.
    .
    """
    while True:
        populate_game_board(board)
        populate_game_board(other_board)

        player_guess = make_guess(board)
        p_row = player_guess[0]
        p_col = player_guess[1]
        valid = validate_guess(board, other_board, p_row, p_col)
        if valid is False:
            return play_game(board, other_board, ships)

        comp_guess = make_guess(other_board)
        c_row = comp_guess[0]
        c_col = comp_guess[1]
        valid_two = validate_guess(other_board, board, c_row, c_col)
        if valid_two is False:
            board.guesses.pop()
            return play_game(board, other_board, ships)

        scores(board, valid)
        scores(other_board, valid_two)
        print('~' * 60)
        next_round = input('Press Enter to continue or "q" to quit.\n')
        if next_round == 'Enter':
            continue
        elif next_round == 'q':
            break
        if len(other_board.guesses) == ships:
            break
    print(f"{board.name}'s score is: {board.score}")
    print(f"{other_board.name}'s score is: {other_board.score}\n")
    if board.score > other_board.score:
        print(f'{board.name} won this game.')
        print('Yor won congrats')
    elif board.score < other_board.score:
        print(f'Ha {other_board.name} won this game. You lost')
    elif board.score == other_board.score:
        print('Both side are equal. Try again.')


def scores(board, hit):
    """
    If a ship is hit, updates class board score by adding 1.
    """
    if hit:
        board.score += 1
        print(f"{board.name}'s score is: {board.score}")
    else:
        print(f"{board.name}'s score is: {board.score}")


def new_game():
    """
    Runs main game.
    """
    print(" Welcome to BATTLESHIPS!!")
    name = get_name()
    print(f"Hi {name}. Let's go through some rules first...\n")
    print('~' * 60)
    print('1. Top left hand corner is row 0,\n col 0 (0, 0)\n')
    print('2. Number of rounds will be equal to\n your number of ships\n')
    print('3. Number of rows will be equal to\n the number of columns')
    print('~' * 60)
    input('Press Enter to start your game.\n')
    print('Starting game...\n')
    data = get_user_data()
    size = int(data[0])
    num_of_ships = int(data[1])
    print('~' * 60)
    print(f'Remember, rows and cols will now\n range from 0 to {size - 1}\n')
    print(f'Ships to hit: {num_of_ships}  \nTotal rounds: {num_of_ships}')
    print('~' * 60)
    print('Creating new game...\n')

    player_board = Board(name, size, num_of_ships, person='player')
    computer_board = Board('Computer', size, num_of_ships, person='computer')
    play_game(player_board, computer_board, num_of_ships)

    populate_game_board(player_board)

    populate_game_board(computer_board)
    print('~' * 60)
    print('Play again?\n')
    replay = input('Enter "y" to play another or "n" to quit the game:\n')
    if replay == 'y':
        new_game()
    else:
        print(f'Well played {player_board.name}. Goodbye for now!\n')


new_game()
