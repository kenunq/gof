from abc import ABC, abstractmethod


# Компонент
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass


# Лист
class Line(Graphic):
    def draw(self):
        print("Drawing a Line")


class Text(Graphic):
    def draw(self):
        print("Drawing a Text")


# Контейнер (Composite)
class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def draw(self):
        print("Drawing a Picture with:")
        for child in self.children:
            child.draw()


if __name__ == "__main__":
    # Создаем листовые элементы
    line1 = Line()
    line2 = Line()
    text1 = Text()
    text2 = Text()

    # Создаем первую композицию
    picture1 = Picture("Picture 1")
    picture1.add(line1)
    picture1.add(text1)

    # Создаем вторую композицию
    picture2 = Picture("Picture 2")
    picture2.add(line2)
    picture2.add(text2)

    # Вложенная композиция
    big_picture = Picture("Big Picture")
    big_picture.add(picture1)
    big_picture.add(picture2)

    # Добавляем еще один лист в большую композицию
    big_picture.add(Line())

    # Рисуем все элементы
    big_picture.draw()
