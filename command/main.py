class Command:
    """Абстрактный класс команды."""

    def execute(self):
        raise NotImplementedError("Метод execute() должен быть переопределён.")

    def undo(self):
        """Метод отмены действия команды."""
        raise NotImplementedError("Метод undo() должен быть переопределён.")


class CopyCommand(Command):
    """Команда копирования."""

    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.clipboard = self.editor.selected_text
        print(f"Текст '{self.editor.selected_text}' скопирован в буфер обмена.")

    def undo(self):
        print("Команда копирования не требует отмены.")


class PasteCommand(Command):
    """Команда вставки."""

    def __init__(self, editor):
        self.editor = editor
        self.previous_text = ""

    def execute(self):
        self.previous_text = self.editor.text
        self.editor.insert_text(self.editor.clipboard)
        print(f"Текст '{self.editor.clipboard}' вставлен.")

    def undo(self):
        self.editor.text = self.previous_text
        print(f"Вставка отменена. Текущий текст: '{self.editor.text}'")


class Editor:
    """Текстовый редактор."""

    def __init__(self):
        self.clipboard = ""
        self.text = ""
        self.selected_text = ""

    def select_text(self, text):
        self.selected_text = text
        print(f"Выбран текст: '{text}'")

    def insert_text(self, text):
        self.text += text
        print(f"Текущий текст в редакторе: '{self.text}'")


class CommandInvoker:
    """Класс для хранения и выполнения команд."""

    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            print("Последняя команда отменена.")
        else:
            print("Нет команд для отмены.")


if __name__ == "__main__":
    editor = Editor()
    editor.select_text("Hello, world!")

    copy_command = CopyCommand(editor)
    paste_command = PasteCommand(editor)

    invoker = CommandInvoker()

    invoker.execute_command(copy_command)

    invoker.execute_command(paste_command)

    invoker.undo_last_command()

    invoker.execute_command(paste_command)
