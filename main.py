
import util
import engine
import ui
import time
from random import randint

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = dict()
    player["sign"] = PLAYER_ICON
    player["position"] = [PLAYER_START_X, PLAYER_START_Y]
    name = input("Your name: ")
    player["name"] = name
    race = input("Input race like(elf, dwarf)")
    player["race"] = race
    health = 50;
    player["armor"] = 0
    player["attack"] = 5
    player["health"] = health
    player["inventory"] = []
    return player


def create_character(name, type):
    character = dict()
    character["type"] = "P"
    character["position"] = [randint(1, BOARD_HEIGHT-1), randint(1, BOARD_WIDTH-1)]
    character["name"] = name
    character["sign"] = type
    health = 20
    character["armor"] = randint(0, 3)
    character["attack"] = randint(10, 15)
    character["health"] = health
    character["inventory"] = []
    return character


def create_boss():
    character = dict()
    character["type"] = "B"
    character["position"] = [11, 16]
    character["name"] = "BOSS"
    character["sign"] = "BOSS"
    health = 50
    character["armor"] = randint(10, 30)
    character["attack"] = randint(20, 25)
    character["health"] = health
    character["inventory"] = []
    return [character]


def main():
    player = create_player()
    list_enemies = list()
    list_enemies.append(create_character("ork", "ork"))
    list_enemies.append(create_character("smok", "smok"))
    boss = create_boss()

    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    engine.items(board)
    engine.put_enemies_on_board(board, list_enemies)

    board_boss = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    engine.put_enemies_on_board(board_boss, boss)

    # util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        ui.display_player(player)
        for enemy in list_enemies:
            ui.display_player(enemy)
        for enemy in boss:
            ui.display_player(enemy)

        key = util.key_pressed()
        if key == 'i':
            util.clear_screen()
            print(player["inventory"])
            time.sleep(3)
        if key == 'q':
            is_running = False
        else:
            player, boss_fight = engine.move_player(board, player, key.upper())
            if boss_fight is True:
                board = board_boss
            for i in range(len(list_enemies)):
            #    if list_enemies[i]['sign'] != enemy_sign:
             #       list_enemies[i] = engine.move_character(board, list_enemies[i])
                if list_enemies[i]["health"] <= 0:
                    list_enemies.pop(i)
            for i in range(len(boss)):
                if boss[i]["health"] <= 0:
                    util.clear_screen()
                    print("WIN")
                    time.sleep(5)
                    return
        util.clear_screen()


if __name__ == '__main__':
    main()
