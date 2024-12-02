# Генератор случайных паролей

Этот проект создает простой генератор случайных паролей с возможностью хеширования пароля с использованием алгоритма SHA-256. Пользователь может указать длину пароля и выбрать, какие символы использовать (буквы, цифры, специальные символы). После генерации пароля, пользователь может выбрать, хочет ли он хешировать пароль.

## Функционал

* Генерация пароля заданной длины.
* Выбор используемых символов:
    * Только буквы (строчные и прописные).
    * Буквы и цифры.
    * Буквы, цифры и специальные символы.
* Хеширование пароля с использованием алгоритма SHA-256.
  
## Использование

Пример использования генератора:

* Шаг 1. Ввод параметров пароля
Скрипт попросит вас ввести параметры для генерации пароля:

Длина пароля:

Введите длину пароля: 12
В данном примере мы вводим длину пароля равную 12 символам.

Использование цифр:

Использовать цифры? (y/n): y
Мы выбираем использовать цифры в пароле.

Использование специальных символов:

Использовать специальные символы? (y/n): y
Мы также выбираем использовать специальные символы в пароле.

* Шаг 2. Генерация пароля
После ввода параметров, скрипт сгенерирует пароль и выведет его на экран:

Сгенерированный пароль: A1b2C3d4!@#$

* Шаг 3. Хеширование пароля
Далее скрипт спросит, хотите ли вы хешировать пароль:

Хотите хешировать пароль? (y/n): y
Мы выбираем хешировать пароль.

* Шаг 4. Вывод хешированного пароля
Скрипт выведет хешированный пароль:

Хешированный пароль: 5e884898da28047151d0e56f8dc6292773603d0d6aabbddc7254aa1f218c923a

## Полный пример вывода

Введите длину пароля: 12

Использовать цифры? (y/n): y

Использовать специальные символы? (y/n): y

Сгенерированный пароль: A1b2C3d4!@#$

Хотите хешировать пароль? (y/n): y

Хешированный пароль: 5e884898da28047151d0e56f8dc6292773603d0d6aabbddc7254aa1f218c923a
