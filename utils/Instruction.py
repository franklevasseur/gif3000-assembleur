from utils import CompilationException as CE
import re


class Instruction:

    opcodes = {'NOP': 0, 'ADD': 1, 'SUB': 2, 'MUL': 3, 'AND': 4, 'MOV': 5, 'SHR': 6, 'SHL': 7, 'LD': 8, 'SD': 9}
    conditions = {'Z': 4, 'NZ': 5, 'C': 6, 'NC': 7}

    def __init__(self, line: int, brute_string: str):
        self.line = line
        self.brute_string = brute_string.upper()

        opcode, rest_of_line = self.get_opcode(self.brute_string)
        condition, resulting_opcode = self.extract_condition(opcode)

        self.opcode = resulting_opcode
        self.condition = condition
        self.rest_of_line = rest_of_line

    @staticmethod
    def get_opcode(brute_string):
        first_space_index = brute_string.find(' ')
        string_opcode = brute_string[:first_space_index]
        rest_of_line = brute_string[first_space_index:].strip()
        return string_opcode, rest_of_line

    @staticmethod
    def extract_condition(opcode: str):
        matchs_object = re.search("(NZ|NC|Z|C)$", opcode)
        if matchs_object:
            first_match = matchs_object.regs[0]
            condition: str = opcode[first_match[0]: first_match[1]]
            resulting_opcode: str = opcode[:first_match[0]]
            return condition, resulting_opcode

        return None, opcode

    def compile(self):
        opcode_nibble = self.extract_opcode_nibble()
        registrers_nibble = self.extract_registers_nibble()
        middle_nibble = self.extract_middle_nibble()

        returned_hexa = '{:x}{:x}{:x}'.format(registrers_nibble, middle_nibble, opcode_nibble)

        return returned_hexa.upper()

    def extract_opcode_nibble(self):
        try:
            opcode_nibble: int = self.opcodes[self.opcode]
        except Exception:
            raise CE.CompilationException("ligne {}: un des opcodes ne fait pas partie des choix ({})"
                                          .format(self.line, self.opcode))

        return opcode_nibble

    def extract_registers_nibble(self):

        comma_index = self.rest_of_line.find(',')
        rd = self.rest_of_line[:comma_index]
        rs = self.rest_of_line[comma_index + 1:].strip()
        rs = rs if rs.find(' ') == -1 else rs[:rs.find(' ')]  # truncate rest of line

        get_register_id = lambda rx: 0 if rx.upper() == 'PC' else int(rx[1])
        rd = get_register_id(rd)
        rs = get_register_id(rs)

        registrers_nibble: int = int(format(rd, "02b") + format(rs, "02b"), 2)

        return registrers_nibble

    def extract_middle_nibble(self):
        immediate_index = self.brute_string.find('#')
        update_flag_index = self.brute_string.find('-F')

        if immediate_index != -1 and update_flag_index != -1:
            raise CE.CompilationException("ligne {}: il est impossible de passer une immediate "
                                          "ET demander un update de flags"
                                          .format(self.line))

        if immediate_index != -1:

            if self.opcode not in ['LD', 'SD']:
                raise CE.CompilationException("ligne {}: une valeur immediate n'est permis que sur un LD ou SD"
                                          .format(self.line))

            immediate = self.brute_string[immediate_index + 1:]
            return int(immediate)

        middle_nibble: int = 0

        if update_flag_index != -1:

            if self.opcode in ['LD', 'SD']:
                raise CE.CompilationException("ligne {}: il est impossible d'updater les flags sur un LD ou SD"
                                          .format(self.line))

            middle_nibble += 8

        if self.condition:
            middle_nibble += self.conditions[self.condition]

        return middle_nibble
