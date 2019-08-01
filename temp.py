
# -*- coding: utf-8 -*-

import src.editconllu as ed
from src.editsrl import SemanticRoleLabeling as srl
from conllu import parse_incr


def add_deprel_score(input_file, output_file):
    for each_line in input_file:
        string_buffer = each_line.strip()
        if len(string_buffer) < 1:
            print(file=output_file)
            continue
        if string_buffer[0] == '#':
            print(string_buffer, file=output_file)
            continue
        print(string_buffer + '\t' + '1.0', file=output_file)


def open_read_file_utf8(file_path):
    return open(file_path, 'r', encoding='utf-8-sig')


input_dir_path = ''
output_dir_path = ''
input_file_path = ''
output_file_path = ''

data_file_path = ''
data_dir_path = ''
