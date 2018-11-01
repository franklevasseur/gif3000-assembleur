opcodes = {'NOP': 1, 'ADD': 2, 'SUB': 3, 'MUL': 4, 'AND': 5, 'MOV': 6, 'SHR': 7, 'SHL': 8, 'LD': 9, 'SD': 10}


class CompilationException(Exception):
    pass


def compile_instructions(content):
    content = [x.strip() for x in content]
    content = [l for l in content if l]

    returned_instructions = []

    for l in content:
        opcode_nibble, rest_of_line = extract_opcode_nibble(l)
        registrers_nibble = extract_registers_nibble(rest_of_line)
        middle_nibble = extract_middle_nibble(l)

        returned_instructions.append('{:x}{:x}{:x}'.format(registrers_nibble, middle_nibble, opcode_nibble))

    return returned_instructions


def extract_opcode_nibble(l):
    first_space_index = l.find(' ')
    string_opcode = l[:first_space_index]

    try:
        opcode_nibble = opcodes[string_opcode.upper()]
    except:
        raise CompilationException("un des opcodes ne fait pas partie des choix")

    rest_of_line = l[first_space_index:].strip()

    return opcode_nibble, rest_of_line


def extract_registers_nibble(rest_of_line):
    comma_index = rest_of_line.find(',')
    rd = rest_of_line[:comma_index]
    rs = rest_of_line[comma_index + 1:].strip()
    rs = rs if rs.find(' ') == -1 else rs[:rs.find(' ')] # truncate rest of line

    getRegisterId = lambda rx: 0 if rx.upper() == 'PC' else int(rx[1])
    rd = getRegisterId(rd)
    rs = getRegisterId(rs)

    registrers_nibble = int(format(rd, "02b") + format(rs, "02b"), 2)

    return registrers_nibble


def extract_middle_nibble(l):
    immediate_index = l.find('#')
    if immediate_index != -1:
        immediate = l[immediate_index + 1:]
        return int(immediate)

    middle_nibble = 0
    return middle_nibble

