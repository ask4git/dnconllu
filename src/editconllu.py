
# -*- coding: utf-8 -*-

import os
import glob
from conllu import parse_incr


def edit_dir_corpus(target_dir, data_dir):
    target_file_list = glob.glob(target_dir + '\\*.conllu')
    data_file_list = glob.glob(data_dir + '\\*.conllu')
    for target_file_name in target_file_list:
        print(target_file_name)


def delete_column(input_file, output_file):
    """
    input_file의 마지막 column을 삭제해서 output_file에 저장
    :param input_file:
    :param output_file:
    :return:
    """
    for each_line in input_file:
        string_buffer = each_line.strip()
        if len(string_buffer) < 1:
            print(file=output_file)
            continue
        if string_buffer[0] == '#':
            print(string_buffer, file=output_file)
            continue
        string_buffer = string_buffer.split('\t')[:-1]
        print('\t'.join(string_buffer), file=output_file)


def scrap_column(target_file, column_name):
    """
    파일에서 특정 column의 정보만 return
    :param target_file:
    :param column_name:
    :return:
    """
    columndata = dict()
    tokenlist = parse_incr(target_file)
    for token in tokenlist:
        sent_id = str(token.metadata['sent_id'])
        if sent_id not in columndata:
            columndata[sent_id] = []
        for wordtoken in token:
            columndata[sent_id].append(str(wordtoken[str(column_name)]))
    return columndata


def add_column(target_file, add_file, column_name, output_file):
    """
    target_file 뒤에 add_file의 column_name을 추가
    :param target_file:
    :param add_file:
    :param column_name:
    :param output_file:
    :return:
    """
    columndata = scrap_column(add_file, column_name)
    sent_id = ''
    idx = 0
    for each_line in target_file:
        string_buffer = each_line.strip()
        if len(string_buffer) < 1:
            print(file=output_file)
            continue
        if string_buffer[0] == '#':
            if string_buffer[:6] == '# sent':
                idx = 0
                sent_id = str(string_buffer[11:].strip())

            print(string_buffer, file=output_file)
            continue
        print(string_buffer + '\t' + str(columndata[sent_id][idx]), file=output_file)
        idx += 1


def swich_conllu_column(input_file, output_file, a, b):
    """
    input_file의 a column과 b column의 값을 바꾸고 output_file에 저장
    :param input_file:
    :param output_file:
    :param a:
    :param b:
    :return:
    """
    for each_line in input_file:
        string = each_line.strip()
        if len(string) < 1:
            print(string, file=output_file)
            continue
        if string[0] == '#':
            print(string, file=output_file)
            continue
        string = string.split('\t')
        try:
            temp = string[a]
            string[a] = string[b].strip()
            string[b] = temp.strip()
        except IndexError as e:
            print(e)
            print('origin data error: ', string)
        print('\t'.join(string), file=output_file)


def switch_misc_deps(input_file, output_file):
    """
    문장의 의미역정보를 misc에서 deps로 이동
    :param input_file:
    :param output_file:
    :return:
    """
    for each_line in input_file:
        string = each_line.strip()
        if len(string) < 1:
            print(string, file=output_file)
            continue
        if string[0] == '#':
            print(string, file=output_file)
            continue
        string = string.split('\t')
        try:
            temp = string[9]
            string[9] = string[8].strip()
            string[8] = temp.strip()
        except IndexError as e:
            print(e)
            print('origin data error: ', string)
        print('\t'.join(string), file=output_file)


def split_to_conllu_corpus(input_file, output_dir_path, num_of_sent=1000):
    """
    말뭉치를 분할
    :param input_file:
    :param output_dir_path:
    :param num_of_sent:
    :return:
    """

    def open_output_file(_output_dir_path, _output_file_name, _file_index):
        return open(_output_dir_path + '\\' + _output_file_name + '_' + str(_file_index).zfill(3) +
                    '.conllu', 'w', encoding='utf-8-sig')

    file_name = os.path.splitext(input_file.name)
    file_name = os.path.split(file_name[0])
    output_file_name = file_name[1]
    file_index = 0
    _num_of_sent = 0
    output_file = open_output_file(output_dir_path, output_file_name, file_index)

    for tokenlist in parse_incr(input_file):

        if _num_of_sent >= num_of_sent:
            file_index += 1
            _num_of_sent = 0
            output_file = open_output_file(output_dir_path, output_file_name, file_index)

        _num_of_sent += 1
        print(tokenlist.serialize().strip(), file=output_file)
        print(file=output_file)
