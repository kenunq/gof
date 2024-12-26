# Разделяемое состояние (внутреннее)
class Font:
    def __init__(self, font_name, font_size):
        self.font_name = font_name
        self.font_size = font_size

    def __str__(self):
        return f"{self.font_name}, {self.font_size}px"

# Приспособленец
class FontFactory:
    def __init__(self):
        self._fonts = {}

    def get_font(self, font_name, font_size):
        key = (font_name, font_size)
        if key not in self._fonts:
            self._fonts[key] = Font(font_name, font_size)
        return self._fonts[key]

# Текстовый символ (внешнее состояние)
class TextCharacter:
    def __init__(self, character, font):
        self.character = character
        self.font = font  # Разделяемый объект

    def render(self):
        return f"Character: {self.character}, Font: {self.font}"

# Клиентский код
if __name__ == "__main__":
    factory = FontFactory()

    # Создаем символы с разделяемыми шрифтами
    font1 = factory.get_font("Arial", 12)
    font2 = factory.get_font("Times New Roman", 14)

    char_a = TextCharacter("A", font1)
    char_b = TextCharacter("B", font2)
    char_c = TextCharacter("C", font1)  # Повторно использует font1

    print(char_a.render())
    print(char_b.render())
    print(char_c.render())

    # Проверяем, что объекты шрифта разделяются
    print(f"Font1 and Font3 are the same object: {font1 is char_c.font}")
