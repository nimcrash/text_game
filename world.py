import random
import room
import entity

class World:

    def __init__(self):

        positions = [i for i in range(0,5)]
            
        key_position = random.choice(positions)
        positions.remove(key_position)

        door_position = random.choice(positions)
        positions.remove(door_position)

        smth_position = random.choice(positions)
        positions.remove(smth_position)

        rooms = []  
        for i in range(0,5):

            new_room = room.Room(i)
            if i == key_position:

                key = entity.Entity("key", new_room)             
                new_room.objects.update({"key" : key})

            elif i == door_position:

                door = entity.Entity("door", new_room)                 
                new_room.objects.update({"door" : door})

            elif i == smth_position:

                smth_special = entity.Entity("smth_special", new_room)   
                new_room.objects.update({"smth_special" : smth_special})

            rooms.append(new_room)

        #определение путей
        available_rooms = rooms.copy()
        
        new_room = random.choice(available_rooms)
        available_rooms.remove(new_room)
        way_tree(new_room, available_rooms)
        
        self.rooms = rooms
        self.player = entity.Entity("player", new_room)

        self.player.look_around()

    def play(self, room_number):

        #костыльно, в новых условиях правильно передавать непосредственно комнату, но я хочу спать
        room_number = self.player.owner.owner.number if room_number == -1 else room_number

        self.player.go_to(self.rooms[room_number])
        self.player.look_around()

def way_tree(room, available_rooms):
 
    available_rooms_count = len(available_rooms)

    # 0 - тупик 
    # комната не может быть тупиковй, если с неё стартует игрок
    if room.owner is None:
        range_start = 1
    # комната не может быть тупиковой, если она единственная у родителя, и не все комнаты распределены
    elif len(room.owner.ways) == 1 and available_rooms_count > 0:
        range_start = 1
    else:
        range_start = 0

    # количество максимально возможных путей из каждой комнаты равно 2
    # дверь на выход тоже учитвается как путь
    
    if "door" in room.objects:
        range_stop = 2;
    else:
        range_stop = 3;

    available_ways_count = range(range_start, range_stop)
    ways = random.choice(available_ways_count)
    if available_rooms_count < ways:
        ways = available_rooms_count

    if ways != 0:

        for i in range(ways):

            random_room = random.choice(available_rooms)
            random_room.owner = room
            room.ways.append(random_room)
            available_rooms.remove(random_room)

        for way in room.ways:
            way_tree(way, available_rooms) 

