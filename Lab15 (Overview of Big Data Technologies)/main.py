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
