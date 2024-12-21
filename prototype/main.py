import copy


# Абстрактный класс, задающий интерфейс клонирования
class Prototype:
    def clone(self):
        raise NotImplementedError("Subclass must implement clone method")


# Лабиринт
class Maze(Prototype):
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def get_room(self, room_number):
        return self.rooms.get(room_number)

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Maze with rooms: {', '.join(str(room) for room in self.rooms.values())}"


# Комната
class Room(Prototype):
    def __init__(self, room_number):
        self.room_number = room_number
        self.sides = {"north": None, "south": None, "east": None, "west": None}

    def set_side(self, direction, map_site):
        self.sides[direction] = map_site

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        sides = ", ".join(f"{dir}: {type(site).__name__}" for dir, site in self.sides.items())
        return f"Room {self.room_number} with sides ({sides})"


# Комната с бомбой
class RoomWithBomb(Room):
    def __str__(self):
        sides = ", ".join(f"{dir}: {type(site).__name__}" for dir, site in self.sides.items())
        return f"Room {self.room_number} (with a bomb) with sides ({sides})"


# Стена
class Wall(Prototype):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Wall"


# Дверь
class Door(Prototype):
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

    def open(self):
        self.is_open = True

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Door between Room {self.room1.room_number} and Room {self.room2.room_number}"


# Клиентский код
if __name__ == "__main__":
    # Создаем оригинальные компоненты лабиринта
    maze = Maze()

    # Создаем комнаты
    room1 = Room(1)
    room2 = RoomWithBomb(2)

    # Создаем стену и дверь
    wall = Wall()
    door = Door(room1, room2)

    # Задаем стороны комнат
    room1.set_side("north", wall)
    room1.set_side("east", door)
    room1.set_side("south", wall)
    room1.set_side("west", wall)

    room2.set_side("north", wall)
    room2.set_side("east", wall)
    room2.set_side("south", wall)
    room2.set_side("west", door)

    # Добавляем комнаты в лабиринт
    maze.add_room(room1)
    maze.add_room(room2)

    print("Original Maze:")
    print(maze)

    # Клонируем лабиринт
    cloned_maze = maze.clone()

    # Добавляем новую комнату в клон
    room3 = Room(3)
    door2 = Door(room2, room3)

    room3.set_side("north", wall)
    room3.set_side("east", wall)
    room3.set_side("south", wall)
    room3.set_side("west", door2)

    cloned_maze.add_room(room3)
    room2.set_side("east", door2)  # Обновляем дверь в оригинальной комнате 2

    print("\nCloned Maze:")
    print(cloned_maze)

    print("\nOriginal Maze After Cloning:")
    print(maze)
