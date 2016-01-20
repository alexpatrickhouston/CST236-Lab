"""
Testing of requirements for the questions asked
"""

from unittest import TestCase  # imports testing tools

from plugins.ReqTracer import requirements  # imports the requirements checker
from source.main import Interface

test = Interface()  # test interface


class testAsk(TestCase):
    @requirements(['#0006', '#0008', '#0009'])
    def test_integer(self):
        self.assertRaises(Exception, test.ask, question=2)


    @requirements(['#0007','#0019', '#0014'])
    def test_who(self):
        result = test.ask(question="Who ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014'])
    def test_what(self):
        result = test.ask(question="What ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014'])
    def test_why(self):
        result = test.ask(question="Why ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014'])
    def test_where(self):
        result = test.ask(question="Where ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0009'])
    def test_how(self):
        result = test.ask(question="How do you eat a tiger ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")
