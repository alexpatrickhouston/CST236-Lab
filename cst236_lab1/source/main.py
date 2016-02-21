from source.question_answer import QA
from source.shape_checker import get_triangle_type, get_4sided_type
from source.answers import what_time, life, fibonacci, open_door, convert, digit_pi, lucky_number, square_root, computer_name, star_sign, divide, subtract, love, multiply, add
from source.git_utils import is_file_in_repo,has_untracked_files, has_diff_files, get_git_file_info, get_file_info, get_repo_branch, get_repo_url
import difflib

NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
question_values = ('inch','mm','um','nm','cm','kilometer','mile','feet','yards','meters','January','February','March','April','May','June','July','August','September','October','November','December')

class Interface(object):
    def __init__(self):

        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', 'Why', 'Convert', 'Please', 'Open','My' ,'Is']
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
            'Convert to': QA("Convert to", convert),
            'What is my lucky number?': QA("What is my lucky number?", lucky_number),
            'What is divded by ?': QA('What is divided by ?', divide),
            'What is plus ?': QA('What is plus ?', add),
            'What is minus ?': QA('What is minus ?', subtract),
            'What is times ?': QA('What is times ?', multiply),
            'What is love?': QA('What is love?', love),
            'What is my computers name?': QA('What is my computers name?', computer_name),
            'My birthday is on !':QA('My birthday is on !', star_sign),
            'What is the square root of ?': QA('What is the sqaure root of ?', square_root),
            'Is in the repo?': QA('Is in the repo?', is_file_in_repo),
            'What is the status of ?': QA('What is the status of?', get_git_file_info),
            'What is the deal with ?': QA('What is the deal with ?', get_file_info),
            'What branch is ?': QA('What branch is ?', get_repo_branch),
            'Where did come from?': QA('Where did come from?', get_repo_url)

        }
        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_4sided_type),
            'What time is it ?': QA("What time is it ?", what_time),
            'What is the meaning of life?': QA("What is the meaning of life?", life),
            'What is the digit of pi?': QA("What is the digit of pi?", digit_pi),
            'What is the digit of fibonacci?': QA("What is the digit of fibonacci?", fibonacci),
            'Open the door Hal!': QA("Open the door Hal!", open_door),
            'Convert to': QA("Convert to", convert),
            'What is my lucky number?': QA("What is my lucky number?", lucky_number),
            'What is divded by ?': QA('What is divided by ?', divide),
            'What is plus ?': QA('What is plus ?', add),
            'What is minus ?': QA('What is minus by ?', subtract),
            'What is times ?': QA('What is times ?', multiply),
            'What is love?': QA('What is love?', love),
            'What is my computers name?': QA('What is my computers name?', computer_name),
            'My birthday is on !':QA('My birthday is on !', star_sign),
            'What is the square root of ?': QA('What is the sqaure root of ?', square_root),
            'Is in the repo?': QA('Is in the repo?', is_file_in_repo),
            'What is the status of ?': QA('What is the status of?', get_git_file_info),
            'What is the deal with ?': QA('What is the deal with ?', get_file_info),
            'What branch is ?': QA('What branch is ?', get_repo_branch),
            'Where did come from?': QA('Where did come from?', get_repo_url)

        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')
        if question == 'Please clear memory!':
            self.clear()
            return "Memory cleared"
        elif question[-1] != self.question_mark and question[-1] != self.exclamation_mark or question.split(' ')[
            0] not in self.keywords:
            self.last_question = None
            return NOT_A_QUESTION_RETURN
        else:
            parsed_question = ""
            args = []
            for keyword in question[:-1].split(' '):
                try:
                    if keyword=="":
                        continue
                    elif keyword in question_values:
                        args.append(keyword)
                    elif keyword[0] == '<' and keyword[-1] == '>':
                        print("This keyword was removed :"+keyword);
                        args.append(keyword[1:-1])
                        print("This keyword was removed :"+keyword);

                    else:
                        args.append(float(keyword))

                except:
                    parsed_question += "{0} ".format(keyword)
            print(parsed_question)
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
                            import traceback
                            traceback.print_exc()
                            print ex.message
                            print args
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
