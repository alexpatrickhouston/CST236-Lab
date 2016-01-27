from unittest import TestCase  # imports testing tools
import time
import getpass
from plugins.ReqTracer import story  # imports the requirements checker
from source.main import Interface

test = Interface();


class testAnswers(TestCase):
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_What_Time_is_it(self):
        result = test.ask(question="What time is it?")
        self.assertEqual(result, time.strftime("%H:%M"))

    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I dont have to figure it out myself')
    def test_fibonacci(self):
        result = test.ask(question="What is the 7 digit of fibonacci")
        self.assertEqual(result, '13')

    @story('When I ask "What is the n digit of pi" I want to receive the answer so I dont have to figure it out myself')
    def test_pi(self):
        result = test.ask(question="What is the 6 digit of pi?")
        self.assertEqual(result, "7")

    @story(
            'When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')
    def test_clear_memory(self):
        result = test.ask(question="Please clear memory")
        self.assertEqual(result, "Memory cleared")

    @story(
            'When I say "Open the door hal", I want the application to say "Im afraid I cant do that <user name> so I know that is not an option')
    def test_open_door(self):
        result = test.ask(question="Open the door hal!")
        self.assertEqual(result, "Im afraid I cant do that " + getpass.getuser())

    @story(
            'When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer.')
    def test_convert(self):
        result = test.ask(question="Convert 1 foot to inches")
        self.assertEqual(result, 12)

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type1(self):
        result = test.ask(question="Convert 12 inches to feet")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type2(self):
        result = test.ask(question="Convert 1 mile to feet")
        self.assertEqual(result, 5280)

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type3(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type4(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type5(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type6(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type7(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type8(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type9(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask for a numberic conversion I want at least 10 different units I can convert from/to')
    def test_type10(self):
        result = test.ask(question="What is the " + n + " digit of pi?")
        self.assertEqual(result, "7")

    @story('When I ask "What is the meaning of life?" I want the application to say "42" so that I may be enlightened')
    def test_life(self):
        result = test.ask(question="What is the meaning of life")
        self.assertEqual(result, 42)
