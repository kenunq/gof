class State:
    """Абстрактное состояние."""
    def insert_coin(self):
        raise NotImplementedError()

    def eject_coin(self):
        raise NotImplementedError()

    def press_button(self):
        raise NotImplementedError()

    def dispense(self):
        raise NotImplementedError()


class NoCoinState(State):
    """Состояние: монета не вставлена."""
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Монета вставлена.")
        self.machine.set_state(self.machine.has_coin_state)

    def eject_coin(self):
        print("Монета не вставлена. Нечего вернуть.")

    def press_button(self):
        print("Нельзя выбрать напиток без монеты.")

    def dispense(self):
        print("Сначала нужно вставить монету.")


class HasCoinState(State):
    """Состояние: монета вставлена."""
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Монета уже вставлена.")

    def eject_coin(self):
        print("Монета возвращена.")
        self.machine.set_state(self.machine.no_coin_state)

    def press_button(self):
        print("Напиток выбран.")
        self.machine.set_state(self.machine.sold_state)

    def dispense(self):
        print("Сначала нужно выбрать напиток.")


class SoldState(State):
    """Состояние: напиток продан."""
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Подождите, напиток уже выдаётся.")

    def eject_coin(self):
        print("Нельзя вернуть монету после выбора напитка.")

    def press_button(self):
        print("Напиток уже выбран.")

    def dispense(self):
        print("Напиток выдан.")
        self.machine.set_state(self.machine.no_coin_state)


class VendingMachine:
    """Автомат по продаже напитков."""
    def __init__(self):
        self.no_coin_state = NoCoinState(self)
        self.has_coin_state = HasCoinState(self)
        self.sold_state = SoldState(self)
        self.state = self.no_coin_state

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def press_button(self):
        self.state.press_button()
        self.state.dispense()

    def dispense(self):
        self.state.dispense()


# Использование
if __name__ == "__main__":
    machine = VendingMachine()

    # Попробуем выбрать напиток без монеты
    machine.press_button()

    # Вставляем монету
    machine.insert_coin()

    # Выбираем напиток
    machine.press_button()

    # Попробуем вернуть монету после покупки
    machine.eject_coin()
