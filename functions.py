# functions.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # Intentional bug to fix later

def multiply(a, b):
    return a * b

#def convert_fahrenheit_to_celsius(fahrenheit):
#    return multiply(subtract(fahrenheit, 32), 9 / 5)

def convert_fahrenheit_to_celsius(fahrenheit):
    return multiply(subtract(fahrenheit, 32), 5 / 9)  # Ensure the function is correct
