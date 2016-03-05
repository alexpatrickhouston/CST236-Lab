"""Holds the question functions and the methods for answering them"""
import time
import getpass
import math
import platform
import random
#pylint: disable=too-many-return-statements, too-many-branches
CONVERSION = {'feet,feet': 1.0, 'feet,mile': 1.0 / 5280.0, 'feet,yard': 1.0 / 3.0,
              'feet,meter': 1.0 / 3.28084,
              'feet,cm': 30.48,
              'feet,mm': 304.8, 'feet,inch': 12.0,
              'feet,kilometer': 1.0 / 3280.84, 'feet,um': 304800.0,
              'feet,nm': 304800000.0,
              'mile,mile': 1.0, 'mile,feet': 5280.0,
              'mile,yard': 1760.0, 'mile:meter': 1609.34, 'mile,cm': 160934.0,
              'mile,mm': 1609000000.0, 'mile,inch': 63360.0,
              'mile,kilometer': 1.60934, 'mile,um': 1609000000.0,
              'mile,nm': 1609000000000.0,
              'yard,yard': 1.0, 'yard,feet': 3.0,
              'yard,mile': 1.0 / 1760.0, 'yard,meter': 1.0 / 1.09361,
              'yard,cm': 91.44,
              'yard,mm': 914.4, 'yard,inch': 36.0,
              'yard,kilometer': 1.0 / 1093.61, 'yard,um': 914400.0,
              'yard,nm': 914400000.0,
              'meter,meter': 1.0, 'meter,feet': 3.28084,
              'meter,mile': 1 / 1609.34, 'meter,yard': 1.09361,
              'meter,cm': 100.0,
              'meter,mm': 1000.0, 'meter,inch': 39.3701,
              'meter,kilometer': 0.001, 'meter,um': 1000000.0,
              'meter,nm': 1000000000.0,
              'cm,feet': 1 / 30.48, 'cm,mile': 1.0 / 160934.0,
              'cm,yard': 1.0 / 91.44, 'cm,meter': 1.0 / 100.0,
              'cm,cm': 1.0,
              'cm,inch': .393701, 'cm,kilometer': 0.00001,
              'cm,um': 10000.0, 'cm,nm': 10000000.0,
              'mm,mm': 1.0, 'mm,yard': 1.0 / 914.4, 'mm,feet': 1.0 / 304.8,
              'mm,mile': 1.0 / 1609000.0,
              'mm,meter': 1.0 / 1000.0, 'mm,cm': 1.0 / 10.0,
              'mm,inch': 1.0 / 25.4, 'mm,kilometer': 0.000001, 'mm,um': 1000.0,
              'mm,nm': 1000000.0,
              'inch,inch': 1.0, 'inch,yard': 1.0 / 36.0, 'inch,feet': 1.0 / 12.0,
              'inch,mile': 1.0 / 63360.0,
              'inch,meter': 1.0 / 39.3701,
              'inch,cm': 2.54, 'inch,mm': 25.4, 'inch,kilometer': 1.0 / 39370.1, 'inch,um': 25400.0,
              'inch,nm': 25400000.0,
              'kilometer,kilometer': 1.0, 'kilometer,yard': 1093.61, 'kilometer,feet': 3280.84,
              'kilometer,mile': 1.0 / 1.60934,
              'kilometer,meter': 1000.0, 'kilometer,cm': 100000.0, 'kilometer,mm': 1000000.0,
              'kilometer,inch': 39370.1,
              'kilometer,um': 1000000000.0, 'kilometer,nm': 1000000000000.0,
              'um,um': 1, 'um,yard': 1.0 / 914.4, 'um,feet': 1.0 / 304.8,
              'um,mile': 1.0 / 1609000000.0,
              'um,meter': 1.0 / 1000000.0, 'um,cm': 1.0 / 10000.0,
              'um,mm': 1.0 / 1000.0, 'um,inch': 1.0 / 25400.0, 'um,kilometer': 1.0 / 1000000000.0,
              'um,nm': 1000.0,
              'nm,nm': 1, 'nm,yard': 1.0 / 914400.0, 'nm,feet': 1.0 / 304000.8,
              'nm,mile': 1.0 / 1609000000000.0,
              'nm,meter': 1.0 / 1000000000.0, 'nm,cm': 1.0 / 10000000.0,
              'nm,mm': 1.0 / 1000000.0, 'nm,inch': 1.0 / 25400000.0,
              'nm,kilometer': 1.0 / 1000000000.0,
              'nm,um': 1.0 / 1000.0}


