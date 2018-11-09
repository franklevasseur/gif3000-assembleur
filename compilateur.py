import argparse
from utils.Program import Program

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='fichier à compiler', default="./programme.txt")
parser.add_argument('-o', help='fichier où pousser le code')
args = parser.parse_args()

filename = args.f
output_filename = args.o

with open(filename) as f:
    file_content = f.readlines()

program = Program(file_content)
compiled_program = program.compile()

if not output_filename:
    for i in compiled_program:
        print(i)
else:
    with open(output_filename, 'w') as of:
        of.write('v2.0 raw\n')
        for i in compiled_program:
            of.write(i + '\n')

