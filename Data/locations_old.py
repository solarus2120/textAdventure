import random
import Code.actions
import Data.config

locations = [
    {
        'Location': 'Ruined Gatehouse',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': 'True',
        'Desc': 'A Gatehouse, tumbling into ruin. A set of stairs lead down into darkness',
        'Search': 'Disc'
    }
             ]

current = 'Ruined Gatehouse'
previous = ''
direction = 'NORTH'  # null this when finished

walls = ['glistening with moisture',
         'riddled with mold',
         'gleaming  marble',
         'festooned with roots',
         'covered with moss',
         'worked stone',
         'cracked bricks',
         'spotted with plaster',
         'painted with murals',
         'bare earth']


def build_desc():
    descr = 'The walls are {}. '.format(random.choice(walls))
    return descr


def how_big():
    x = random.randrange(10, 110, 10)
    y = random.randrange(10, 110, 10)
    dimension = 'This room is {} feet by {} feet. '.format(x, y)
    return dimension


def exits():
    exits_cnt = random.randrange(1, 5)
    exit1 = Code.actions.get_value_from_direction_key(Data.locations_old.direction)
    x = 1
    Data.config.exitx[1] = exit1

    if exits_cnt == 1:
        descr = 'There is only one exit to this room, in the {} wall\n'.format(Data.config.exitx[1])
    else:
        descr = 'There are {} exits from this room.\n'.format(exits_cnt)
        while x <= exits_cnt:
            if x == 1:
                descr = descr + 'There is an exit in the {} wall.\n'.format(Data.config.exitx[1])
            else:
                Data.config.exitx[x] = exit_direction(x)
                descr = descr + 'There is an exit in the {} wall.\n'.format(Data.config.exitx[x])
            x += 1
        Data.config.exitx = ['', '', '', '', '']
    return descr


def exit_direction(intx):
    rnd_exit = random.choice(['NORTH', 'SOUTH', 'EAST', 'WEST'])
    while rnd_exit in Data.config.exitx:
        rnd_exit = random.choice(['NORTH', 'SOUTH', 'EAST', 'WEST'])
        Data.config.exitx[intx] = rnd_exit
    return rnd_exit


def get_room_number():
    my_count = Data.config.room_cnt + 1
    name = 'Room {}'.format(my_count)
    Data.config.room_cnt = my_count
    return name
