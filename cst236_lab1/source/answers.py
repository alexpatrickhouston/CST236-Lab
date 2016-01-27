import time
import getpass


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
    return "I'm sorry I can't do that " + getpass.getuser()+"!"


def clear_memory():

    return "Memory Cleared"


def digit_pi(n):
    return n;


def life():  # Enlighten yourself you pig in human clothing
    return 42;

def convert(value,type1,type2):

    if(type1 =="inches"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="feet"):
        if(type2=="inches"):
            return value*12;
        if(type2=="feet"):
            return value
        elif(type2=="miles"):
            return value/5820
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/3
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="miles"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="cm"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="meters"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="yards"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="mm"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="km"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="hectometer"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value
        elif(type2=="decameter"):
            return value/393.701

    if(type1 =="decameter"):
        if(type2=="inches"):
            return value;
        if(type2=="feet"):
            return value/12
        elif(type2=="miles"):
            return value/63360
        elif(type2=="cm"):
            return value*2.54
        elif(type2=="meters"):
            return value/39.3701
        elif(type2=="yards"):
            return value/36
        elif(type2=="mm"):
            return value*25.4
        elif(type2=="km"):
            return value/39370.1
        elif(type2=="hectometer"):
            return value/3937.01
        elif(type2=="decameter"):
            return value
