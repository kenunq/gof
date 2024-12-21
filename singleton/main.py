class MazeFactory:
    """Базовый класс для создания лабиринта"""
    def make_maze(self):
        return "Maze"

    def make_wall(self):
        return "Wall"

    def make_room(self, room_number):
        return f"Room {room_number}"

    def make_door(self, room1, room2):
        return f"Door between {room1} and {room2}"


class SingletonMazeFactory(MazeFactory, metaclass=type):
    """Singleton для фабрики лабиринтов"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def make_bombed_room(self, room_number):
        return f"Bombed Room {room_number}"

    def make_enchanted_maze(self):
        return "Enchanted Maze"


# Использование Singleton MazeFactory
if __name__ == "__main__":
    factory1 = SingletonMazeFactory()
    factory2 = SingletonMazeFactory()

    print(factory1 is factory2)  # True
    print(factory1.make_room(1))  # Room 1
    print(factory1.make_bombed_room(2))  # Bombed Room 2
