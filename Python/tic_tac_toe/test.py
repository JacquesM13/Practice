board = '| TL | TM | TR |\n --------------\n| ML | MM | MR |\n --------------\n| BL | BM | BR |'
game_squares = {'TL': ' ',
                'TM': ' ',
                'TR': ' ',
                'ML': ' ',
                'MM': ' ',
                'MR': ' ',
                'BL': ' ',
                'BM': ' ',
                'BR': ' ', }

play_board = f'| {game_squares["TL"]} | {game_squares["TM"]} | {game_squares["TR"]} |\n--------------\n| {game_squares["ML"]} | {game_squares["MM"]} | {game_squares["MR"]} |\n--------------\n| {game_squares["BL"]} | {game_squares["BM"]} | {game_squares["BR"]} |'

print(board)

# Won if (TL, TM, TR) or (ML, MM, MR) or (BL, BM, BR) or (TL, ML, BL) or (TM, MM, BM) or (TR, MR, BR) or
# (TL, MM, BR) or (TR, MM, BL) all the same

winning = {'TL': 'O',
           'TM': 'O',
           'TR': 'O'}

xs_won = False
os_won = False

while not (xs_won or os_won):
    user_input = input('Where do you want to put your "X"?: ')
    if user_input == 'quit':
        break
    game_squares[user_input] = 'X'
    play_board = f'| {game_squares["TL"]} | {game_squares["TM"]} | {game_squares["TR"]} |\n--------------\n| {game_squares["ML"]} | {game_squares["MM"]} | {game_squares["MR"]} |\n--------------\n| {game_squares["BL"]} | {game_squares["BM"]} | {game_squares["BR"]} |'
    print(play_board)
    if set(winning.items()).issubset(game_squares.items()):
        xs_won = True
        break

    user_input = input('Where do you want to put your "O"?: ')
    if user_input == 'quit':
        break
    game_squares[user_input] = 'O'
    play_board = f'| {game_squares["TL"]} | {game_squares["TM"]} | {game_squares["TR"]} |\n--------------\n| {game_squares["ML"]} | {game_squares["MM"]} | {game_squares["MR"]} |\n--------------\n| {game_squares["BL"]} | {game_squares["BM"]} | {game_squares["BR"]} |'
    print(play_board)
    if set(winning.items()).issubset(game_squares.items()):
        os_won = True
        break

if xs_won:
    print('Xs won!')

if os_won:
    print('Os won!')