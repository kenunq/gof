class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def get_room(self, room_number):
        return self.rooms.get(room_number)

    def __str__(self):
        return f"Maze with rooms: {list(self.rooms.keys())}"


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.sides = {}

    def set_side(self, direction, element):
        self.sides[direction] = element

    def __str__(self):
        return f"Room {self.room_number} with sides: {self.sides}"


class Wall:
    def __str__(self):
        return "Wall"


class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

    def __str__(self):
        return f"Door between Room {self.room1.room_number} and Room {self.room2.room_number}"


# Направления для сторон комнаты
class Direction:
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"


# Базовый класс Строителя
class MazeBuilder:
    def __init__(self):
        self.maze = None

    def build_maze(self):
        self.maze = Maze()

    def build_room(self, room_number):
        raise NotImplementedError

    def build_door(self, room1, room2):
        raise NotImplementedError

    def get_maze(self):
        return self.maze


# Конкретный строитель, который строит стандартный лабиринт
class StandardMazeBuilder(MazeBuilder):
    def build_room(self, room_number):
        if self.maze.get_room(room_number) is None:
            room = Room(room_number)
            room.set_side(Direction.NORTH, Wall())
            room.set_side(Direction.SOUTH, Wall())
            room.set_side(Direction.EAST, Wall())
            room.set_side(Direction.WEST, Wall())
            self.maze.add_room(room)

    def build_door(self, room1_number, room2_number):
        room1 = self.maze.get_room(room1_number)
        room2 = self.maze.get_room(room2_number)
        if room1 is not None and room2 is not None:
            door = Door(room1, room2)
            room1.set_side(Direction.EAST, door)
            room2.set_side(Direction.WEST, door)


# Директор, управляющий процессом построения
class MazeDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_maze(self):
        self.builder.build_maze()
        self.builder.build_room(1)
        self.builder.build_room(2)
        self.builder.build_door(1, 2)


# Клиентский код
if __name__ == "__main__":
    builder = StandardMazeBuilder()
    director = MazeDirector(builder)
    director.construct_maze()

    maze = builder.get_maze()
    print(maze)
    for room_number, room in maze.rooms.items():
        print(room)
