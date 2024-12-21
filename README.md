# Паттерны объектно-ориентированного проектирования

## Порождающие паттерны

### ABSTRACT FACTORY (Абстрактная фабрика)
* Предоставляет библиотеку объектов, раскрывая только их интерфейсы, но не реализацию
* Изалирует клиента от реализации классов
* Упращает замену продуктов
* Гарантирует совместимость продуктов
* Сложно расширять

### BUILDER (Строитель)
* Предоставляет абстрактный интерфейс для конструирования продукта
* Инкапсулирует способ конструирования и представление сложного объекта

### FACTORY METHOD (Фабричный метод)
* Изолирует клиента от деталей создания объекта
* Обеспечивает гибкость и упрощает добавление новых типов объектов
* Определяет интерфейс для создания объектов, позволяя подклассам изменять тип создаваемых объектов
* Может привести к увеличению числа классов в системе

### PROTOTYPE (Прототип)
* Скрывает от  клиента конкретные классы продуктов
* Добавление и удаление продуктов во время выполнения
* Уменьшение числа подклассов
* Каждый подкласс класса Prototype должен реализовывать операцию Clone

### SINGLETON (Одиночка)
* Контролируемый доступ к единственному экземпляру
* Сокращение пространства имен
* Возможность использования переменного числа экземпляров
