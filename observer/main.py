class Subject:
    """Абстрактный класс субъекта."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()


class Observer:
    """Абстрактный класс наблюдателя."""

    def update(self):
        raise NotImplementedError("Метод update() должен быть переопределён.")


class ConcreteSubject(Subject):
    """Конкретный субъект с состоянием."""

    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class ConcreteObserverA(Observer):
    """Наблюдатель A."""

    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} получил уведомление!")


class ConcreteObserverB(Observer):
    """Наблюдатель B."""

    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} был оповещён о изменении!")


if __name__ == "__main__":
    # Создаём субъект
    subject = ConcreteSubject()

    # Создаём наблюдателей
    observer1 = ConcreteObserverA("Observer 1")
    observer2 = ConcreteObserverB("Observer 2")

    # Подключаем наблюдателей
    subject.attach(observer1)
    subject.attach(observer2)

    # Изменяем состояние субъекта
    print("Изменение состояния на 'State 1'")
    subject.state = "State 1"

    # Отключаем одного наблюдателя
    subject.detach(observer1)

    # Изменяем состояние субъекта
    print("Изменение состояния на 'State 2'")
    subject.state = "State 2"
