import random

import Code.actions
import Data.config
import Data.locations
import time


def play():
    while Data.config.active_play:
        print(Code.actions.get_current_location())
        if Data.config.light_level > 0 or Data.locations.current == 'Ruined Gatehouse':
            print(Code.actions.get_value_from_location_key(Code.actions.get_current_location(), 'Desc'))
        else:
            print('Your Torch has gone out. It is too dark to see')
            gru_check()

        if Data.locations.current == 'Altar Room' \
                and Code.actions.victory_condition():
            print('You place the 5 treasures in the body upon the altar.\n'
                  'A sonorous chant begins.\n'
                  'He is risen.\n'
                  'He is risen.')
            time.sleep(3)
            print('The body sits up, and the eyes turn to gaze upon you.')
            time.sleep(2)
            print('I am risen. You have my thanks. Now, begone')
            time.sleep(2)
            Code.actions.set_location('current', 'Ruined Gatehouse')
            print(Code.actions.get_value_from_location_key(Code.actions.get_current_location(), 'Desc'))
            time.sleep(2)
            print('You won. Well Done.')
            Code.actions.quit_game()
        else:
            user_input()


def user_input():
    user_in = input("What would you like to do? ")
    if user_in[:4].upper() == 'MOVE':
        Code.actions.move(user_in[5:].upper())
    elif user_in[:4].upper() == 'QUIT':
        Code.actions.quit_game()
    elif user_in[:4].upper() == 'HELP':
        Code.actions.help_command()
    elif user_in[:6].upper() == 'SEARCH':
        Code.actions.search_location()
    elif user_in[:9].upper() == 'INVENTORY':
        Code.actions.list_inventory()
    elif user_in[:4].upper() == 'BACK':
        Code.actions.back_command()
    elif user_in[:3].upper() == 'USE':
        Code.actions.use_command(user_in[4:].upper())
    else:
        print("Invalid command. Please type 'help' for a list of valid commands")


def gru_check():
    check_value = random.randint(1, 6)
    if check_value == 6:
        print("In the darkness, you did not see what came for you./nYou are, however, most assuredly, dead.")
        Code.actions.quit_game()


# def generate_location():
#    Data.locations_old.locations.append({'Location': 'TEST_LOCATION',
#                                     'NORTH': 'TEST_NORTH',
#                                     'EAST': 'TEST_EAST',
#                                     'SOUTH': 'TEST_SOUTH',
#                                     'WEST': 'TEST_WEST',
#                                     'UP': 'TEST_UP',
#                                     'DOWN': 'TEST_DOWN',
#                                     'Desc': 'TEST_DESC',
#                                     'Search': 'TEST_SEARCH'})
