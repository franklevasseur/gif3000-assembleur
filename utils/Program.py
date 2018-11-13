from utils.Instruction import *


class Program:
    def __init__(self, code):
        content = [x.strip() for x in code]
        comments_free_code = [self.remove_comment(l) for l in content]
        self.instructions = [Instruction(i, s) for (i, s) in enumerate(comments_free_code) if s]

    def compile(self):
        return [i.compile() for i in self.instructions]

    @staticmethod
    def remove_comment(line_of_code):
        comment_index = line_of_code.find('//')
        return line_of_code[:comment_index] if comment_index != -1 else line_of_code

