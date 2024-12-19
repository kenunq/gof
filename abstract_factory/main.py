from abc import ABC, abstractmethod

# Абстрактные компоненты лабиринта
class MapSite(ABC):
    @abstractmethod
    def enter(self):
        pass

class Wall(MapSite):
    def enter(self):
        return "You hit a wall."

# Конкретные компоненты лабиринта
class Room(MapSite):
    def __init__(self, room_number: int):
        self.room_number = room_number
        self.sides = {}

    def set_side(self, direction: str, map_site: MapSite):
        self.sides[direction] = map_site

    def enter(self):
        return f"You entered room {self.room_number}."

class Door(MapSite):
    def __init__(self, room1: Room, room2: Room):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

    def enter(self):
        if self.is_open:
            return "You passed through the door."
        else:
            return "The door is closed."

    def open(self):
        self.is_open = True

# Абстрактная фабрика
class MazeFactory(ABC):
    @abstractmethod
    def make_maze(self) -> MapSite:
        pass

    @abstractmethod
    def make_room(self, room_number: int) -> Room:
        pass

    @abstractmethod
    def make_wall(self) -> Wall:
        pass

    @abstractmethod
    def make_door(self, room1: Room, room2: Room) -> Door:
        pass

# Конкретная фабрика
class StandardMazeFactory(MazeFactory):
    def make_maze(self) -> MapSite:
        return {}

    def make_room(self, room_number: int) -> Room:
        return Room(room_number)

    def make_wall(self) -> Wall:
        return Wall()

    def make_door(self, room1: Room, room2: Room) -> Door:
        return Door(room1, room2)

# Клиентский код
class MazeGame:
    def create_maze(self, factory: MazeFactory) -> Room:
        # Создаем комнаты и дверь
        room1 = factory.make_room(1)
        room2 = factory.make_room(2)
        door = factory.make_door(room1, room2)

        # Настраиваем стороны для комнат
        room1.set_side("North", factory.make_wall())
        room1.set_side("East", door)
        room1.set_side("South", factory.make_wall())
        room1.set_side("West", factory.make_wall())

        room2.set_side("North", factory.make_wall())
        room2.set_side("East", factory.make_wall())
        room2.set_side("South", factory.make_wall())
        room2.set_side("West", door)

        # Возвращаем начальную комнату
        return room1

# Пример использования
if __name__ == "__main__":
    factory = StandardMazeFactory()
    game = MazeGame()
    maze_start = game.create_maze(factory)

    # Пример взаимодействия с лабиринтом
    print(maze_start.enter())  # Вы входите в комнату 1
    print(maze_start.sides["East"].enter())  # Дверь закрыта
    maze_start.sides["East"].open()  # Открываем дверь
    print(maze_start.sides["East"].enter())  # Вы проходите через дверь
    print(maze_start.sides["East"].room2.enter())  # Вы входите в комнату 2
