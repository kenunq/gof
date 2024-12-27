from abc import ABC, abstractmethod

# Абстрактный интерфейс изображения
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Реальный класс изображения
class RealImage(Graphic):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Загрузка изображения {self.filename} с диска")

    def draw(self):
        print(f"Отображение изображения {self.filename}")

# Заместитель для изображения
class ImageProxy(Graphic):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def draw(self):
        if not self.real_image:
            print(f"Создание реального изображения для {self.filename}")
            self.real_image = RealImage(self.filename)
        self.real_image.draw()

# Клиентский код
def main():
    print("Создание объекта-заместителя")
    image = ImageProxy("large_photo.jpg")

    print("\nПервый вызов draw:")
    image.draw()  # Загружается изображение, затем отображается

    print("\nВторой вызов draw:")
    image.draw()  # Используется уже загруженное изображение

if __name__ == "__main__":
    main()
