import world

def run_game():
    
    new_world = world.World()

    while True:
        try:
            turn(new_world)
        except Exception as GameOver:
            break
    print('Game over')

def turn(new_world):

    room_number = int(input("Выбери номер комнаты (1-5): ")) - 1
    if not room_number in range(0,5):
        print("Ударившись головой о стену, вы теряете сознание.")
        raise GameOver

    new_world.play(room_number)

if __name__ == "__main__": 
    run_game()