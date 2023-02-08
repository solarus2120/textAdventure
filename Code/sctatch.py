import Data.locations_old
# import Data.config
# import Code.actions


def generate_location():
    print(Data.locations_old.how_big() + Data.locations_old.build_desc() +
          Data.locations_old.exits())
    # validate_location()


# def validate_location():
#    descr = Code.actions.get_value_from_location_key('Room ' + str(Data.config.room_cnt), 'Desc')
#    if 'NORTH' in descr:
#        Code.actions.mutate_value_from_dict_key('Room ' + str(Data.config.room_cnt), 'NORTH', 'True')
#    elif 'SOUTH' in descr:
#        Code.actions.mutate_value_from_dict_key('Room ' + str(Data.config.room_cnt), 'SOUTH', 'True')
#    elif 'EAST' in descr:
#        Code.actions.mutate_value_from_dict_key('Room ' + str(Data.config.room_cnt), 'EAST', 'True')
#    elif 'WEST' in descr:
#        Code.actions.mutate_value_from_dict_key('Room ' + str(Data.config.room_cnt), 'WEST', 'True')##
#
#    if Data.config.direction in descr:
#        Code.actions.mutate_value_from_dict_key('Room ' + str(Data.config.room_cnt),
#                                                Data.locations_old.direction, Data.locations_old.previous)
