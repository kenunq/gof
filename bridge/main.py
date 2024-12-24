class Shape:
    def __init__(self, renderer):
        self.renderer = renderer  # Ссылка на реализацию (композиция)

    def draw(self):
        raise NotImplementedError("This method should be implemented in subclasses")


class Renderer:
    def render_circle(self, radius):
        raise NotImplementedError("This method should be implemented in subclasses")


class WindowsRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} on Windows")


class LinuxRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} on Linux")


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)


if __name__ == "__main__":
    # Клиент выбирает конкретный рендерер
    windows_renderer = WindowsRenderer()
    linux_renderer = LinuxRenderer()

    # Фигура, использующая рендерер
    circle_on_windows = Circle(windows_renderer, 5)
    circle_on_linux = Circle(linux_renderer, 10)

    # Рисуем фигуры
    circle_on_windows.draw()
    circle_on_linux.draw()
