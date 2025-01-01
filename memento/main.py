class Memento:
    """Хранитель для сохранения состояния."""

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    """Создатель, который может создавать и восстанавливать состояния."""

    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Установлено состояние: {state}")
        self._state = state

    def get_state(self):
        return self._state

    def save_to_memento(self):
        print(f"Сохранено состояние: {self._state}")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Восстановлено состояние: {self._state}")


class Caretaker:
    """Хранитель, управляющий состояниями Memento."""

    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    # Установка состояний и их сохранение
    originator.set_state("Состояние 1")
    caretaker.add_memento(originator.save_to_memento())

    originator.set_state("Состояние 2")
    caretaker.add_memento(originator.save_to_memento())

    originator.set_state("Состояние 3")
    caretaker.add_memento(originator.save_to_memento())

    # Восстановление состояния
    originator.restore_from_memento(caretaker.get_memento(0))
    originator.restore_from_memento(caretaker.get_memento(1))
