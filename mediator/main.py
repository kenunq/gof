class Mediator:
    """Абстрактный класс посредника."""

    def notify(self, sender, event):
        raise NotImplementedError("Метод notify() должен быть переопределён.")


class DialogMediator(Mediator):
    """Конкретный посредник для диалога."""

    def __init__(self):
        self.button = None
        self.checkbox = None
        self.textbox = None

    def notify(self, sender, event):
        if sender == self.checkbox and event == "checked":
            print("Флажок отмечен. Делаем кнопку активной.")
            self.button.enable()
        elif sender == self.checkbox and event == "unchecked":
            print("Флажок снят. Делаем кнопку неактивной.")
            self.button.disable()
        elif sender == self.textbox and event == "text_changed":
            print("Текст изменён. Проверяем длину текста.")
            if len(self.textbox.get_text()) > 0:
                self.button.enable()
            else:
                self.button.disable()


class Component:
    """Базовый компонент, взаимодействующий с посредником."""

    def __init__(self, mediator=None):
        self.mediator = mediator

    def set_mediator(self, mediator):
        self.mediator = mediator


class Button(Component):
    def enable(self):
        print("Кнопка активирована.")

    def disable(self):
        print("Кнопка деактивирована.")


class Checkbox(Component):
    def check(self):
        print("Флажок отмечен.")
        if self.mediator:
            self.mediator.notify(self, "checked")

    def uncheck(self):
        print("Флажок снят.")
        if self.mediator:
            self.mediator.notify(self, "unchecked")


class TextBox(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"Текст в поле: '{text}'")
        if self.mediator:
            self.mediator.notify(self, "text_changed")

    def get_text(self):
        return self.text


if __name__ == "__main__":
    mediator = DialogMediator()

    button = Button(mediator)
    checkbox = Checkbox(mediator)
    textbox = TextBox(mediator)

    mediator.button = button
    mediator.checkbox = checkbox
    mediator.textbox = textbox

    # Взаимодействие через посредника
    checkbox.check()
    textbox.set_text("Hello")
    textbox.set_text("")
    checkbox.uncheck()
