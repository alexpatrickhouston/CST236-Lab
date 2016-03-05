class QA(object):
    """question object"""
    def __init__(self, question, answer):
        """dammit python this is a freaking init"""
        self.question = question
        self.function = None
        self.value = None
        if hasattr(answer, '__call__'):
            self.function = answer
        else:
            self.value = answer
