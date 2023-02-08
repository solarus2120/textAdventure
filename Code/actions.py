import Data.locations
import Data.config
import Code.sctatch


def get_value_from_location_key(key, search):
    dic = None
    for item in Data.locations.locations:
        if item['Location'] == key:
            dic = item
    return dic[search]


def get_current_location():
    current = Data.locations.current
    return current


def set_location(currprev, location):
    if currprev == 'current':
        Data.locations.current = location
    else:
        Data.locations.previous = location


def move(direction):
    current = get_current_location()
    Data.locations.previous = current

    if validate_direction(direction):
        target = get_value_from_location_key(current, direction)
        Data.locations.direction = direction

    if target == '' or not (validate_direction(direction)):
        print('You cannot move {}'.format(direction))
        target = current
    else:
        set_location('previous', Code.actions.get_current_location())
        set_location('current', target)
        if Data.config.light_level > 0:
            Data.config.light_level -= 1


def quit_game():
    Data.config.active_play = False


def validate_direction(supplied):
    if supplied != 'NORTH' and supplied != 'SOUTH' and supplied != 'EAST' and supplied != 'WEST' \
            and supplied != 'UP' and supplied != 'DOWN':
        return False
    else:
        return True


def help_command():
    Data.config.help_list.sort()
    for item in Data.config.help_list:
        print(item)


def search_location():
    location = get_current_location()
    item = get_value_from_location_key(location, 'Search')
    print('You search the {}'.format(location))
    if item == '':
        print('You find nothing')
    else:
        print('You find {}'.format(item))
        update_inventory(item)
        mutate_value_from_dict_key(location, 'Search', '')


def update_inventory(new):
    Data.config.inventory.append(new)
    Data.config.inventory.sort
    print('{} added to Inventory'.format(new))


def list_inventory():
    for item in Data.config.inventory:
        print(item)


def mutate_value_from_dict_key(key, search, value):  # Has a test
    dic = None
    for item in Data.locations.locations:
        if item['Location'] == key:
            dic = item
            dic[search] = value
    return dic[search]


def back_command():
    print("You return to the previous location")
    set_location('current', Data.locations.previous)


def get_value_from_direction_key(key):
    value = None
    search_key = str(key)
    if search_key in Data.config.direction.keys():
        value = Data.config.direction.get(search_key)
    return value


def use_command(item):
    if validate_item(item):
        if item == 'TORCH':
            Data.config.light_level += 12
            Data.config.inventory.remove(item)
    else:
        print("You cannot use {}!".format(item))


def validate_item(test):
    valid = False
    for item in Data.config.inventory:
        if item == test:
            valid = True
    return valid


def victory_condition():
    results = False
    if 'STONE HEART' in Data.config.inventory and 'IRON LUNG' in Data.config.inventory \
            and 'DISEASED BRAIN' in Data.config.inventory and 'DESICCATED SOUL' in Data.config.inventory \
            and 'ROTTEN STOMACH' in Data.config.inventory:
        results = True
    return results
