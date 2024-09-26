## Описание
Созданы классы Product и Category .


Для класса Product определены следующие свойства:
- название (name),
- описание (description),
- цена (price),
- количество в наличии (quantity).

Также класс Product имеет свои классы-наследники, которые расширяют или переопределяют его функционал.

Для класса Category определены следующие свойства:
- название (name),
- описание (description),
- список товаров категории (products).

Также для класса Category добавлено два атрибута класса. 
Доступ к этим атрибутам есть у каждого объекта класса, и в них хранится общая информация для всех объектов.
Эти атрибуты хранят в себе количество категорий и количество товаров.
Атрибуты класса заполняются автоматически при инициализации нового объекта.


Написаны тесты, которые проверяют корректность инициализации экземпляров классов и выполнения работы его методов.

Реализована подгрузка данных по категориями и товарам из файла JSON. 
Для этого описаны функции, одна из котрых читает файл, другая создает объекты классов.

Созданы приватные переменные (атрибуты), специальные методы для работы в разных режимах доступа,
добавлены геттеры и сеттеры.

Добавлены магические методы, для более удобного использования магазина,
предоставления пользователям интерфейсов, которые позволяют быстрее работать с товарами и категориями.

Описано строковое и отладочное отображение объектов для более комфортного использования интерфейсов
и получения информации об объектах.

Созданы родительские классы и выделены классы-наследники, чтобы исключить повторение функциональности и
оптимизировать код.
