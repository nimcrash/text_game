import world
from GameOver import GameOver

def run_game():
    
    new_world = world.World()

    while True:
        try:
            turn(new_world)
        except GameOver:
            break
    print('Game over')

def turn(new_world):

    current_room = new_world.player.owner
    print("Вы в комнате %i" % (current_room.number + 1))

    room_numbers = []
    if len(current_room.ways) != 0:
        
        text = "Номера доступных для перехода комнат:"
        for room in current_room.ways:

            room_numbers.append(room.number)
            text += " %i" % (room.number + 1)

        print(text)
    
    if not current_room.owner is None:
        room_numbers.append(-1)
        print("Вернуться: 0")

    room_number = int(input("Выберите номер комнаты: ")) - 1
    if not room_number in room_numbers:
        print("Ударившись головой о стену, вы теряете сознание.")
        raise GameOver()

    print()

    new_world.play(room_number)

if __name__ == "__main__": 
    run_game()