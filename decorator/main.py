from abc import ABC, abstractmethod


# Компонент
class VisualComponent(ABC):
    @abstractmethod
    def draw(self):
        pass


# Конкретный компонент
class TextView(VisualComponent):
    def draw(self):
        print("Drawing TextView")


# Декоратор
class Decorator(VisualComponent):
    def __init__(self, component: VisualComponent):
        self._component = component

    def draw(self):
        self._component.draw()


# Декоратор для добавления рамки
class BorderDecorator(Decorator):
    def draw(self):
        self._component.draw()
        self.add_border()

    def add_border(self):
        print("Adding border")


# Декоратор для добавления скроллинга
class ScrollDecorator(Decorator):
    def draw(self):
        self._component.draw()
        self.add_scroll()

    def add_scroll(self):
        print("Adding scroll")


if __name__ == "__main__":
    # Создаем базовый компонент
    text_view = TextView()

    # Оборачиваем его в декораторы
    bordered_text_view = BorderDecorator(text_view)
    scrollable_bordered_text_view = ScrollDecorator(bordered_text_view)

    # Вызываем метод draw
    print("Base TextView:")
    text_view.draw()

    print("\nTextView with Border:")
    bordered_text_view.draw()

    print("\nTextView with Border and Scroll:")
    scrollable_bordered_text_view.draw()
