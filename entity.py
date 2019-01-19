from GameOver import GameOver
class Entity:

    def __init__(self, name, owner = None):
        
        self.name = name
        self.owner = owner
        self.objects = {}

    def go_to(self, new_owner):
        
        #Уходим
        if not self.owner is None:
            if self.name in self.owner.objects:          
                del self.owner.objects[self.name]

        #Приходим
        new_owner.objects.update({self.name : self})
        self.owner = new_owner 

    def look_around(self):

        objects_around = self.owner.objects

        if "key" in objects_around:
            
            print("Ключ найден!")
            objects_around["key"].go_to(self)

        if "smth_special" in objects_around:

            print('В комнате на столе лежит флаг. Надпись на нём гласит: "Aestas non semper durabit: condite nidos!" Хороший совет, пожалуй стоит взять его с собой')
            objects_around["smth_special"].go_to(self)

        if "door" in objects_around:

            text = "Дверь! Путь на свободу лежит из этой комнаты"
            
            if "key" in self.objects:

                print(text + " и ключ как раз уже у Вас. Вперед в неизвестность!")
                raise GameOver()

            else:

                print(text + ", но ключа у Вас еще нет. Советую просто запомнить номер.")