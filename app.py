def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(2, 4))


def is_even(number):
    return number % 2 == 0
print(is_even(3))


def reverse_string(text):
  return text[::-1]
text = reverse_string("Welcome to phase 3")
print(text)


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = input("Enter a text: ")
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    
    return count
print(count_vowels(text))


def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
n = 1
print(calculate_factorial(n))


