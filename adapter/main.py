from abc import ABC, abstractmethod


class TextView:
    def __init__(self, text: str):
        self.text = text

    def get_extent(self):
        """Возвращает ширину и высоту текста."""
        return (len(self.text) * 7, 20)  # Условные размеры текста

    def display(self):
        print(f"Displaying text: {self.text}")


class Shape(ABC):
    @abstractmethod
    def bounding_box(self):
        """Возвращает ограничивающий прямоугольник."""
        pass

    @abstractmethod
    def draw(self):
        """Рисует объект на экране."""
        pass


class TextShapeAdapter(Shape):
    def __init__(self, text_view: TextView):
        self.text_view = text_view

    def bounding_box(self):
        """Адаптируем метод get_extent() для интерфейса bounding_box()."""
        width, height = self.text_view.get_extent()
        return (0, 0, width, height)  # Левая верхняя точка (0,0), ширина, высота

    def draw(self):
        """Адаптируем метод display() для интерфейса draw()."""
        self.text_view.display()


def render_shape(shape: Shape):
    bbox = shape.bounding_box()
    print(f"Rendering shape with bounding box: {bbox}")
    shape.draw()


# Используем TextView через адаптер
text_view = TextView("Hello, Adapter!")
text_shape = TextShapeAdapter(text_view)

# Клиентский код ожидает интерфейс Shape
render_shape(text_shape)
