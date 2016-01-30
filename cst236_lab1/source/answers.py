import time
import getpass
import math

conversion = {'feet,feet': 1, 'feet,mile': 1 / 5280, 'feet,yard': 1 / 3, 'feet,meter': 3.28084, 'mile,mile': 1,
              'mile,feet': 5280 / 1, 'mile,yard': 1760, 'mile:meter': 1609.34, 'yard,yard': 1, 'yard,feet': 3,
              'yard,mile': 1 / 1760, 'yard,meter': 1 / 1.09361, 'meter,meter': 1, 'meter,feet': 3.28084,
              'meter,mile': 1 / 1609.34, 'meter,yard': 1.09361
              }


def what_time():  # when the user asks "What time is it?" main will call this function and return the time
    return time.strftime("%H:%M")


def fibonacci(n):  # when the user asks for a digit of the fibonacci sequence this calculates and returns that value
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def open_door():  # I'm sorry I can't do that
    return "I'm afraid I cant do that" + getpass.getuser() + "!"


def clear_memory():
    return "Memory Cleared"


def digit_pi(n):
    pi_value = math.pi
    pi_value *= 10 ^ n
    pi_value %= 10
    return n;


def life():  # Enlighten yourself you pig in human clothing
    return 42;


def convert(value, type1, type2):
    value *= conversion[type1 + ',' + type2]
    return value;
