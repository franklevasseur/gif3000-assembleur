from utils import CompilationException as CE


class Instruction:

    opcodes = {'NOP': 0, 'ADD': 1, 'SUB': 2, 'MUL': 3, 'AND': 4, 'MOV': 5, 'SHR': 6, 'SHL': 7, 'LD': 8, 'SD': 9}

    def __init__(self, line: int, brute_string: str):
        self.line = line
        self.brute_string = brute_string

    def compile(self):
        opcode_nibble = self.extract_opcode_nibble()
        registrers_nibble = self.extract_registers_nibble()
        middle_nibble = self.extract_middle_nibble()

        return '{:x}{:x}{:x}'.format(registrers_nibble, middle_nibble, opcode_nibble)

    def extract_opcode_nibble(self):

        string_opcode, _ = self.get_opcode()

        try:
            opcode_nibble = self.opcodes[string_opcode.upper()]
        except Exception:
            raise CE.CompilationException("ligne {}: un des opcodes ne fait pas partie des choix".format(self.line))

        return opcode_nibble

    def get_opcode(self):
        first_space_index = self.brute_string.find(' ')
        string_opcode = self.brute_string[:first_space_index]
        rest_of_line = self.brute_string[first_space_index:].strip()
        return string_opcode, rest_of_line

    def extract_registers_nibble(self):

        _, rest_of_line = self.get_opcode()

        comma_index = rest_of_line.find(',')
        rd = rest_of_line[:comma_index]
        rs = rest_of_line[comma_index + 1:].strip()
        rs = rs if rs.find(' ') == -1 else rs[:rs.find(' ')]  # truncate rest of line

        rd = self.get_register_id(rd)
        rs = self.get_register_id(rs)

        registrers_nibble = int(format(rd, "02b") + format(rs, "02b"), 2)

        return registrers_nibble

    def get_register_id(self, rx):
        return 0 if rx.upper() == 'PC' else int(rx[1])

    def extract_middle_nibble(self):
        immediate_index = self.brute_string.find('#')
        if immediate_index != -1:
            immediate = self.brute_string[immediate_index + 1:]
            return int(immediate)

        middle_nibble = 0
        return middle_nibble
