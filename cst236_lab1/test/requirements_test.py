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


    @requirements(['#0007','#0019', '#0014','#0015'])
    def test_who(self):
        result = test.ask(question="Who ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014','#0015'])
    def test_what(self):
        result = test.ask(question="What ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014','#0015'])
    def test_why(self):
        result = test.ask(question="Why ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014','#0015'])
    def test_where(self):
        result = test.ask(question="Where ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0007','#0019','#0014','#0015'])
    def test_how(self):
        result = test.ask(question="How ?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0009'])
    def test_questionmark(self):
        result = test.ask(question="How do you eat a tiger")
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0010'])
    def test_commas(self):
        result = test.ask(question="How,do,i.eat,a,panda,?")
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0021','#0017'])
    def test_no_question(self):
        result = test.teach(answer='42')
        self.assertEqual(result, "Please ask a question first")

    @requirements(['#0013'])
    def test_valid_match(self):
        test.ask(question="Why are we here?")
        test.teach(answer="to become nerds")
        result = test.ask(question="Why are we here?")
        self.assertEqual(result, "to become nerds")

    @requirements(['#0016','#0018','#0020'])
    def test_already_answered(self):
        test.ask(question="Why are we here?")
        test.teach(answer="to become nerds")
        test.ask(question="Why are we here?")
        result = test.teach(answer="because reasons")
        self.assertEqual(result, "I don't know about that. I was taught differently")

    @requirements(['#0012'])
    def test_exclude_number(self):
        result = test.ask(question="2 + 3 ?")
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0011'])
    def test_90_correct(self):
        test.ask(question="How How How how how how how how how blarg?")
        test.teach(answer="because i said so")
        result = test.ask(question="How How How how how how how how how blrg?")
        self.assertEqual(result, "because i said so")

    @requirements(['#0011'])
    def test_80_correct(self):
        test.ask(question="How How How how how how how how how blarg?")
        test.teach(answer="because i said so")
        result = test.ask(question="How How How how how how how berg berg blrg?")
        self.assertEqual(result, "I don't know, please provide the answer")