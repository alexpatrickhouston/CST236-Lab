from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_4sided_type
from source.answers import what_time, life, fibonacci, open_door, clear_memory, convert, digit_pi

import difflib

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'


class Interface(object):
    def __init__(self):

        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', 'Why', 'Convert', 'Please', 'Open']
        self.question_mark = chr(0x3F)
        self.exclamation_mark = chr(0x21)
        self.backup_questions = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_4sided_type),
            'What time is it ?': QA("What time is it ?", what_time),
            'What is the meaning of life?': QA("What is the meaning of life?", life),
            'What is the digit of pi?': QA("What is the digit of pi?", digit_pi),
            'What is the digit of fibonacci?': QA("What is the digit of fibonacci?", fibonacci),
            'Open the door Hal!': QA("Open the door Hal!", open_door),
            'Please clear memory!': QA("Please clear memory!", clear_memory),
            'Convert to': QA("Convert to", convert)

        }
        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_4sided_type),
            'What time is it ?': QA("What time is it ?", what_time),
            'What is the meaning of life?': QA("What is the meaning of life?", life),
            'What is the digit of pi?': QA("What is the digit of pi?", digit_pi),
            'What is the digit of fibonacci?': QA("What is the digit of fibonacci?", fibonacci),
            'Open the door Hal!': QA("Open the door Hal!", open_door),
            'Please clear memory!': QA("Please clear memory!", clear_memory),
            'Convert to': QA("Convert to", convert)

        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question[-1] != self.question_mark and question[-1] != self.exclamation_mark or question.split(' ')[
            0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    args.append(float(keyword))
                except:
                    parsed_question += "{0} ".format(keyword)
            parsed_question = parsed_question[0:-1]
            self.last_question = parsed_question
            for answer in self.question_answers.values():
                if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                    if answer.function is None:
                        return answer.value
                    else:
                        try:
                            print args
                            return answer.function(*args)
                        except Exception as ex:
                            print ex.message
                            raise Exception("Too many extra parameters")
            else:
                return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)

    def clear(self):
        self.question_answers = self.backup_questions
