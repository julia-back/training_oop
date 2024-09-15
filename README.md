## Описание
Созданы классы Product и Category .


Для класса Product определены следующие свойства:
- название (name),
- описание (description),
- цена (price),
- количество в наличии (quantity).

Для класса Category определены следующие свойства:
- название (name),
- описание (description),
- список товаров категории (products).

Также для класса Category добавлено два атрибута класса. 
Доступ к этим атрибутам есть у каждого объекта класса, и в них хранится общая информация для всех объектов.
Эти атрибуты хранят в себе количество категорий и количество товаров.
Атрибуты класса заполняются автоматически при инициализации нового объекта.


Написаны тесты для классов, которые проверяют:
корректность инициализации объектов класса Category ,
корректность инициализации объектов класса Product ,
подсчет количества продуктов,
подсчет количества категорий.


Реализована подгрузка данных по категориями и товарам из файла JSON. 
Для этого описаны функции, одна из котрых читает файл, другая создает объекты классов.