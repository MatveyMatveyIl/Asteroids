# Asteroids


Авторы: Ильичев Матвей, Карпова Юлия


# Описание

Данное приложение является реализацией игры "Астероиды".

# Пример запуска:
 
python3 asteroids.py

# Состав

Графическая версия: asteroids.py

Модули: asteroids_game/

Изображения: assets/sprites

Шрифт: assets/font

Звуки: assets/sounds


# Подробности реализации:

- Модули, отвечающие за логику игры, расположены в папке asteroids_game. Игра реализована с помощью библиотеки pygame. Класс Game отвечает за основную логику игры, объединяя классы всех игровых объектов( Asteroid, PlayerShip, Bullet). Все игровые объекты наследуют класс GameObject, который в свою очередь реализует методы: передвижение, коллизии, отрисовки.

- В папке assets расположены все спрайты для игровых объектов, фон меню и игры

- В папке asteroid_game/src расположены дополнительные модули: загрузка музыки, изображения, уровня и сохранение текущего уровня пользователя.

- Класс Menu реализует меню игры с функциями : новая игра(New Game), продолжение игры(Start), выбор уровня (1 -10), выход (Exit)

