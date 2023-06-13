import sys
import os

def txt_importer(path_file):
    if not os.path.isfile(path_file):
        sys.stderr.write('Arquivo {} não encontrado\n'.format(path_file))
        return

    if not path_file.endswith(".txt"):
        sys.stderr.write('Formato inválido\n')
        return

    with open(path_file, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        return lines
