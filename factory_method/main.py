class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def __str__(self):
        return f"Maze with rooms: {list(self.rooms.keys())}"


class Room:
    def __init__(self, room_number):
        self.room_number = room_number

    def __str__(self):
        return f"Room {self.room_number}"


class Wall:
    def __str__(self):
        return "Wall"


class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2

    def __str__(self):
        return f"Door between Room {self.room1.room_number} and Room {self.room2.room_number}"


# Фабричный метод в базовом классе
class MazeFactory:
    def make_maze(self):
        return Maze()

    def make_room(self, room_number):
        return Room(room_number)

    def make_wall(self):
        return Wall()

    def make_door(self, room1, room2):
        return Door(room1, room2)


# Конкретная фабрика для создания лабиринта с "комнатами с бомбами"
class BombedMazeFactory(MazeFactory):
    def make_room(self, room_number):
        return RoomWithBomb(room_number)


# Конкретная фабрика для создания "волшебного" лабиринта
class EnchantedMazeFactory(MazeFactory):
    def make_room(self, room_number):
        return EnchantedRoom(room_number)

    def make_door(self, room1, room2):
        return EnchantedDoor(room1, room2)


# Дополнительные классы для BombedMazeFactory
class RoomWithBomb(Room):
    def __str__(self):
        return f"Room {self.room_number} with a bomb"


# Дополнительные классы для EnchantedMazeFactory
class EnchantedRoom(Room):
    def __str__(self):
        return f"Enchanted Room {self.room_number}"


class EnchantedDoor(Door):
    def __str__(self):
        return f"Enchanted Door between Room {self.room1.room_number} and Room {self.room2.room_number}"


# Клиентский код
def create_maze(factory: MazeFactory):
    maze = factory.make_maze()

    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    door = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    print(f"Adding {room1}")
    print(f"Adding {room2}")
    print(f"Adding {door}")

    return maze


if __name__ == "__main__":
    # Используем обычную фабрику
    print("Standard Maze:")
    standard_factory = MazeFactory()
    maze = create_maze(standard_factory)
    print(maze)

    print("\nBombed Maze:")
    bombed_factory = BombedMazeFactory()
    bombed_maze = create_maze(bombed_factory)
    print(bombed_maze)

    print("\nEnchanted Maze:")
    enchanted_factory = EnchantedMazeFactory()
    enchanted_maze = create_maze(enchanted_factory)
    print(enchanted_maze)