def what_time():
    """when the user asks "What time is it?" main will call this function and return the time"""
    return time.strftime("%H:%M")


def fibonacci(n_digit):
    """ when the user asks for a digit of the fibonacci sequence this
    calculates and returns that value"""
    if n_digit == 0:
        return 0
    elif n_digit == 1:
        return 1
    else:
        return fibonacci(n_digit - 1) + fibonacci(n_digit - 2)


def open_door():
    """I'm sorry I can't do that"""
    return "Im afraid I cant do that " + getpass.getuser() + "!"


def digit_pi(n_digit):
    """Gives you the n digit of pi"""
    pi_value = math.pi
    pi_value *= 10 ** n_digit
    pi_value %= 10
    return n_digit


def convert(value, type1, type2):
    """Converts 1 thing to another thing"""
    value *= CONVERSION[type1 + ',' + type2]
    print value
    return value


def life():
    """Enlighten yourself you pig in human clothing"""
    return 42


def square_root(n_digit):
    """Gives you the square root of a number"""
    return math.sqrt(n_digit)


def love():
    """Tells you what love is"""
    return "Baby Don't hurt me!!"


def add(value1, value2):
    """Adds 2 values"""
    return value1 + value2


def subtract(value1, value2):
    """Subtracts 2 values"""
    return value1 - value2


def multiply(value1, value2):
    """Multiplies 2 values"""
    return value1 * value2


def divide(value1, value2):
    """divides 2 values"""
    return value1 / value2


def computer_name():
    """tells you your computer's name"""
    return "The name of this computer is " + platform.node()


def star_sign(month, day):
    """Calculates your birth sign"""
    if month == "January":
        if day <= 19:
            return 'You are a Capricorn'
        elif 20 <= day <= 31:
            return "You are a Aquarius"
        else:
            return "Not Valid date"

    elif month == "February":
        if day <= 18:
            return 'You are a Aquarius'
        elif 19 <= day <= 29:
            return "You are a Pisces"
        else:
            return "Not Valid date"

    elif month == "March":
        if day <= 20:
            return 'You are a Pisces'
        elif 21 <= day <= 31:
            return "You are a Aries"
        else:
            return "Not Valid date"

    elif month == "April":
        if day <= 19:
            return 'You are a Aries'
        elif 20 <= day <= 30:
            return "You are a Taurus"
        else:
            return "Not Valid date"

    elif month == "May":
        if day <= 20:
            return 'You are a Taurus'
        elif 21 <= day <= 31:
            return "You are a Gemini"
        else:
            return "Not Valid date"

    elif month == "June":
        if day <= 21:
            return 'You are a Gemini'
        elif 22 <= day <= 30:
            return "You are a Cancer"
        else:
            return "Not Valid date"

    elif month == "July":
        if day <= 22:
            return 'You are a Cancer'
        elif 23 <= day <= 31:
            return "You are a Leo"
        else:
            return "Not Valid date"

    elif month == "August":
        if day <= 22:
            return 'You are a Leo'
        elif 23 <= day <= 31:
            return "You are a Virgo"
        else:
            return "Not Valid date"

    elif month == "September":
        if day <= 22:
            return 'You are a Virgo'
        elif 23 <= day <= 30:
            return "You are a Libra"
        else:
            return "Not Valid date"

    elif month == "October":
        if day <= 23:
            return 'You are a Libra'
        elif 24 <= day <= 31:
            return "You are a Scorpio"
        else:
            return "Not Valid date"

    elif month == "November":
        if day <= 21:
            return 'You are a Scorpio'
        elif 22 <= day <= 30:
            return "You are a Sagittarius"
        else:
            return "Not Valid date"

    elif month == "December":
        if day <= 21:
            return 'You are a Sagittarius'
        elif 22 <= day <= 31:
            return "You are a Capricorn"
        else:
            return "Not Valid date"
    else:
        return "Please Enter a valid month"


def lucky_number():
    """Are you feeling lucky, punk?"""
    lucky = random.randrange(1, 20, 1)
    return lucky
