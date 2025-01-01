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

## Структурные паттерны

### ADAPTER (Адаптер)
* Предоставляет интерфейс, ожидаемый клиентом, к объекту, который имеет несовместимый интерфейс
* Повышает повторное использование существующего кода


### BRIDGE (Мост)
* Отделение абстракции от реализации
* Уменьшается количество создаваемых подклассов для расширения
* Абстракция и реализация могут расширяться независимо

### Composite (Компоновщик)
* Позволяет клиенту работать с отдельными объектами и группами объектов единообразно.
* Упрощает добавление новых видов компонентов.
* Может усложнить реализацию, если структура объекта слишком гибкая или изменяемая.

### DECORATOR (Декоратор)
* Позволяет динамически добавлять объекту новую функциональность, не изменяя его структуру
* Предоставляет гибкую альтернативу наследованию для расширения функциональности
* Компоненты могут быть вложены друг в друга для создания сложного поведения

### FACADE (Фасад)
* Клиент взаимодействует только с фасадом, не зная о деталях работы подсистем
* Фасад упрощает интерфейс, но не ограничивает возможность прямого взаимодействия с подсистемами при необходимости


### FLYWEIGHT (Приспособленец)
* Оптимизирует использование памяти при большом количестве однотипных объектов
* Позволяет повторно использовать общие части объектов
* Упрощает управление большим числом объектов, но может усложнить код

### PROXY (Заместитель)
* Позволяет управлять доступом к объекту, добавляя дополнительные функции без изменения объекта
* Может использоваться для реализации контроля доступа, ленивой инициализации, удаленного доступа или логирования
* Упрощает управление тяжелыми или удаленными объектами

## Паттерны поведения

### CHAIN OF RESPONSIBILITY (Чепочка обязанностей)
* Гибкость при распределении обязанностей между объектами
* Нет гарантий, что запрос будет обработан

### COMMAND (Команда)
* Обеспечивает гибкость, позволяя клиентам инициализировать команды без жесткой привязки к их реализации.
* Поддерживает отмену и повтор операций.
* Может усложнить код из-за добавления большого числа классов для каждой команды.

### INTERPRETER (Интерпретатор)
* Простота изменения и расширения
* Простая реализация
* Сложное сопровождение сложных грамматик

### ITERATOR (Итератор)
* Поддержка разных способов обхода агрегата
* Инкапсуляция логики обхода
* Единый интерфейс для всех коллекций
* Упрощение клиентского кода

### MEDIATOR (Посредник)
* Снижение числа пораждаемых подклассов
* Асбтрагирование способа кооперирования объектов
* Централизация управления


### MEMENTO (Хранитель)
* Позволяет сохранить и восстановить состояние объекта
* Инкапсулирует детали состояния, не нарушая инкапсуляции объекта
* Удобен для реализации отката изменений (Undo/Redo)
* Может привести к увеличению использования памяти, если требуется сохранять большое количество состояний
