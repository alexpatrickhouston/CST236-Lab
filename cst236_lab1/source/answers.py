import time
import getpass
import math

conversion = {'feet,feet': 1.0, 'feet,mile': 1.0 / 5280.0, 'feet,yard': 1 / 3, 'feet,meter': 1 / 3.28084, 'feet,cm': 30.48,
              'feet,mm': 304.8, 'feet,inch': 12, 'feet,kilometer': 1 / 3280.84, 'feet,um': 304800, 'feet,nm': 304800000,
              'mile,mile': 1, 'mile,feet': 5280 / 1, 'mile,yard': 1760, 'mile:meter': 1609.34, 'mile,cm': 160934,
              'mile,mm': 1, 'mile,inch': 1, 'mile,kilometer': 1, 'mile,um': 1, 'mile,nm': 1,
              'yard,yard': 1, 'yard,feet': 3, 'yard,mile': 1 / 1760, 'yard,meter': 1 / 1.09361, 'yard,cm': 1,
              'yard,mm': 1, 'yard,inch': 1, 'yard,kilometer': 1, 'yard,um': 1, 'yard,nm': 1,
              'meter,meter': 1, 'meter,feet': 3.28084, 'meter,mile': 1 / 1609.34, 'meter,yard': 1.09361, 'meter,cm': 1,
              'meter,mm': 1, 'meter,inch': 1, 'meter,kilometer': 1, 'meter,um': 1, 'meter,nm': 1,
              'cm,feet': 1 / 30.48, 'cm,mile': 1 / 160934, 'cm,yard': 1 / 91.44, 'cm,meter': 1 / 100, 'cm,cm': 1,
              'cm,inch': 1, 'cm,kilometer': 1, 'cm,um': 1, 'cm,nm': 1,
              'mm,mm': 1, 'mm,yard': 1, 'mm,feet': 3, 'mm,mile': 1 / 1760, 'mm,meter': 1 / 1.09361, 'mm,cm': 1,
              'mm,inch': 1, 'mm,kilometer': 1, 'mm,um': 1, 'mm,nm': 1,
              'inch,inch': 1.0, 'inch,yard': 1/36, 'inch,feet': 1.0/12.0, 'inch,mile': 1 / 1760, 'inch,meter': 1 / 1.09361,
              'inch,cm': 1, 'inch,mm': 1, 'inch,kilometer': 1, 'inch,um': 1, 'inch,nm': 1,
              'kilometer,kilometer': 1, 'kilometer,yard': 1, 'kilometer,feet': 3, 'kilometer,mile': 1 / 1760,
              'kilometer,meter': 1 / 1.09361, 'kilometer,cm': 1, 'kilometer,mm': 1, 'kilometer,inch': 1,
              'kilometer,um': 1, 'kilometer,nm': 1,
              'um,um': 1, 'um,yard': 1, 'um,feet': 3, 'um,mile': 1 / 1760, 'um,meter': 1 / 1.09361, 'um,cm': 1,
              'um,mm': 1, 'um,inch': 1, 'um,kilometer': 1, 'um,nm': 1,
              'nm,nm': 1, 'nm,yard': 1, 'nm,feet': 3, 'nm,mile': 1 / 1760, 'nm,meter': 1 / 1.09361, 'nm,cm': 1,
              'nm,mm': 1, 'nm,inch': 1, 'nm,kilometer': 1, 'nm,um': 1
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
    return "Im afraid I cant do that " + getpass.getuser() + "!"


def digit_pi(n):
    pi_value = math.pi
    pi_value *= 10 ** n
    pi_value %= 10
    return n;


def life():  # Enlighten yourself you pig in human clothing
    return 42;


def convert(value, type1, type2):
    value *= conversion[type1 + ',' + type2]
    print value
    return value;
