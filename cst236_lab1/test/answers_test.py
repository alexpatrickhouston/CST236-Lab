"""Blarg tests and answers and things"""
#pylint:disable= invalid-name
import platform
import time
import getpass
from unittest import TestCase  # imports testing tools
from test.plugins.ReqTracer import story  # imports the requirements checker
from source.main import Interface


TEST = Interface()


class Test_Answers(TestCase):
    """Tests all the answers in answer.py"""
    @story('When I ask "What time is it?" I want to be given the current date/time '
           'so I can stay up to date')
    def test_What_Time_is_it(self):
        """Test for current time"""
        result = TEST.ask(question="What time is it?")
        self.assertEqual(result, time.strftime("%H:%M"))

    @story('When I ask "What is the n digit of fibonacci" I want to '
           'receive the answer so I dont have to figure it out myself')
    def test_fibonacci(self):
        """test the nth digit of fibonacci"""
        result = TEST.ask(question="What is the 7 digit of fibonacci?")
        self.assertEqual(result, 13)

    @story('When I ask "What is the n digit of pi" I want to receive the '
           'answer so I dont have to figure it out myself')
    def test_pi(self):
        """Tests the nth digit of pi"""
        result = TEST.ask(question="What is the 6 digit of pi?")
        self.assertEqual(result, 6.0)

    @story('When I ask "Please clear memory" I was the application to '
           'clear user set questions and answers so I can reset the application')
    def test_clear_memory(self):
        """Tests the clear memory function"""
        result = TEST.ask(question="Please clear memory!")
        self.assertEqual(result, "Memory cleared")

    @story('When I say "Open the door hal", I want the application to say '
           '"Im afraid I cant do that <user name> so I know that is not an option')
    def test_open_door(self):
        """Tests opening the door"""
        result = TEST.ask(question="Open the door hal!")
        self.assertEqual(result, "Im afraid I cant do that " + getpass.getuser() + '!')

    @story('When I ask "What is my lucky number?", I want the application '
           'to give me a random number 1-10, to fuel my gambling addiction')
    def test_lucky_number(self):
        """tests the lucky number"""
        result = TEST.ask(question="What is my lucky number?")
        self.assertLessEqual(result, 20)
    @story('When I ask "What is <number> plus <number>?", I want the '
           'application to give me the answer so I dont have to think')
    def test_add(self):
        """tests the add function"""
        result = TEST.ask(question="What is 2 plus 2?")
        self.assertEqual(result, 4)

    @story('When I ask "What is <number> minus <number>?", I want the'
           ' application to give me the answer so I dont have to think')
    def test_minus(self):
        """tests the minus function"""
        result = TEST.ask(question="What is 2 minus 2?")
        self.assertEqual(result, 0)

    @story('When I ask "What is <number> divided by <number>?", '
           'I want the application to give me the answer so I dont have to think')
    def test_division(self):
        """tests the division function"""
        result = TEST.ask(question="What is 2 divided by 2?")
        self.assertEqual(result, 1)

    @story('When I ask "What is <number> times <number>?", '
           'I want the application to give me the answer so I dont have to think')
    def test_multiplication(self):
        """tests the multiplication function"""
        result = TEST.ask(question="What is 2 times 2?")
        self.assertEqual(result, 4)

    @story('When I ask "What is love?" I want the application '
           'to say "Baby dont hurt me!", to let me know that computers have feelings too!')
    def test_love(self):
        """tests what is love"""
        result = TEST.ask(question="What is love?")
        self.assertEqual(result, "Baby Don't hurt me!!")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star'
           ' sign so I dont have to look it up online')
    def test_star_sign_invalid_month(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on 8 6!")
        self.assertEqual(result, "Please Enter a valid month")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_january_capricorn(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on January 8!")
        self.assertEqual(result, "You are a Capricorn")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_january_aquarius(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on January 30!")
        self.assertEqual(result, "You are a Aquarius")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star'
           ' sign so I dont have to look it up online')
    def test_star_sign_january_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on January 300!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_february_aquarius(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on February 8!")
        self.assertEqual(result, "You are a Aquarius")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_february_pisces(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on February 29!")
        self.assertEqual(result, "You are a Pisces")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_february_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on February 300!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_march_pisces(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on March 8!")
        self.assertEqual(result, "You are a Pisces")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_march_aries(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on March 30!")
        self.assertEqual(result, "You are a Aries")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_march_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on March 300!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_april_aries(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on April 8!")
        self.assertEqual(result, "You are a Aries")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_april_taurus(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on April 29!")
        self.assertEqual(result, "You are a Taurus")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_april_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on April 299!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_may_taurus(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on May 8!")
        self.assertEqual(result, "You are a Taurus")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_may_gemini(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on May 29!")
        self.assertEqual(result, "You are a Gemini")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_may_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on May 299!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>"'
           ' I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_june_gemini(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on June 8!")
        self.assertEqual(result, "You are a Gemini")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_june_cancer(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on June 28!")
        self.assertEqual(result, "You are a Cancer")

    @story('When I tell "My birthday is on <month> <day>"'
           ' I want the application to respond with my star '
           'sign so I dont have to look it up online')
    def test_star_sign_june_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on June 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_july_cancer(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on July 8!")
        self.assertEqual(result, "You are a Cancer")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_july_leo(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on July 28!")
        self.assertEqual(result, "You are a Leo")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_july_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on July 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_august_leo(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on August 8!")
        self.assertEqual(result, "You are a Leo")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_august_virgo(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on August 28!")
        self.assertEqual(result, "You are a Virgo")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_august_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on August 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_september_virgo(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on September 8!")
        self.assertEqual(result, "You are a Virgo")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_september_libra(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on September 28!")
        self.assertEqual(result, "You are a Libra")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_september_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on September 298!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_october_libra(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on October 8!")
        self.assertEqual(result, "You are a Libra")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_october_scorpio(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on October 28!")
        self.assertEqual(result, "You are a Scorpio")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_october_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on October 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_november_scorpio(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on November 8!")
        self.assertEqual(result, "You are a Scorpio")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_november_sagittarius(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on November 28!")
        self.assertEqual(result, "You are a Sagittarius")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_november_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on November 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I tell "My birthday is on <month> <day>"'
           ' I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_december_sagittarius(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on December 8!")
        self.assertEqual(result, "You are a Sagittarius")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign_december(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on December 28!")
        self.assertEqual(result, "You are a Capricorn")

    @story('When I tell "My birthday is on <month> <day>" '
           'I want the application to respond with my star sign '
           'so I dont have to look it up online')
    def test_star_sign__december_invalid(self):
        """test star sign"""
        result = TEST.ask(question="My birthday is on December 289!")
        self.assertEqual(result, "Not Valid date")

    @story('When I ask "What is the square root of <number>?", '
           'I want the application to give me the square root of '
           'the number given so I dont have to think')
    def test_square_root(self):
        """tests square root"""
        result = TEST.ask(question="What is the square root of 4?")
        self.assertEqual(result, 2)

    @story('When I ask "What is the name of this computer?", '
           'I want the application to give me the name of the '
           'computer so I dont have to look it up')
    def test_computer_name(self):
        """tests giving computer name"""
        result = TEST.ask(question="What is my computers name?")
        self.assertEqual(result, "The name of this computer is " + platform.node())

    @story('When I ask "Convert <number> <units> to <units>" '
           'I want to receive the converted value and units so I can know the answer.')
    def test_convert(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 feet to inch!")
        self.assertEqual(result, 12)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type1(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 12 inch to feet!")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type2(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 inch to feet!")
        self.assertEqual(result, 1.0 / 12.0)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type3(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 12 inch to feet!")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type4(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 mile to feet!")
        self.assertEqual(result, 5280)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type5(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 12 inch to feet!")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type6(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 mile to feet!")
        self.assertEqual(result, 5280)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type7(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 12 inch to feet!")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type8(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 mile to feet!")
        self.assertEqual(result, 5280)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type9(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 12 inch to feet!")
        self.assertEqual(result, 1)

    @story('When I ask for a numberic conversion I want at '
           'least 10 different units I can convert from/to')
    def test_type10(self):
        """Convert numbers to other numbers"""
        result = TEST.ask(question="Convert 1 mile to feet!")
        self.assertEqual(result, 5280)

    @story('When I ask "What is the meaning of life?" I want '
           'the application to say "42" so that I may be enlightened')
    def test_life(self):
        """tests wisdom"""
        result = TEST.ask(question="What is the meaning of life?")
        self.assertEqual(result, 42)
