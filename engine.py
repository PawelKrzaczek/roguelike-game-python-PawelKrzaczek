from random import randint, choice

FOOD = '😁'
KEY = 'K'
ARMOR = 'A'
WEAPONS = 'W'


def create_board(width, height):
    board = [[' ' for _ in range(width)] for _ in range(height)]

    # Add walls
    for i in range(width):
        board[0][i] = '#'
        board[height - 1][i] = '#'
    for i in range(height):
        board[i][0] = '#'
        board[i][width - 1] = '#'

    # Add gates at fixed positions
    board[0][width // 2] = 'G'
    board[height - 1][width // 2] = 'G'
    board[height // 2][0] = 'G'
    board[height // 2][width - 1] = 'G'

    return board


def items(board):
    for _ in range(randint(8, 10)):
        x, y = randint(1, len(board) - 2), randint(1, len(board[0]) - 2)
        types = choice([FOOD, KEY, ARMOR, WEAPONS])
        item = {'type': types, 'position': [x, y]}
        if board[x][y] == ' ':
            board[x][y] = item


def put_player_on_board(board, player):
    x, y = player["position"][0], player["position"][1]
    board[x][y] = player["sign"]


def put_enemies_on_board(board, list_enemies):
    for enemy in list_enemies:
        x, y = enemy["position"][0], enemy["position"][1]
        if board[x][y] == ' ':
            board[x][y] = enemy


def attack(player, enemy):
    enemy["health"] -= player["attack"]
    if enemy["health"] > 0:
        if player["armor"] > 0:
            player["armor"] -= enemy["attack"]
        else:
            player["health"] -= enemy["attack"]


def game_over(player):
    if player["health"] <= 0:
        exit()


def move_player(board, player, direction):
    x, y = player["position"][0], player["position"][1]
    board[x][y] = ' '
    new_x, new_y = x, y
    enemy_sign = ""

    if direction == 'W' and board[x - 1][y] != '#':
        new_x -= 1
    elif direction == 'A' and board[x][y - 1] != '#':
        new_y -= 1
    elif direction == 'S' and board[x + 1][y] != '#':
        new_x += 1
    elif direction == 'D' and board[x][y + 1] != '#':
        new_y += 1

    if type(board[new_x][new_y]) == dict:
        if board[new_x][new_y]['type'] == '😁':
            player["health"] += 10
        elif board[new_x][new_y]['type'] == 'W':
            player["attack"] += 1
        elif board[new_x][new_y]['type'] == 'A':
            player["armor"] += 5
        elif board[new_x][new_y]['type'] == 'K':
            player["inventory"].append(board[new_x][new_y])
            print(player["inventory"])
        elif board[new_x][new_y]['type'] == 'P':
            attack(player, board[new_x][new_y])
            enemy_sign = board[new_x][new_y]['sign']
            game_over(player)
            if board[new_x][new_y]["health"] > 0:
                new_x, new_y = x, y

    player["position"][0] = new_x
    player["position"][1] = new_y
    return player, enemy_sign


def move_character(board, enemy):
    x, y = enemy["position"][0], enemy["position"][1]
    board[x][y] = ' '
    new_x, new_y = x, y

    direction = choice(['W', 'A', 'S', 'D'])

    if direction == 'W' and board[x - 1][y] != '#':
        new_x -= 1
    elif direction == 'A' and board[x][y - 1] != '#':
        new_y -= 1
    elif direction == 'S' and board[x + 1][y] != '#':
        new_x += 1
    elif direction == 'D' and board[x][y + 1] != '#':
        new_y += 1

    if type(board[new_x][new_y]) == dict:
        if board[new_x][new_y]['type'] == '😁':
            enemy["health"] += 10
        elif board[new_x][new_y]['type'] == 'W':
            enemy["attack"] += 1
        elif board[new_x][new_y]['type'] == 'A':
            enemy["armor"] += 5
        elif board[new_x][new_y]['type'] == 'K':
            enemy["inventory"].append(board[new_x][new_y])
        elif board[new_x][new_y]['type'] == '@':
            attack(enemy, board[new_x][new_y])
            if board[new_x][new_y]["health"] > 0:
                new_x, new_y = x, y

    enemy["position"][0] = new_x
    enemy["position"][1] = new_y
    return enemy