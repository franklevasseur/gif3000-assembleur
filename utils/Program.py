from utils.Instruction import *


class Program:
    def __init__(self, code):
        content = [x.strip() for x in code]
        self.instructions = [Instruction(i, l) for (i, l) in enumerate(content) if l]

    def compile(self):
        return [i.compile() for i in self.instructions]

