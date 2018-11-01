import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='fichier à compiler', default="./programme.txt")
parser.add_argument('-o', help='fichier où pousser le code')
args = parser.parse_args()

filename = args.f
output_filename = args.o

with open(filename) as f:
    content = f.readlines()


instructions = utils.compile_instructions(content)


if not output_filename:
    for i in instructions:
        print(i)
else:
    with open(output_filename, 'w') as of:
        of.write('v2.0 raw\n')
        for i in instructions:
            of.write(i + '\n')

