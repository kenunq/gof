class Context:
    """Контекст, содержащий информацию для интерпретации."""
    def __init__(self):
        self.variables = {}

    def assign(self, variable, value):
        """Назначить значение переменной."""
        self.variables[variable] = value

    def lookup(self, variable):
        """Получить значение переменной."""
        return self.variables.get(variable, 0)


class AbstractExpression:
    """Абстрактный класс выражения."""
    def interpret(self, context):
        raise NotImplementedError("Метод interpret() должен быть переопределён.")


class NumberExpression(AbstractExpression):
    """Числовое выражение."""
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number


class VariableExpression(AbstractExpression):
    """Переменное выражение."""
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.lookup(self.name)


class AddExpression(AbstractExpression):
    """Выражение сложения."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class SubtractExpression(AbstractExpression):
    """Выражение вычитания."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


if __name__ == "__main__":
    context = Context()
    context.assign("x", 10)
    context.assign("y", 20)

    # Выражение: x + y - 5
    expression = SubtractExpression(
        AddExpression(
            VariableExpression("x"),
            VariableExpression("y")
        ),
        NumberExpression(5)
    )

    result = expression.interpret(context)
    print(f"Результат интерпретации: {result}")
