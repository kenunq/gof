class Handler:
    """Абстрактный базовый класс для всех обработчиков."""
    def __init__(self, successor=None):
        self.successor = successor  # Следующий обработчик в цепочке

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class Button(Handler):
    """Класс кнопки, который может обрабатывать события."""
    def handle_request(self, request):
        if request == "button_click":
            print("Button: Обработан запрос на клик.")
        else:
            super().handle_request(request)


class Panel(Handler):
    """Класс панели, который может обрабатывать события."""
    def handle_request(self, request):
        if request == "panel_action":
            print("Panel: Обработан запрос на действие.")
        else:
            super().handle_request(request)


class Window(Handler):
    """Класс окна, который может обрабатывать события."""
    def handle_request(self, request):
        if request == "window_resize":
            print("Window: Обработан запрос на изменение размера.")
        else:
            super().handle_request(request)


# Создание цепочки обработчиков
window = Window()
panel = Panel(window)
button = Button(panel)

# Генерация запросов
requests = ["button_click", "panel_action", "window_resize", "unknown_request"]

for req in requests:
    print(f"\nОтправка запроса: {req}")
    button.handle_request(req)
