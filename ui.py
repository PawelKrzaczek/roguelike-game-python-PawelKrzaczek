def display_board(board):
    for row in board:
        for elem in row:
            if type(elem) == dict:
                print(elem['type'], end="")
            else:
                print(elem, end="")
        print()


def display_player(player):
    print("Name:", player["name"], "Attack:", player["attack"], "Armor:", player["armor"], "Health:", player["health"])
    print(player)