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




def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def my_function(x, y):
    return x + y

result = my_function(2, 4)
print(result)




def sort_by_age():
    age = [12, 16, 20, 22, 27, 34]
    age.sort()  
    print(age)  
sort_by_age()



def merge_dicts():
    dict1= {1, 2, 3, 4}
    dict2 = {"a", "b", "c", "d"}

    dict1.update(dict2)
    print(dict1)
merge_dicts()



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

my_car = Car("Toyota", "supra", 2022)
my_car.display_info()

  