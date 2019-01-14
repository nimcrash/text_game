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

            new_room = room.Room()
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

        self.rooms = rooms
        self.player = entity.Entity("player")

    def play(self, room_number):

        self.player.go_to(self.rooms[room_number])
        self.player.look_around()