opcodes = {'NOP': 1, 'ADD': 2, 'SUB': 3, 'MUL': 4, 'AND': 5, 'MOV': 6, 'SHR': 7, 'SHL': 8, 'LD': 9, 'SD': 10}


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
        raise Exception("un des opcodes ne fait pas partie des choix")

    rest_of_line = l[first_space_index:].strip()

    return opcode_nibble, rest_of_line


def extract_registers_nibble(rest_of_line):
    comma_index = rest_of_line.find(',')
    rd = rest_of_line[:comma_index]
    rs = rest_of_line[comma_index + 1:].strip()

    getRegisterId = lambda rx: 0 if rx.upper() == 'PC' else int(rx[1])
    rd = getRegisterId(rd)
    rs = getRegisterId(rs)

    if abs(rd) > 3 or abs(rs) > 3:
        raise Exception("les registres doivent être compris entre R0 et R3 ou PC.")

    registrers_nibble = int(format(rd, "b") + format(rs, "b"), 2)

    return registrers_nibble


def extract_middle_nibble(l):
    immediate_index = l.find('#')
    if immediate_index != -1:
        immediate = l[immediate_index + 1:]
        return int(immediate)

    middle_nibble = 0
    return middle_nibble

