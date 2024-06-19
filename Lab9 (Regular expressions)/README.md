Лабораторна робота №9: Regular expressions
___
Мета роботи:
 Метою цієї лабораторної роботи є ознайомлення з основами роботи з регулярними виразами у мові програмування Python. А також вивчення створювати, застосовувати та аналізувати регулярні вирази для вирішення різноманітних задач перевірки та валідації вхідних даних. Зокрема, робота з шаблонами для перевірки таких форматів: рядки, що містять лише малі літери та цифри; наявність великої літери у рядку; коректність IP-адреси версії 4; формат часу у вигляді години:хвилини:секунди;  номери кредитних карток з певними початковими цифрами; номери соціального страхування у заданому форматі і тд. Виконання цих завдань допомагає набути практичних навичок використання модуля re у Python, навчитися будувати ефективні та точні регулярні вирази для різних цілей та зрозуміти, як застосовувати ці вирази для валідації реальних даних.
___
Опис завдання:
```Python
Task1: Write a def(task1) regular expression that matches a string containing only lowercase letters and digits. Input: "hello123" Output: True
Task2: Write a def(task2) regular expression that matches a string containing at least one uppercase letter. Input: "Hello" Output: True
Task3: Write a def(task3) regular expression that matches a string containing a valid IPv4 address. Input: "192.168.1.1" Output: True
Task4: Write a def(task4) regular expression that matches a string containing a valid time in the format of "HH:MM:SS". Input: "12:34:56" Output: True
Task5: Write a def(task5) regular expression that matches a string containing a valid US postal code in the format of "NNNNN" or "NNNNN-NNNN". Input: "12345" or "12345-6789" Output: True
Task6: Write a def(task6) regular expression that matches a string containing a valid username, with the following criteria: only contains lowercase letters, numbers, underscores, and hyphens, and is between 6 and 12 characters long. Input: "john_doe-123" Output: True
Task7: Write a def(task7) regular expression that matches a string containing a valid credit card number (either 15 or 16 digits, starting with either 4, 5, or 6). Input: "4512-3456-7890-1234" Output: True
Task8: Write a def(task8) regular expression that matches a string containing a valid social security number (in the format of ###-##-####). Input: "123-45-6789" Output: True
Task9: Write a def(task9) regular expression that matches a string containing a valid password, with the following criteria: at least one uppercase letter, one lowercase letter, one digit, one special character (@, #, $, or %), and at least 8 characters long. Input: "Passw0rd#" Output: True
Task10: Write a def(task10) regular expression that matches a string containing a valid IPv6 address. Input: "2001:0db8:85a3:0000:0000:8a2e:0370:7334" Output: True.
```
___
Виконання роботи:
```Python
import re


def task1(input_str):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, input_str))



def task2(input_str):
    pattern = r'[A-Z]'
    return bool(re.search(pattern, input_str))



def task3(input_str):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, input_str))



def task4(input_str):
    pattern = r'^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    return bool(re.match(pattern, input_str))



def task5(input_str):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, input_str))



def task6(input_str):
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, input_str))



def task7(input_str):
    pattern = r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    return bool(re.match(pattern, input_str.replace("-", "")))



def task8(input_str):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, input_str))



def task9(input_str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(pattern, input_str))



def task10(input_str):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, input_str))

```
___
Результати:
```Python
True
True
True
True
True
True
True
True
True
True

```
___
Висновки:Виконання даної лабораторної роботи та використані функції дозволили мені краще зрозуміти, як ефективно використовувати регулярні вирази для різних задач валідації даних.
Функції, які я реалізувала, охоплюють широкий спектр перевірок, від простих перевірок на наявність малих літер та цифр у рядку до більш складних перевірок, таких як валідація IP-адрес. Я також навчилася використовувати модуль re у Python для пошуку та відповідності шаблонів у рядках. Особливо корисним було розуміння того, як створювати регулярні вирази для специфічних форматів. Виконання цієї лабораторної дало мені практичні навички, які я зможу застосувати у реальних проектах, де потрібно перевіряти та валідувати різні типи даних
___