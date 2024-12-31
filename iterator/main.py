class Iterator:
    """Абстрактный интерфейс итератора."""

    def first(self):
        raise NotImplementedError("Метод first() должен быть переопределён.")

    def next(self):
        raise NotImplementedError("Метод next() должен быть переопределён.")

    def is_done(self):
        raise NotImplementedError("Метод is_done() должен быть переопределён.")

    def current_item(self):
        raise NotImplementedError("Метод current_item() должен быть переопределён.")


class ConcreteIterator(Iterator):
    """Конкретный итератор."""

    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current_index = 0

    def first(self):
        self.current_index = 0

    def next(self):
        self.current_index += 1

    def is_done(self):
        return self.current_index >= len(self.aggregate)

    def current_item(self):
        if self.is_done():
            raise StopIteration("Итератор вышел за пределы коллекции.")
        return self.aggregate[self.current_index]


class Aggregate:
    """Абстрактный интерфейс агрегата."""

    def create_iterator(self):
        raise NotImplementedError("Метод create_iterator() должен быть переопределён.")


class ConcreteAggregate(Aggregate):
    """Конкретный агрегат."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self):
        return ConcreteIterator(self.items)


if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item(1)
    aggregate.add_item(2)
    aggregate.add_item(3)

    iterator = aggregate.create_iterator()

    print("Обход коллекции:")
    while not iterator.is_done():
        print(iterator.current_item())
        iterator.next()
