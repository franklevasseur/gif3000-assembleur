import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='fichier à compiler')
args = parser.parse_args()

filename = args.f
if not filename:
    filename = './programme.txt'

opcodes = {'NOP': 1, 'ADD': 2, 'SUB': 3, 'MUL': 4, 'AND': 5, 'MOV': 6, 'SHR': 7, 'SHL': 8, 'LD': 9, 'SD': 10}

with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]
content = [l for l in content if l]

i = 0
for l in content:
    first_space_index = l.find(' ')
    string_opcode = l[:first_space_index]
    opcode_nibble = opcodes[string_opcode.upper()]

    registrers = l[first_space_index:].strip()

    comma_index = registrers.find(',')
    rd = registrers[:comma_index]
    rs = registrers[comma_index + 1:].strip()

    getRegisterIndex = lambda rx: 0 if rx.upper() == 'PC' else int(rx[1])
    rd = getRegisterIndex(rd)
    rs = getRegisterIndex(rs)

    registrers_nibble = int(format(rd, "b") + format(rs, "b"), 2)

    immediate_index = l.find('#')
    immediate = l[immediate_index+1:] if immediate_index != -1 else None

    print('{:x}{:x}{:x}'.format(registrers_nibble, 0 if not immediate else int(immediate), opcode_nibble))

