Лабораторна робота №15: Overview of Big Data Technologies
___
Мета роботи:
Метою даної лабораторної роботи є закріплення навичок роботи з функціями обробки даних у Python, таких як використання функцій map(), filter(), та регулярних виразів для очищення, нормалізації, фільтрації та маніпуляції рядками і числовими даними, що сприяє підвищенню ефективності і продуктивності обробки інформації.
___
Опис завдання:
```Python
Task 1: Clean Data
Write a function clean_data() that takes a long string of data points separated
by commas, and uses map() to return a list of data points where each is stripped
of whitespace and converted to lowercase.
Example of function usage:data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned) # ['apple', 'banana', 'orange']
Task 2: Filter Emails
Create a function filter_emails() that takes a long string containing emails,
and uses filter() to return a list containing only valid email addresses. An
email is valid if it contains exactly one '@' symbol.
Example of function usage:emails = "mail us test@example.com and invalid-email.com.djwd
with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails) # ['test@example.com', 'example@test.co']
Task 3: Extract Keywords
Write a function extract_keywords() that takes a long string of words, and uses
filter() to return a list containing words that are longer than a specified length.
Example of function usage:words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words) # ['apple', 'banana']
Task 4: Process Text Data
Write a function process_text() that takes a long string of text data, uses
map() to strip whitespace, remove special characters, and convert to lowercase,
then uses filter() to return a list excluding any empty or very short entries.
Example of function usage:texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts) # ['hello', 'yes', 'no']
Task 5: Normalize Data
Write a function normalize_data() that takes a long string of numeric values
separated by commas and normalizes them to a range between 0 and 1 based on
the maximum value.
Example of function usage:numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers) # [0.333, 0.667, 1.0]
Task 6: Concatenate Strings
Develop a function concatenate_strings() that takes multiple strings separated
by a special character and concatenates them into a single string without the
separator.
Example of function usage:data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated) # 'helloworldagain'
Task 7: Sum Numeric Strings
Create a function sum_numeric_strings() that takes a string containing
numbers separated by commas and calculates their total sum.
Example of function usage:numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum) # 10
Task 8: Filter Numbers
Write a function filter_numbers() that filters out numbers from a string that are
above a specified threshold.
Example of function usage:numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered) # [30, 40]
Task 9: Map to Squares
Create a function map_to_squares() that takes a string of numbers, converts
them to their squares, and returns them as a list.
Example of function usage:numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers) # [1, 4, 9, 16]
Task 10: Reverse Strings
Develop a function reverse_strings() that takes a string of words separated by
commas and reverses each word.
Example of function usage:words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words) # ['elppa', 'ananab', 'torrac']

```
___
Виконання роботи:
```Python
import re

def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned = [item.strip().lower() for item in data]
    return cleaned



def filter_emails(emails_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    valid_emails = re.findall(pattern, emails_string)
    valid_emails_list = [email for email in valid_emails if email.count('@') == 1]
    return valid_emails_list



def extract_keywords(words, length):
    filtered_words = [word for word in words.split() if len(word) > length]
    return filtered_words



def process_text(text):
    processed = [re.sub(r'[^\w\s]', '', item.strip().lower()) for item in text.split(',')]
    processed = [item for item in processed if item]
    return processed



def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_value = max(numbers_list)
    normalized = [round(num / max_value, 3) for num in numbers_list]
    return normalized



def concatenate_strings(data, separator):
    concatenated = ''.join(data.split(separator))
    return concatenated



def sum_numeric_strings(numbers):
    total_sum = sum(map(int, re.findall(r'\d+', numbers)))
    return total_sum



def filter_numbers(input_string, threshold):
    numbers_list = [int(num) for num in re.findall(r'\d+', input_string)]
    filtered_numbers = [num for num in numbers_list if num > threshold]
    return filtered_numbers



def map_to_squares(numbers):
    squared_numbers = [int(num) ** 2 for num in numbers.split(',')]
    return squared_numbers



def reverse_strings(words):
    reversed_words = [word[::-1] for word in words.split(',')]
    return reversed_words



# Test the functions
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)

texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)

numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)

data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)

numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)

numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)

numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)

strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
 
#Приклади виклику функцій з очікуваним виводом
print(clean_data(" Hello, World , Python , Programming ")) 
print(filter_emails("user@example.com, invalid-email@, another.user@domain.com"))
print(extract_keywords("Python is a great programming language", 4)) 
print(process_text("Hello, World!, Python; Programming.")) 
print(normalize_data("10, 20, 30, 40")) 
print(concatenate_strings("apple-orange-banana", "-")) 
print(sum_numeric_strings("12 apples and 23 oranges")) 
print(filter_numbers("The numbers are 10, 25, 30, 45", 20)) 
print(map_to_squares("1, 2, 3, 4, 5")) 
print(reverse_strings("apple,orange,banana")) 

```
___
Результати:
```Python
['hello', 'world', 'python', 'programming']
['user@example.com', 'another.user@domain.com']
['Python', 'great', 'programming', 'language']
['hello', 'world', 'python programming']
[0.25, 0.5, 0.75, 1.0]
appleorangebanana
35
[25, 30, 45]
[1, 4, 9, 16, 25]
['elppa', 'egnaro', 'ananab']


```
___
Висновки:Виконуючи дану лабораторну роботу, я закріпила свої навички роботи з функціями map(), filter() та регулярними виразами в Python для обробки та маніпуляції даними. Я навчилася ефективно очищати дані, нормалізувати числові значення, фільтрувати валідні електронні адреси, виділяти ключові слова та виконувати інші операції, що дозволяє значно покращити продуктивність обробки інформації та розвинути більш глибоке розуміння роботи з даними у Python.