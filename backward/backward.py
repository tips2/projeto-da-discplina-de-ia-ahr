from .read import read
from .evaluate import evaluate


class Backward:
    def __init__(self):
        self.context = {}
        self.ask = {}

    def read(self, text):
        return read(text)

    def evaluate(self, text):
        return evaluate(self.context, self.read(text), self.ask)

    def bind_question(self, text, question):
        self.ask[text] = question
