locations = [
    {
        'Location': 'Ruined Gatehouse',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': 'Grand Gallery',
        'Desc': 'A Gatehouse, tumbling into ruin. A set of stairs lead down into darkness\n'
                'Seek the treasures and then the Altar Room',
        'Search': ''
    },
    {
        'Location': 'Grand Gallery',
        'NORTH': 'Hall of Statues',
        'EAST': 'Flooded Passage',
        'SOUTH': 'Cracked Room',
        'WEST': '',
        'UP': 'Ruined Gatehouse',
        'DOWN': '',
        'Desc': 'This gallery is 50 feet by 60 feet. The walls are bare earth. There are 3 exits from this room,'
                ' in the North, South and East walls. Stairs lead up towards the light.',
        'Search': ''
    },
    {
        'Location': 'Hall of Statues',
        'NORTH': '',
        'EAST': '',
        'SOUTH': 'Grand Gallery',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 80 feet by 20 feet and lined with stone statues. The walls are glistening with moisture. '
                'There is only one exit to this room, in the South wall',
        'Search': 'STONE HEART'
    },
    {
        'Location': 'Flooded Passage',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': 'Grand Gallery',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 20 feet by 50 feet and slopes to the East. The walls are gleaming marble. '
                'There is only one exit to this room, in the West wall. There are stairs that lead down to the South, '
                'but they are blocked by flooding',
        'Search': ''
    },
    {
        'Location': 'Cracked Room',
        'NORTH': 'Grand Gallery',
        'EAST': 'Stairwell',
        'SOUTH': 'Grotto',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 40 feet by 30 feet. The walls are worked stone. '
                'There are 3 exits to this room, in the North, South and East walls',
        'Search': ''
    },
    {
        'Location': 'Stairwell',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': 'Cracked Room',
        'UP': '',
        'DOWN': 'Dusty Room',
        'Desc': 'This room is 10 feet by 10 feet. The walls are gleaming marble. '
                'There are 2 exits to this room, a set of stairs leading deeper underground '
                'and an exit in the West wall.',
        'Search': ''
    },
    {
        'Location': 'Grotto',
        'NORTH': 'Cracked Room',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 90 feet by 20 feet. The walls are spotted with plaster. '
                'There is only one exit to this room, in the North wall',
        'Search': ''
    },
    {
        'Location': 'Dusty Room',
        'NORTH': 'Storage Room',
        'EAST': 'Hex Room',
        'SOUTH': 'Spike Room',
        'WEST': 'Scriptorum',
        'UP': 'Stairwell',
        'DOWN': '',
        'Desc': 'This room is 30 feet by 30 feet. The walls are cracked bricks. '
                'There are 5 exits to this room, a set of stairs leading upwards '
                'and an exit in each of the North, East, South and West walls.',
        'Search': ''
    },
    {
        'Location': 'Spike Room',
        'NORTH': 'Dusty Room',
        'EAST': '',
        'SOUTH': '',
        'WEST': 'Band Room',
        'UP': '',
        'DOWN': 'Staircase',
        'Desc': 'This room is 40 feet by 30 feet. The walls are bare earth. There are 3 exits from this room'
                'in the North and West walls, and a set of stairs leading down.',
        'Search': ''
    },
    {
        'Location': 'Scriptorum',
        'NORTH': '',
        'EAST': 'Dusty Room',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 50 feet by 10 feet. The walls are festooned with roots. '
                'There is one exit from this room, in the East wall.',
        'Search': 'DISEASED BRAIN'
    },
    {
        'Location': 'Storage Room',
        'NORTH': '',
        'EAST': '',
        'SOUTH': 'Dusty Room',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 30 feet by 20 feet. The walls are gleaming marble. '
                'There is only one exit to this room, in the South wall',
        'Search': ''
    },
    {
        'Location': 'Hex Room',
        'NORTH': '',
        'EAST': 'Animal Room',
        'SOUTH': 'Tea Room',
        'WEST': 'Dusty Room',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 20 feet by 40 feet. The walls are covered with moss. There are 3 exits from this room'
                'in the East, West and South walls.',
        'Search': ''
    },
    {
        'Location': 'Animal Room',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': 'Hex Room',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 70 feet by 50 feet. The walls are glistening with moisture. '
                'There is only one exit to this room, in the West wall',
        'Search': ''
    },
    {
        'Location': 'Tea Room',
        'NORTH': 'Hex Room',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 50 feet by 90 feet. The walls are glistening with moisture. '
                'There is only one exit to this room, in the North wall',
        'Search': 'ROTTEN STOMACH'
    },
    {
        'Location': 'Band Room',
        'NORTH': '',
        'EAST': 'Spike Room',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'his room is 90 feet by 50 feet. The walls are glistening with moisture. '
                'There is only one exit from this room, in the East wall.',
        'Search': 'IRON LUNG'
    },
    {
        'Location': 'Staircase',
        'NORTH': '',
        'EAST': '',
        'SOUTH': 'Salon',
        'WEST': 'Music Room',
        'UP': 'Spike Room',
        'DOWN': 'Altar Room',
        'Desc': 'This room is 20 feet by 30 feet. The walls are cracked bricks. There are 4 exits from this room \n'
                'in the South and West walls, and a set of stairs leading both up and down.',
        'Search': ''
    },
    {
        'Location': 'Music Room',
        'NORTH': '',
        'EAST': 'Staircase',
        'SOUTH': 'Dance Hall',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 20 feet by 10 feet. The walls are bare earth. '
                'There are 2 exits from this room in the South and East walls.',
        'Search': ''
    },
    {
        'Location': 'Dance Hall',
        'NORTH': 'Music Room',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 60 feet by 70 feet. The walls are covered with moss. '
                'There is only one exit to this room, in the North wall',
        'Search': 'DESICCATED SOUL'
    },
    {
        'Location': 'Salon',
        'NORTH': 'Staircase',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': '',
        'DOWN': '',
        'Desc': 'This room is 90 feet by 70 feet. The walls are worked stone. '
                'There is only one exit to this room, in the North wall',
        'Search': ''
    },
    {
        'Location': 'Altar Room',
        'NORTH': '',
        'EAST': '',
        'SOUTH': '',
        'WEST': '',
        'UP': 'Staircase',
        'DOWN': '',
        'Desc': 'This room is 10 feet by 10 feet. The walls are not present, the starry darkness expands infinitely.'
                'Upon an altar lies a body, missing the brain, heart, lungs and stomach.'
                'A single stairway leads up to the floor above.',
        'Search': ''
    }
             ]

current = 'Ruined Gatehouse'
previous = ''
