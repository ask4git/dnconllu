
# dependency_relations.py
# -*- coding: utf-8 -*-

"""
Modules for ...
"""

import statistics
import re
import glob
import os

CNU = 0     # 충남대
ETRI = 1    # ETRI
KNU = 2     # 강원대
CBNU = 3    # 전북대


class DependencyRelations:
    @staticmethod
    def create_deprel_data(path_input_dir):
        """
        conllu 형식의 말뭉치에서 의존관계에 필요한 정보만 추출해서 dict() 형식으로 return

        :param path_input_dir:
        :return:
        """

        file_list = glob.glob(path_input_dir + '*.txt')
        dictionary = dict()

        try:
            for file_name in file_list:
                with open(file_name, 'r', encoding='utf-8-sig') as input_file:
                    sentence_id = 0
                    for each_line in input_file:
                        string_buffer = each_line.strip()
                        if len(string_buffer) < 1:
                            continue
                        if string_buffer[0] == '#':
                            if string_buffer[2:6] == 'sent':
                                sentence_id = int(string_buffer[12:])
                        else:
                            string_buffer = string_buffer.split('\t')
                            key = str(int(sentence_id * 1000) + int(string_buffer[0]))
                            if key not in dictionary:
                                dictionary[key] \
                                    = '\t'.join([str(sentence_id), string_buffer[0], string_buffer[6], string_buffer[7]])
        except FileNotFoundError as error:
            print('DependencyRelations.corpus_to_table()', error)
        except IndexError as error:
            print('DependencyRelations.corpus_to_table()', error)

        # =========================
        # for key, value in dictionary.items():
        #     print(key, " : ", value)
        # =========================

        return dictionary

    @staticmethod
    def merge_deprel_data(path_cnu_corpus, path_etri_corpus, path_knu_corpus, path_cbnu_corpus,
                          path_input_file, path_output_file):
        """
        여러기관의 말뭉치의 의존관계정보를 하나의 파일로 추합

        :param path_cnu_corpus:
        :param path_etri_corpus:
        :param path_knu_corpus:
        :param path_cbnu_corpus:
        :param path_input_file:
        :param path_output_file:
        :return:
        """
        cnu_deprel_dict = DependencyRelations.create_deprel_data(path_cnu_corpus)
        etri_deprel_dict = DependencyRelations.create_deprel_data(path_etri_corpus)
        knu_deprel_dict = DependencyRelations.create_deprel_data(path_knu_corpus)
        cbnu_deprel_dict = DependencyRelations.create_deprel_data(path_cbnu_corpus)

        try:
            with open(path_input_file, 'r', encoding='utf-8-sig') as input_file, \
                    open(path_output_file, 'w', encoding='utf-8-sig') as output_file:
                sentence_id = 0
                for each_line in input_file:
                    string_buffer = each_line.strip()
                    if len(string_buffer) < 1:
                        continue
                    if string_buffer[0] == '#':
                        if string_buffer[2:6] == 'sent':
                            sentence_id = int(string_buffer[12:])
                    else:
                        string_buffer = string_buffer.split('\t')
                        key = str(int(sentence_id * 1000) + int(string_buffer[0]))
                        cnu_data = cnu_deprel_dict[key].split('\t')
                        etri_data = etri_deprel_dict[key].split('\t')
                        knu_data = knu_deprel_dict[key].split('\t')
                        cbnu_data = cbnu_deprel_dict[key].split('\t')

                        print('\t'.join([key, str(sentence_id), string_buffer[0], string_buffer[1],
                                         cnu_data[2], cnu_data[3],
                                         etri_data[2], etri_data[3],
                                         knu_data[2], knu_data[3],
                                         cbnu_data[2], cbnu_data[3]]), file=output_file)

        except FileNotFoundError as error:
            print('DependencyRelations.tmp()', error)
        except IndexError as error:
            print('DependencyRelations.tmp()', error)

    @staticmethod
    def compare_deprel_sentence(_ref, _tar):
        """
        의존관계에 필요한 정보를 서로 비교해서 문장 단위로 UAS LAS 를 파일과 console 에 출력

        :param _ref:
        :param _tar:
        :return:
        """
        deprel_dictionary = dict()

        try:
            with open('..\\res\\deprel\\sample.txt', 'r', encoding='utf-8-sig') as deprel_data:
                for each_line in deprel_data:
                    string_buffer = each_line.strip().split('\t')
                    if str(string_buffer[1]) in deprel_dictionary:
                        pass
                    else:
                        # sent_length, uas, las
                        deprel_dictionary[string_buffer[1]] = list([0] * 5)
                    ref_head_id = string_buffer[(_ref + 2) * 2]
                    ref_deprel = string_buffer[((_ref + 2) * 2) + 1]
                    tar_head_id = string_buffer[(_tar + 2) * 2]
                    tar_deprel = string_buffer[((_tar + 2) * 2) + 1]

        except FileNotFoundError as error:
            print('DependencyRelations.tmp()', error)
        except IndexError as error:
            print('DependencyRelations.tmp()', error)
        pass

    @staticmethod
    def scraping_deprel(path_dir):
        try:
            filenames = os.listdir(path_dir)

            for filename in filenames:
                if os.path.isdir(os.path.join(path_dir, filename)):
                    filelist = glob.glob(os.path.join(path_dir, filename) + '\\*.txt')

                    for filepath in filelist:
                        with open(filepath, 'r', encoding='utf-8-sig') as file:
                            for each_line in file:
                                print(each_line.strip())



        except PermissionError as error:
            print('DependencyRelations.scraping_deprel()', error)

    @staticmethod
    def scoring_in_deprel_sentence():
        """

        :return:
        """
        pass


if __name__ == '__main__':
    DependencyRelations.scraping_deprel('..\\res\\sample\\deprel\\data')
